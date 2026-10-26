"""Demonstrate independent Car objects."""

from prac_06.car import Car


def main():
    """Create two cars and add fuel to one."""
    limo = Car("Limo", 100)
    taxi = Car("Taxi", 40)
    limo.add_fuel(20)
    print(limo.fuel)
    print(taxi.fuel)


main()
