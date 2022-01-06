"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 100, default = 100):
        """Make new variable equal to start that will serve as the counter for incrementation"""
        self.start = self.increment = start
        self.default = default

    def __repr__(self):
        """Representation"""

        return f"<SerialGenerator start={self.start} increment={self.increment} default={self.default}>"


    def generate(self):
        """This function increments value by 1 to the current serial number"""
        self.increment += 1
        return self.increment - 1

    def reset(self):
        """Reset serial back to default number"""
        self.default

