from flask import Flask, jsonify, render_template, url_for, redirect, request
from pyftdi.ftdi import USBError, FtdiError
from FT2232H import *

app = Flask(__name__)

@app.route('/getAll', methods=['GET'])
def get_all_boards():
    """Returns FTDI GPIO Data
    Accesed by GET-Request to URL http://127.0.0.1:5000/getAll

    :return: Returns GPIO Data in JSON format (register, direction, GPIO (port, pin, output_state, input_state), name)
    """
    return jsonify(ftdi0.map_string_to_gpio)


@app.route('/readGPIO', methods=['GET'])
def send_json_data():
    """Reades GPIO.
    Accesed by GET-Request to URL http://127.0.0.1:5000/readGPIO.
    GET-Request requires JSON Data with information about the GPIO (e.g. AD0)
    JSON format example: {'GPIO':'AD0'}

    :return: JSON Data (e.g. {'GPIO':'AD0', 'state':1}
    """
    if request.is_json:
        json_data = request.get_json()
        gpio = json_data.get('GPIO')
        return jsonify({'GPIO':gpio, 'state':ftdi0.map_string_to_gpio[gpio]['GPIO']['input_state']})

@app.route('/setup', methods=['GET','POST'])
def setup():
    """Renders HTML page for FTDI setup if accessed by Webbrowser.
    Accesed by URL http://127.0.0.1:5000/setup
    By clicking the 'Apply' Button on the Webpage, the direction settings are applied to the FTDI.
    Then the you will be redirected to the GUI page.

    :return: Returns Webpage or redirect to GUI page
    """
    if request.method == 'POST':
        mask_direction_interface1, mask_direction_interface2 = ftdi0.get_input_output_from_request(request.form)
        ftdi0.set_direction_2(bitmask_i1=mask_direction_interface1, bitmask_i2=mask_direction_interface2)
        return redirect(url_for('gui'))
    return render_template('setup.html')



@app.route('/toggleGPIO', methods=['POST'])
def toggleGPIO():
    """Toogles GPIO.
    Accesed by POST-Request to URL http://127.0.0.1:5000/writeGPIO.
    Normally this request is made by the GUI, is however availaible via raw request
    POST-Request requires JSON Data with information about GPIO (e.g. AD0)
    JSON format example: {'GPIO':'AD0', 'state':'HIGH'}

    :return: Returns JSON Data e.g. {'msg':'AD0}. In case of an error, the msg-content will be 'fail'.
    """
    if request.is_json:
        json_data = request.get_json()
        gpio = json_data.get("GPIO")
        out_state = ftdi0.map_string_to_gpio[gpio]['GPIO']['output_state']

        if (out_state):
            ftdi0.write_GPIO_LOW(gpio=gpio)
        else:
            ftdi0.write_GPIO_HIGH(gpio=gpio)

        return jsonify({'msg': gpio})
    else:
        return jsonify({'msg': 'fail'})

@app.route('/writeGPIO', methods=['POST'])
def writeGPIO():
    """Writes state to GPIO.
    Accesed by POST-Request to URL http://127.0.0.1:5000/writeGPIO.
    POST-Request requires JSON Data with information about GPIO (e.g. AD0) and state (HIGH or LOW).
    JSON format example: {'GPIO':'AD0', 'state':'HIGH'}

    :return:
    """
    if request.is_json:
        json_data = request.get_json()
        gpio = json_data.get('GPIO')
        state = json_data.get('state')
        if int(state) == 1:
            ftdi0.write_GPIO_HIGH(gpio=gpio)
        else:
            ftdi0.write_GPIO_LOW(gpio=gpio)
        return jsonify({gpio: state})

@app.route('/setGPIODirection', methods=['POST'])
def setGPIODirection():
    """Writes GPIO direction.
    Accesed by POST-Request to URL http://127.0.0.1:5000/setGPIODirection.
    POST-Request requires JSON Data with information about GPIO (e.g. AD0) and direction (input or output).
    JSON format example: {'GPIO':'AD0', 'direction':'output'}

    :return:
    """
    if request.is_json:
        json_data = request.get_json()
        gpio = json_data.get('GPIO')
        direction = json_data.get('direction')
        ftdi0.set_gpio_direction(gpio=gpio, direction=direction)
        return jsonify({'GPIO':gpio, 'direction': direction})

@app.route('/gui', methods=['POST','GET'])
def gui():
    """GUI which provides control over the state of output GPIOs and shows the state of input and output GPIOs.
    Accessed over Webrowser on URL http://127.0.0.1:5000/gui

    :return: Rendered HTML page
    """
    return render_template('gui2.html', io_array=ftdi0.get_direction_array(), color=ftdi0.getColor())


@app.route('/getColorJSON', methods=['GET'])
def getColorJSON():
    """Returns state colors of GPIO (green: HIGH, silver: LOW) used by polling JavaScript which keeps the GUI page updated.
    Accesed by GET-Request to URL http://127.0.0.1:5000/getColorJSON.

    :return: JSON Data
    """
    colors = ftdi0.getColor()
    return jsonify(colors)

@app.route('/getIOJSON', methods=['GET'])
def getIOJSON():
    """Returns direction state of GPIO (input, output) used by polling JavaScript which keeps the GUI page updated.
    Accesed by GET-Request to URL http://127.0.0.1:5000/getIOJSON.

    :return: JSON Data
    """
    io_array = ftdi0.get_direction_array()
    return jsonify(io_array)


if __name__ == '__main__':
    ftdi0 = FTDI2232H(url='ftdi://ftdi:2232:FTWWP6IJ/1')
    app.run()

