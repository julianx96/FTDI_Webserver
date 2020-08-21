# FTDI_Webserver

** Version 0.1 **

Requirements
---
This project uses Python3.
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
The server can be setup page for the FTDI Module can be reached by the URL http:127.0.0.1:5000/setup

By clicking the Apply Button you will get redirectet to the GUI control page
