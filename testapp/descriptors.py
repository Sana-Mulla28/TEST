class StringValidator:
    """Descriptor to ensure non-empty string value."""
    def __init__(self, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.name[1:]} must be a string.")
        if not value.strip():
            raise ValueError(f"{self.name[1:]} cannot be empty.")
        setattr(instance, self.name, value)


class AgeValidator:
    """Descriptor to ensure age is between 18 and 100."""
    def __init__(self, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Age must be an integer.")
        if not (18 <= value <= 100):
            raise ValueError("Age must be between 18 and 100.")
        setattr(instance, self.name, value)
