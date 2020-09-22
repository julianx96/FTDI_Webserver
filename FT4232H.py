from pyftdi.gpio import GpioMpsseController

interface1 = GpioMpsseController()
interface2 = GpioMpsseController()
interface3 = GpioMpsseController()
interface4 = GpioMpsseController()

interface1.configure(url='ftdi://ftdi:4232:FT0QE0W4/1', direction=0x00, frequency=1000000)
interface2.configure(url='ftdi://ftdi:4232:FT0QE0W4/2', direction=0x00, frequency=1000000)
interface3.configure(url='ftdi://ftdi:4232:FT0QE0W4/3', direction=0x00, frequency=1000000)
interface4.configure(url='ftdi://ftdi:4232:FT0QE0W4/4', direction=0x00, frequency=1000000)


def _write(self, data: Union[bytes, bytearray]) -> int:
    if self._debug_log:
        try:
            self.log.debug('> %s', hexlify(data).decode())
        except TypeError as exc:
            self.log.warning('> (invalid output byte sequence: %s)', exc)
    if self._tracer:
        self._tracer.send(self._index, data)
    try:
        return self._usb_dev.write(self._in_ep, data,
                                   self._usb_write_timeout)
    except USBError as ex:
        raise FtdiError('UsbError: %s' % str(ex)) from None