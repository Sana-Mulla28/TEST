 testapp/descriptors.py

class StringValidator:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        # keep validation logic strict and raise ValueError on invalid input
        if not isinstance(value, str):
            raise ValueError(f"{self.name} must be a string")
        if value.strip() == "":
            raise ValueError(f"{self.name} cannot be empty")
        instance.__dict__[self.name] = value


class AgeValidator:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be a positive integer")
        instance.__dict__[self.name] = value
