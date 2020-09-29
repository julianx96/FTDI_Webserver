# FTDI_Webserver

** Version 0.1 **

Requirements
---
This project uses Python3.5 or higher.
The required Hardware is a FT2232H Mini Module, which requires a python module named pyftdi. 
To install required moduls you can run the following command in your shell:
```
pip3 install -r requirements.txt
```
For further requirements of the FTDI modul see https://eblot.github.io/pyftdi/installation.html

Configure Code
---
Open your python shell and run the following commands
```
from pyftdi.ftdi import Ftdi
print(Ftdi.show_devices())
```
This should return two interfaces. Each has an URL. Use one of them and replace it with the URL in line 138 in main.py
Now you can run the webserver with 
```
python3 main.py
```

Server
---
The server setup page for the FTDI Module can be reached by the URL http:127.0.0.1:5000/setup/<number of FTDI>
The parameter <number of FTDI> can be 0, 1, 2, 3 or 4, depending on which FT2232H Mini Module you want to configure/control.
 
By clicking the Apply Button you will get redirectet to the GUI control page or you can access it by the URL http:127.0.0.1:5000/gui/<number of FTDI>

The laboratory power supply will be automatically set to 24V on channel 1. It gets initialized with the following command:
```
inst = rm.open_resource('USB0::0x1AB1::0x0E11::DP8B205101806::INSTR')
```

Maybe you have to change the String in the brackets. To find out what string you have to use you can get it that way:
```
import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())
```
This should return the string. To verify do:
```
import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())
inst = rm.open_resource('<string from print command>')
print(inst.query("*IDN?"))
```

