from pyftdi.gpio import GpioMpsseController
from pyftdi.ftdi import FtdiError, USBError
from sys import exit

class FTDI2232H():
    """Class for FT2232H Mini Module
    """
    def __init__(self, url):
        """Initializes the FTDI Modul

        :param url: url that specifies the FTDI
        """
        self.url = url
        if self.url.split(':')[2] == '2232':

            self.AD0 = {
                'register': 0x0001,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'AD',
                    'Pin': 0,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.AD1 = {
                'register': 0x0002,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'AD',
                    'Pin': 1,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.AD2 = {
                'register': 0x0004,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'AD',
                    'Pin': 2,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.AD3 = {
                'register': 0x0008,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'AD',
                    'Pin': 3,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.AD4 = {
                'register': 0x0010,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'AD',
                    'Pin': 4,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.AD5 = {
                'register': 0x0020,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'AD',
                    'Pin': 5,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.AD6 = {
                'register': 0x0040,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'AD',
                    'Pin': 6,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.AD7 = {
                'register': 0x0080,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'AD',
                    'Pin': 7,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.AC0 = {
                'register': 0x0100,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'AC',
                    'Pin': 0,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.AC1 = {
                'register': 0x0200,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'AC',
                    'Pin': 1,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.AC2 = {
                'register': 0x0400,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'AC',
                    'Pin': 2,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.AC3 = {
                'register': 0x0800,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'AC',
                    'Pin': 3,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.AC4 = {
                'register': 0x1000,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'AC',
                    'Pin': 4,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.AC5 = {
                'register': 0x2000,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'AC',
                    'Pin': 5,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.AC6 = {
                'register': 0x4000,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'AC',
                    'Pin': 6,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.AC7 = {
                'register': 0x8000,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'AC',
                    'Pin': 7,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }


            self.BD0 = {
                'register': 0x0001,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'BD',
                    'Pin': 0,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.BD1 = {
                'register': 0x0002,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'BD',
                    'Pin': 1,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.BD2 = {
                'register': 0x0004,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'BD',
                    'Pin': 2,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.BD3 = {
                'register': 0x0008,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'BD',
                    'Pin': 3,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.BD4 = {
                'register': 0x0010,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'BD',
                    'Pin': 4,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.BD5 = {
                'register': 0x0020,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'BD',
                    'Pin': 5,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.BD6 = {
                'register': 0x0040,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'BD',
                    'Pin': 6,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.BD7 = {
                'register': 0x0080,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'BD',
                    'Pin': 7,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.BC0 = {
                'register': 0x0100,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'BC',
                    'Pin': 0,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.BC1 = {
                'register': 0x0200,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'BC',
                    'Pin': 1,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.BC2 = {
                'register': 0x0400,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'BC',
                    'Pin': 2,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.BC3 = {
                'register': 0x0800,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'BC',
                    'Pin': 3,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.BC4 = {
                'register': 0x1000,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'BC',
                    'Pin': 4,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.BC5 = {
                'register': 0x2000,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'BC',
                    'Pin': 5,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.BC6 = {
                'register': 0x4000,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'BC',
                    'Pin': 6,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }
            self.BC7 = {
                'register': 0x8000,
                'direction': 0x0000,
                'GPIO': {
                    'Port': 'BC',
                    'Pin': 7,
                    'output_state': 0,
                    'input_state': 0
                },
                'name': ''
            }

            self.gpio_array_interface1 = [self.AD0, self.AD1, self.AD2, self.AD3, self.AD4, self.AD5, self.AD6, self.AD7,
                                          self.AC0, self.AC1, self.AC2, self.AC3, self.AC4, self.AC5, self.AC6, self.AC7]

            self.gpio_array_interface2 = [self.BD0, self.BD1, self.BD2, self.BD3, self.BD4, self.BD5, self.BD6, self.BD7,
                                          self.BC0, self.BC1, self.BC2, self.BC3, self.BC4, self.BC5, self.BC6, self.BC7]

            self.map_string_to_gpio = {'AD0': self.AD0, 'AD1': self.AD1, 'AD2': self.AD2, 'AD3': self.AD3,
                                       'AD4': self.AD4, 'AD5': self.AD5, 'AD6': self.AD6, 'AD7': self.AD7,
                                       'AC0': self.AC0, 'AC1': self.AC1, 'AC2': self.AC2, 'AC3': self.AC3,
                                       'AC4': self.AC4, 'AC5': self.AC5, 'AC6': self.AC6, 'AC7': self.AC7,
                                       'BD0': self.BD0, 'BD1': self.BD1, 'BD2': self.BD2, 'BD3': self.BD3,
                                       'BD4': self.BD4, 'BD5': self.BD5, 'BD6': self.BD6, 'BD7': self.BD7,
                                       'BC0': self.BC0, 'BC1': self.BC1, 'BC2': self.BC2, 'BC3': self.BC3,
                                       'BC4': self.BC4, 'BC5': self.BC5, 'BC6': self.BC6, 'BC7': self.BC7
                                       }

            self.bitmask_direction_interface1 = 0x0000
            self.bitmask_direction_interface2 = 0x0000
            self.bitmask_output_state_interface1 = 0x0000
            self.bitmask_output_state_interface2 = 0x0000
            self.module = '2232H'

            self.Interface1 = GpioMpsseController()
            self.Interface2 = GpioMpsseController()

            self.Interface1.configure(url='ftdi://ftdi:2232:FTWWP6IJ/1', direction=self.bitmask_direction_interface1, frequency=1000000)
            self.Interface2.configure(url='ftdi://ftdi:2232:FTWWP6IJ/2', direction=self.bitmask_direction_interface2, frequency=1000000)

            #print(self.Interface1.write(0x0000))


    def set_direction_2(self, bitmask_i1=None, bitmask_i2=None):
        """Sets the direction of the GPIOs. They can be either configured as Output or Input.

        :param bitmask_i1: Bitmask that specifies the direction of the GPIOs from Interface 1
        :param bitmask_i2: Bitmask that specifies the direction of the GPIOs from Interface 2
        :return:
        """
        if self.module == '2232H':
            if bitmask_i1 != None:
                self.bitmask_direction_interface1 = bitmask_i1
                self.Interface1.set_direction(pins=0xffff, direction=self.bitmask_direction_interface1)
                for i in range(16):
                    if self.bitmask_direction_interface1 & (1 << i) == (1 << i):
                        self.gpio_array_interface1[i]['direction'] = self.gpio_array_interface1[i]['register']
                        self.gpio_array_interface1[i]['GPIO']['input_state'] = None
                    else:
                        self.gpio_array_interface1[i]['direction'] = 0x0000
                        self.gpio_array_interface1[i]['GPIO']['output_state'] = None

            if bitmask_i2 != None:
                self.bitmask_direction_interface2 = bitmask_i2
                self.Interface2.set_direction(pins=0xffff, direction=self.bitmask_direction_interface2)
                for i in range(16):
                    if self.bitmask_direction_interface2 & (1 << i) == (1 << i):
                        self.gpio_array_interface2[i]['direction'] = self.gpio_array_interface2[i]['register']
                        self.gpio_array_interface2[i]['GPIO']['input_state'] = None
                    else:
                        self.gpio_array_interface2[i]['direction'] = 0x0000
                        self.gpio_array_interface2[i]['GPIO']['output_state'] = None



    def set_gpio_direction(self, gpio, direction):
        """Sets the direction of one GPIO. The GPIO can be either configured as Input or Output.lol

        :param gpio: GPIO whose direction will be changed
        :param direction: Direction, either Input or Output
        :return:
        """
        pin = self.map_string_to_gpio[gpio]
        if gpio[0] == 'A':
            if direction == 'output':
                self.bitmask_direction_interface1 |= pin['register']
            else:
                self.bitmask_direction_interface1 &= ~pin['register']
            self.set_direction_2(bitmask_i1=self.bitmask_direction_interface1)
        if gpio[0] == 'B':
            if direction == 'output':
                self.bitmask_direction_interface2 |= pin['register']
            else:
                self.bitmask_direction_interface2 &= ~pin['register']
            self.set_direction_2(bitmask_i2=self.bitmask_direction_interface2)

    def read_input_gpio(self):
        """Reads the state on the Input GPIOs and writes them to the Dictionary, containing the GPIOs informations.

        :return:
        """
        try:
            input1 = self.Interface1.read()
            #print(input1)
            input2 = self.Interface2.read()
            # Interface 1
        except (FtdiError, USBError):
            self.reconnect()

        for i in range(16):
            if(int(input1[0]) & (1 << i)) == (1 << i):
                self.gpio_array_interface1[i]['GPIO']['input_state'] = 1
            elif self.gpio_array_interface1[i]['direction'] == 0x0000:
                self.gpio_array_interface1[i]['GPIO']['input_state'] = 0

        for i in range(16):
            if(int(input2[0]) & (1 << i)) == (1 << i):
                self.gpio_array_interface2[i]['GPIO']['input_state'] = 1
            elif self.gpio_array_interface2[i]['direction'] == 0x0000:
                self.gpio_array_interface2[i]['GPIO']['input_state'] = 0


    def set_output_state_gpio(self, gpio, state):
        """Writes one output GPIO to a specific state. Either HIGH or LOW

        :param gpio: GPIO whose Output will be configured
        :param state: State which will be applied to the GPIO
        :return:
        """
        pin = self.map_string_to_gpio[gpio]
        if gpio[0] == 'A':
            if pin['direction'] != 0x0000:
                pin['GPIO']['output_state'] = int(state)
                if int(state) == 1:
                    self.bitmask_output_state_interface1 |= pin['register']
                else:
                    self.bitmask_output_state_interface1 &= ~pin['register']
        if gpio[0] == 'B':
            if pin['direction'] != 0x0000:
                pin['GPIO']['output_state'] = int(state)
                if int(state) == 1:
                    self.bitmask_output_state_interface2 |= pin['register']
                else:
                    self.bitmask_output_state_interface2 &= ~pin['register']

    def write_GPIO_HIGH(self, gpio):
        """Writes an output GPIO High
        Configures the JSON Data containing the GPIO informations.

        :param gpio: GPIO whose Ouput will be set High
        :return:
        """
        if gpio[0] == 'A':
            self.bitmask_output_state_interface1 |= self.map_string_to_gpio[gpio]['direction']
        elif gpio[0] == 'B':
            self.bitmask_output_state_interface2 |= self.map_string_to_gpio[gpio]['direction']
        self.map_string_to_gpio[gpio]['GPIO']['output_state'] = 1
        self.write_output()

    def write_GPIO_LOW(self, gpio):
        """Writes an output GPIO Low
        Configures the JSON Data containing the GPIO informations.

        :param gpio:
        :return:
        """
        if gpio[0] == 'A':
            self.bitmask_output_state_interface1 &= ~self.map_string_to_gpio[gpio]['direction']
        elif gpio[0] == 'B':
            self.bitmask_output_state_interface2 &= ~self.map_string_to_gpio[gpio]['direction']
        self.map_string_to_gpio[gpio]['GPIO']['output_state'] = 0
        self.write_output()

    def write_output(self):
        """Writes all GPIO outputs, according to the Bitmasks

        :return:
        """
        self.Interface1.write(self.bitmask_output_state_interface1)
        self.Interface2.write(self.bitmask_output_state_interface2)


    def getColor(self):
        colors = {}
        self.read_input_gpio()
        for i in range(16):
            if self.gpio_array_interface1[i]['direction'] != 0:
                if self.gpio_array_interface1[i]['GPIO']['output_state'] == 1:
                    colors[i] = 'green'
                else:
                    colors[i] = 'silver'
            else:
                if self.gpio_array_interface1[i]['GPIO']['input_state'] == 1:
                    colors[i] = 'green'
                else:
                    colors[i] = 'silver'
        for i in range(16):
            if self.gpio_array_interface2[i]['direction'] != 0:
                if self.gpio_array_interface2[i]['GPIO']['output_state'] == 1:
                    colors[16+i] = 'green'
                else:
                    colors[16+i] = 'silver'
            else:
                if self.gpio_array_interface2[i]['GPIO']['input_state'] == 1:
                    colors[16+i] = 'green'
                else:
                    colors[16+i] = 'silver'
        return colors

    def get_direction_array(self):
        io_array = {}
        for i in range(16):
            direction = self.gpio_array_interface1[i]['direction']
            if direction != 0x0000:
                #io_array.append('output')
                io_array[i] = 'output'
            else:
                #io_array.append('input')
                io_array[i] = 'input'
        for i in range(16):
            direction = self.gpio_array_interface2[i]['direction']
            if direction != 0x0000:
                #io_array.append('output')
                io_array[16+i] = 'output'
            else:
                #io_array.append('input')
                io_array[16+i] = 'input'
        return io_array

    def get_input_output_from_request(self, request):
        interface1_IO_array = []
        interface2_IO_array = []

        interface1_IO_bitmask = 0x0000
        interface2_IO_bitmask = 0x0000

        interface1_IO_array.append(request['AD0_out_in'])
        interface1_IO_array.append(request['AD1_out_in'])
        interface1_IO_array.append(request['AD2_out_in'])
        interface1_IO_array.append(request['AD3_out_in'])
        interface1_IO_array.append(request['AD4_out_in'])
        interface1_IO_array.append(request['AD5_out_in'])
        interface1_IO_array.append(request['AD6_out_in'])
        interface1_IO_array.append(request['AD7_out_in'])
        interface1_IO_array.append(request['AC0_out_in'])
        interface1_IO_array.append(request['AC1_out_in'])
        interface1_IO_array.append(request['AC2_out_in'])
        interface1_IO_array.append(request['AC3_out_in'])
        interface1_IO_array.append(request['AC4_out_in'])
        interface1_IO_array.append(request['AC5_out_in'])
        interface1_IO_array.append(request['AC6_out_in'])
        interface1_IO_array.append(request['AC7_out_in'])

        interface2_IO_array.append(request['BD0_out_in'])
        interface2_IO_array.append(request['BD1_out_in'])
        interface2_IO_array.append(request['BD2_out_in'])
        interface2_IO_array.append(request['BD3_out_in'])
        interface2_IO_array.append(request['BD4_out_in'])
        interface2_IO_array.append(request['BD5_out_in'])
        interface2_IO_array.append(request['BD6_out_in'])
        interface2_IO_array.append(request['BD7_out_in'])
        interface2_IO_array.append(request['BC0_out_in'])
        interface2_IO_array.append(request['BC1_out_in'])
        interface2_IO_array.append(request['BC2_out_in'])
        interface2_IO_array.append(request['BC3_out_in'])
        interface2_IO_array.append(request['BC4_out_in'])
        interface2_IO_array.append(request['BC5_out_in'])
        interface2_IO_array.append(request['BC6_out_in'])
        interface2_IO_array.append(request['BC7_out_in'])

        for i in range(16):
            if interface1_IO_array[i] == 'output':
                interface1_IO_bitmask |= 1 << i
            if interface2_IO_array[i] == 'output':
                interface2_IO_bitmask |= 1 << i
        return interface1_IO_bitmask, interface2_IO_bitmask

    def reconnect(self):
        print('hm')
