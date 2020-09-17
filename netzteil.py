import pyvisa
import time

rm = pyvisa.ResourceManager()
print(rm.list_resources())
inst = rm.open_resource('USB0::0x1AB1::0x0E11::DP8B205101806::INSTR')
print(inst.query("*IDN?"))

def set_voltage(channel, voltage):
    inst.write(':INST:NSEL {}'.format(str(channel)))
    #time.sleep(0.1)
    inst.write(':VOLT {}'.format(str(voltage)))

def channel_high(channel):
    inst.write(':OUTP CH{},1'.format(str(channel)))

def channel_low(channel):
    inst.write(':OUTP CH{},0'.format(str(channel)))

