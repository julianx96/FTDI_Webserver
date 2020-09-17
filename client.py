"""
This python script contains examples for using the REST API as client
"""

import requests

def setGPIODirection(GPIO, direction):
	"""
	:param GPIO: string - GPIO to be changed (e.g. 'AD0')
	:param direction: string - new direction (eather 'output' or 'input')
	"""
	requests.post('http://127.0.0.1:5000/setGPIODirection', json={'GPIO':GPIO, 'direction':direction})
	
	
def writeGPIO(GPIO, state):
	"""
	:param GPIO: string - GPIO to be changed (e.g. 'AD0')
	:param state: int - new state (eather 0 or 1)
	"""
	requests.post('http://127.0.0.1:5000/writeGPIO', json={'GPIO':GPIO, 'state':state})

	
def readGPIO(GPIO):
	"""
	:param GPIO: string - GPIO to be changed (e.g. 'AD0')
	:return: int - state
	"""
	r = requests.get('http://127.0.0.1:5000/readGPIO', json={'GPIO':GPIO})
	return r.json()['state']
	
#setGPIODirection('AD2', 'input')
#writeGPIO('AD0', 0)
#writeGPIO('AD0', 0)
#setGPIODirection('AC4', 'input')
#print(readGPIO('AC2'))
