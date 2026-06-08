class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if value < 1:
            raise ValueError("Number must be positive")
        self._number = value


def main():
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Charlie", weight=5),
    ]
    for package in packages:
        print(
            f"{package.number}: {package.sender} to {package.recipient}, {package.weight}kg"
        )


main()
