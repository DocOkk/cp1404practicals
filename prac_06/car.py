"""Represent a car for the Practical 06 guided example."""


class Car:
    """Represent a car."""

    def __init__(self, name, fuel=0):
        """Initialise a car's name, fuel and odometer."""
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount):
        """Add fuel to the car."""
        self.fuel += amount
