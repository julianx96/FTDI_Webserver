from flask import Flask, jsonify, render_template, url_for, redirect, request
from pyftdi.ftdi import USBError, FtdiError
from FT2232H import *
from multiprocessing import Process

import pyvisa
#from sys import exit

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
        ftdi = json_data.get("FTDI")
        gpio = json_data.get('GPIO')
        if int(ftdi) == 0:
            ftdi0.read_input_gpio()
            return jsonify({'GPIO':gpio, 'state':ftdi0.map_string_to_gpio[gpio]['GPIO']['input_state']})
        elif int(ftdi) == 1:
            ftdi1.read_input_gpio()
            return jsonify({'GPIO':gpio, 'state':ftdi1.map_string_to_gpio[gpio]['GPIO']['input_state']})
        elif int(ftdi) == 2:
            ftdi2.read_input_gpio()
            return jsonify({'GPIO':gpio, 'state':ftdi2.map_string_to_gpio[gpio]['GPIO']['input_state']})
        elif int(ftdi) == 3:
            ftdi3.read_input_gpio()
            return jsonify({'GPIO':gpio, 'state':ftdi3.map_string_to_gpio[gpio]['GPIO']['input_state']})
        elif int(ftdi) == 4:
            ftdi4.read_input_gpio()
            return jsonify({'GPIO':gpio, 'state':ftdi4.map_string_to_gpio[gpio]['GPIO']['input_state']})

@app.route('/setup/<num>', methods=['GET','POST'])
def setup(num):
    """Renders HTML page for FTDI setup if accessed by Webbrowser.
    Accesed by URL http://127.0.0.1:5000/setup
    By clicking the 'Apply' Button on the Webpage, the direction settings are applied to the FTDI.
    Then the you will be redirected to the GUI page.

    :return: Returns Webpage or redirect to GUI page
    """
    if request.method == 'POST':
        if int(num) == 0:
            mask_direction_interface1, mask_direction_interface2 = ftdi0.get_input_output_from_request(request.form)
            ftdi0.set_direction_2(bitmask_i1=mask_direction_interface1, bitmask_i2=mask_direction_interface2)
        elif int(num) == 1:
            mask_direction_interface1, mask_direction_interface2 = ftdi1.get_input_output_from_request(request.form)
            ftdi1.set_direction_2(bitmask_i1=mask_direction_interface1, bitmask_i2=mask_direction_interface2)
        elif int(num) == 2:
            mask_direction_interface1, mask_direction_interface2 = ftdi2.get_input_output_from_request(request.form)
            ftdi2.set_direction_2(bitmask_i1=mask_direction_interface1, bitmask_i2=mask_direction_interface2)
        elif int(num) == 3:
            mask_direction_interface1, mask_direction_interface2 = ftdi3.get_input_output_from_request(request.form)
            ftdi3.set_direction_2(bitmask_i1=mask_direction_interface1, bitmask_i2=mask_direction_interface2)
        elif int(num) == 4:
            mask_direction_interface1, mask_direction_interface2 = ftdi4.get_input_output_from_request(request.form)
            ftdi4.set_direction_2(bitmask_i1=mask_direction_interface1, bitmask_i2=mask_direction_interface2)
        url = '.gui/FTDI{}'.format(str(num))
        return redirect(url_for('gui', num=num))
    return render_template('setup.html', ftdi=num)



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
        ftdi = json_data.get("FTDI")
        gpio = json_data.get("GPIO")
        if int(ftdi) == 0:
            out_state = ftdi0.map_string_to_gpio[gpio]['GPIO']['output_state']
        elif int(ftdi) == 1:
            out_state = ftdi1.map_string_to_gpio[gpio]['GPIO']['output_state']
        elif int(ftdi) == 2:
            out_state = ftdi2.map_string_to_gpio[gpio]['GPIO']['output_state']
        elif int(ftdi) == 3:
            out_state = ftdi3.map_string_to_gpio[gpio]['GPIO']['output_state']
        elif int(ftdi) == 4:
            out_state = ftdi4.map_string_to_gpio[gpio]['GPIO']['output_state']


        if (out_state):
            if int(ftdi) == 0:
                ftdi0.write_GPIO_LOW(gpio=gpio)
            elif int(ftdi) == 1:
                ftdi1.write_GPIO_LOW(gpio=gpio)
            elif int(ftdi) == 2:
                ftdi2.write_GPIO_LOW(gpio=gpio)
            elif int(ftdi) == 3:
                ftdi3.write_GPIO_LOW(gpio=gpio)
            elif int(ftdi) == 4:
                ftdi4.write_GPIO_LOW(gpio=gpio)
        else:
            if int(ftdi) == 0:
                ftdi0.write_GPIO_HIGH(gpio=gpio)
            elif int(ftdi) == 1:
                ftdi1.write_GPIO_HIGH(gpio=gpio)
            elif int(ftdi) == 2:
                ftdi2.write_GPIO_HIGH(gpio=gpio)
            elif int(ftdi) == 3:
                ftdi3.write_GPIO_HIGH(gpio=gpio)
            elif int(ftdi) == 4:
                ftdi4.write_GPIO_HIGH(gpio=gpio)

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
        ftdi = json_data.get("FTDI")
        gpio = json_data.get('GPIO')
        state = json_data.get('state')
        if int(state) == 1:
            if int(ftdi) == 0:
                ftdi0.write_GPIO_HIGH(gpio=gpio)
            elif int(ftdi) == 1:
                ftdi1.write_GPIO_HIGH(gpio=gpio)
            elif int(ftdi) == 2:
                ftdi2.write_GPIO_HIGH(gpio=gpio)
            elif int(ftdi) == 3:
                ftdi3.write_GPIO_HIGH(gpio=gpio)
            elif int(ftdi) == 4:
                ftdi4.write_GPIO_HIGH(gpio=gpio)
        else:
            if int(ftdi) == 0:
                ftdi0.write_GPIO_LOW(gpio=gpio)
            elif int(ftdi) == 1:
                ftdi1.write_GPIO_LOW(gpio=gpio)
            elif int(ftdi) == 2:
                ftdi2.write_GPIO_LOW(gpio=gpio)
            elif int(ftdi) == 3:
                ftdi3.write_GPIO_LOW(gpio=gpio)
            elif int(ftdi) == 4:
                ftdi4.write_GPIO_LOW(gpio=gpio)
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
        ftdi = json_data.get('FTDI')
        gpio = json_data.get('GPIO')
        direction = json_data.get('direction')
        state = json_data.get('state')
        if int(ftdi) == 0:
            ftdi0.set_gpio_direction(gpio=gpio, direction=direction, state=state)
        elif int(ftdi) == 1:
            ftdi1.set_gpio_direction(gpio=gpio, direction=direction, state=state)
        elif int(ftdi) == 2:
            ftdi2.set_gpio_direction(gpio=gpio, direction=direction, state=state)
        elif int(ftdi) == 3:
            ftdi3.set_gpio_direction(gpio=gpio, direction=direction, state=state)
        elif int(ftdi) == 4:
            ftdi4.set_gpio_direction(gpio=gpio, direction=direction, state=state)
        return jsonify({'FTDI': ftdi ,'GPIO':gpio, 'direction': direction})

