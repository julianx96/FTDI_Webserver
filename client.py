"""
This python script contains examples for using the REST API as client
"""

import requests

def setGPIODirection(FTDI, GPIO, direction, state=0):
	"""
	:param GPIO: string - GPIO to be changed (e.g. 'AD0')
	:param direction: string - new direction (eather 'output' or 'input')
	"""
	requests.post('http://127.0.0.1:5000/setGPIODirection', json={'FTDI': FTDI ,'GPIO':GPIO, 'direction':direction, 'state': state})
	
	
def writeGPIO(FTDI, GPIO, state):
	"""
	:param GPIO: string - GPIO to be changed (e.g. 'AD0')
	:param state: int - new state (eather 0 or 1)
	"""
	requests.post('http://127.0.0.1:5000/writeGPIO', json={'FTDI': FTDI ,'GPIO':GPIO, 'state':state})

	
def readGPIO(FTDI, GPIO):
	"""
	:param GPIO: string - GPIO to be changed (e.g. 'AD0')
	:return: int - state
	"""
	r = requests.get('http://127.0.0.1:5000/readGPIO', json={'FTDI': FTDI ,'GPIO':GPIO})
	return r.json()['state']
	

def power_on(ftdi, board):
	if board == 0:
		gpio = 'AC0'
	elif board == 1:
		gpio = 'AD0'
	elif board == 2:
		gpio = 'BC0'
	elif board == 3:
		gpio = 'BD0'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='output', state=1)

def power_off(ftdi, board):
	if board == 0:
		gpio = 'AC0'
	elif board == 1:
		gpio = 'AD0'
	elif board == 2:
		gpio = 'BC0'
	elif board == 3:
		gpio = 'BD0'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='output', state=0)

def pio1_on(ftdi, board):
	if board == 0:
		gpio = 'AC1'
	elif board == 1:
		gpio = 'AD1'
	elif board == 2:
		gpio = 'BC1'
	elif board == 3:
		gpio = 'BD1'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='output', state=1)

def pio1_off(ftdi, board):
	if board == 0:
		gpio = 'AC1'
	elif board == 1:
		gpio = 'AD1'
	elif board == 2:
		gpio = 'BC1'
	elif board == 3:
		gpio = 'BD1'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='output', state=0)

def read_pio1(ftdi, board):
	if board == 0:
		gpio = 'AC1'
	elif board == 1:
		gpio = 'AD1'
	elif board == 2:
		gpio = 'BC1'
	elif board == 3:
		gpio = 'BD1'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='input')
	readGPIO(FTDI=ftdi, GPIO=gpio)


def pio2_on(ftdi, board):
	if board == 0:
		gpio = 'AC2'
	elif board == 1:
		gpio = 'AD2'
	elif board == 2:
		gpio = 'BC2'
	elif board == 3:
		gpio = 'BD2'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='output', state=1)


def pio2_off(ftdi, board):
	if board == 0:
		gpio = 'AC2'
	elif board == 1:
		gpio = 'AD2'
	elif board == 2:
		gpio = 'BC2'
	elif board == 3:
		gpio = 'BD2'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='output', state=0)


def read_pio2(ftdi, board):
	if board == 0:
		gpio = 'AC2'
	elif board == 1:
		gpio = 'AD2'
	elif board == 2:
		gpio = 'BC2'
	elif board == 3:
		gpio = 'BD2'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='input')
	readGPIO(FTDI=ftdi, GPIO=gpio)

def led_on(ftdi, board):
	if board == 0:
		gpio = 'AC3'
	elif board == 1:
		gpio = 'AD3'
	elif board == 2:
		gpio = 'BC3'
	elif board == 3:
		gpio = 'BD3'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='output', state=1)


def led_off(ftdi, board):
	if board == 0:
		gpio = 'AC3'
	elif board == 1:
		gpio = 'AD3'
	elif board == 2:
		gpio = 'BC3'
	elif board == 3:
		gpio = 'BD3'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='output', state=0)


def read_led(ftdi, board):
	if board == 0:
		gpio = 'AC3'
	elif board == 1:
		gpio = 'AD3'
	elif board == 2:
		gpio = 'BC3'
	elif board == 3:
		gpio = 'BD3'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='input')
	readGPIO(FTDI=ftdi, GPIO=gpio)

def rdy_on(ftdi, board):
	if board == 0:
		gpio = 'AC4'
	elif board == 1:
		gpio = 'AD4'
	elif board == 2:
		gpio = 'BC4'
	elif board == 3:
		gpio = 'BD4'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='output', state=1)


def rdy_off(ftdi, board):
	if board == 0:
		gpio = 'AC4'
	elif board == 1:
		gpio = 'AD4'
	elif board == 2:
		gpio = 'BC4'
	elif board == 3:
		gpio = 'BD4'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='output', state=0)


def read_rdy(ftdi, board):
	if board == 0:
		gpio = 'AC4'
	elif board == 1:
		gpio = 'AD4'
	elif board == 2:
		gpio = 'BC4'
	elif board == 3:
		gpio = 'BD4'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='input')
	readGPIO(FTDI=ftdi, GPIO=gpio)


def run_on(ftdi, board):
	if board == 0:
		gpio = 'AC5'
	elif board == 1:
		gpio = 'AD5'
	elif board == 2:
		gpio = 'BC5'
	elif board == 3:
		gpio = 'BD5'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='output', state=1)


def run_off(ftdi, board):
	if board == 0:
		gpio = 'AC5'
	elif board == 1:
		gpio = 'AD5'
	elif board == 2:
		gpio = 'BC5'
	elif board == 3:
		gpio = 'BD5'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='output', state=0)


def read_run(ftdi, board):
	if board == 0:
		gpio = 'AC5'
	elif board == 1:
		gpio = 'AD5'
	elif board == 2:
		gpio = 'BC5'
	elif board == 3:
		gpio = 'BD5'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='input')
	readGPIO(FTDI=ftdi, GPIO=gpio)


def reset_on(ftdi, board):
	if board == 0:
		gpio = 'AC6'
	elif board == 1:
		gpio = 'AD6'
	elif board == 2:
		gpio = 'BC6'
	elif board == 3:
		gpio = 'BD6'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='output', state=0)


def reset_off(ftdi, board):
	if board == 0:
		gpio = 'AC6'
	elif board == 1:
		gpio = 'AD6'
	elif board == 2:
		gpio = 'BC6'
	elif board == 3:
		gpio = 'BD6'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='output', state=1)


def usb_on(ftdi, board):
	if board == 0:
		gpio = 'AC7'
	elif board == 1:
		gpio = 'AD7'
	elif board == 2:
		gpio = 'BC7'
	elif board == 3:
		gpio = 'BD7'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='output', state=1)


def usb_off(ftdi, board):
	if board == 0:
		gpio = 'AC7'
	elif board == 1:
		gpio = 'AD7'
	elif board == 2:
		gpio = 'BC7'
	elif board == 3:
		gpio = 'BD7'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='output', state=0)


def usb_run(ftdi, board):
	if board == 0:
		gpio = 'AC7'
	elif board == 1:
		gpio = 'AD7'
	elif board == 2:
		gpio = 'BC7'
	elif board == 3:
		gpio = 'BD7'
	setGPIODirection(FTDI=ftdi, GPIO=gpio, direction='input')
	readGPIO(FTDI=ftdi, GPIO=gpio)
