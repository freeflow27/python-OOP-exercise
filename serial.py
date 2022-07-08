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

    def __init__(self, start=0):
        """creates new generator, starting at 0, or input number"""
        self.start = self.next = start

    def __repr__(self):
        return f"SerialGenerator {self.start} will be {self.next} next"

    def generate(self):
        """adds the enxt number, but returns the previous number"""
        self.next += 1
        return self.next -1

    def reset(self):
        "resets the generator"
        self.next = self.start