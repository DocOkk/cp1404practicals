"""Represent a programming language."""


class ProgrammingLanguage:
    """Store information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Initialise a programming language."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        """Return the language's details."""
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, "
                f"First appeared in {self.year}, "
                f"Pointer Arithmetic={self.pointer_arithmetic}")

    def is_dynamic(self):
        """Determine whether the language is dynamically typed."""
        return self.typing == "Dynamic"