@app.route('/gui/<num>', methods=['POST','GET'])
def gui(num):
    """GUI which provides control over the state of output GPIOs and shows the state of input and output GPIOs.
    Accessed over Webrowser on URL http://127.0.0.1:5000/gui

    :return: Rendered HTML page
    """
    if int(num) == 0:
        return render_template('gui2.html', io_array=ftdi0.get_direction_array(), color=ftdi0.getColor(), ftdi=num)
    elif int(num) == 1:
        return render_template('gui2.html', io_array=ftdi1.get_direction_array(), color=ftdi1.getColor(), ftdi=num)
    elif int(num) == 2:
        return render_template('gui2.html', io_array=ftdi2.get_direction_array(), color=ftdi2.getColor(), ftdi=num)
    elif int(num) == 3:
        return render_template('gui2.html', io_array=ftdi3.get_direction_array(), color=ftdi3.getColor(), ftdi=num)
    elif int(num) == 4:
        return render_template('gui2.html', io_array=ftdi4.get_direction_array(), color=ftdi4.getColor(), ftdi=num)


@app.route('/getColorJSON/<num>', methods=['GET'])
def getColorJSON(num):
    """Returns state colors of GPIO (green: HIGH, silver: LOW) used by polling JavaScript which keeps the GUI page updated.
    Accesed by GET-Request to URL http://127.0.0.1:5000/getColorJSON.

    :return: JSON Data
    """
    if int(num) == 0:
        colors = ftdi0.getColor()
    elif int(num) == 1:
        colors = ftdi1.getColor()
    elif int(num) == 2:
        colors = ftdi2.getColor()
    elif int(num) == 3:
        colors = ftdi3.getColor()
    elif int(num) == 4:
        colors = ftdi4.getColor()

    return jsonify(colors)

@app.route('/getIOJSON/<num>', methods=['GET'])
def getIOJSON(num):
    """Returns direction state of GPIO (input, output) used by polling JavaScript which keeps the GUI page updated.
    Accesed by GET-Request to URL http://127.0.0.1:5000/getIOJSON.

    :return: JSON Data
    """
    if int(num) == 0:
        io_array = ftdi0.get_direction_array()
    elif int(num) == 1:
        io_array = ftdi1.get_direction_array()
    elif int(num) == 2:
        io_array = ftdi2.get_direction_array()
    elif int(num) == 3:
        io_array = ftdi3.get_direction_array()
    elif int(num) == 4:
        io_array = ftdi4.get_direction_array()
    return jsonify(io_array)

#@app.errorhandler(Exception)
#def handle_exception(e):
#    print(e)
#    print("so")
#    server.terminate()
#    server.join()
#    sys.exit()


def set_voltage(channel, voltage):
    inst.write(':INST:NSEL {}'.format(str(channel)))
    #time.sleep(0.1)
    inst.write(':VOLT {}'.format(str(voltage)))

def channel_high(channel):
    inst.write(':OUTP CH{},1'.format(str(channel)))

def channel_low(channel):
    inst.write(':OUTP CH{},0'.format(str(channel)))

if __name__ == '__main__':
    #ftdi0 = FTDI2232H(url='ftdi://ftdi:2232:FT46S3T7/1')
    try:
        ftdi0 = FTDI2232H(url='ftdi://ftdi:2232:FTWWP6IJ/1')
    except Exception as e:
        print(e)
    try:
        ftdi1 = FTDI2232H(url='andere URL')
    except Exception as e:
        print(e)
    try:
        ftdi2 = FTDI2232H(url='andere URL')
    except Exception as e:
        print(e)
    try:
        ftdi3 = FTDI2232H(url='andere URL')
    except Exception as e:
        print(e)
    try:
        ftdi4 = FTDI2232H(url='andere URL')
    except Exception as e:
        print(e)
    try:
        rm = pyvisa.ResourceManager()
        inst = rm.open_resource('USB0::0x1AB1::0x0E11::DP8B205101806::INSTR')
        set_voltage(1, 24)
        channel_high(1)
    except Exception as e:
        print(e)

    #server = Process(target=app.run())
    #server.start()
    app.run()


#usb.dst==3.255.2 || usb.dst==3.255.4