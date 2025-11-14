from decimal import Decimal, InvalidOperation


class Positive:
    """Descriptor that ensures assigned value is positive decimal."""
    
    def __init__(self, name):
        self.name = name  # attribute name in instance.__dict__

    def __get__(self, instance, owner):
        if instance is None:
            return self  # Accessed via class, return descriptor itself
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value is None:
            instance.__dict__[self.name] = None
            return
        
        try:
            dec = Decimal(value)
        except (InvalidOperation, TypeError, ValueError):
            raise ValueError(f"{self.name} must be numeric.")
        
        if dec <= 0:
            raise ValueError(f"{self.name} must be positive.")
        
        instance.__dict__[self.name] = dec


class ProductPlain:
    """A simple product class using descriptor for price validation."""
    
    price = Positive('price')

    def __init__(self, price=None):
        if price is not None:
            self.price = price


def main():
    print("=== Testing Descriptor Validation ===")
    
    p = ProductPlain()
    
    # Valid assignment
    try:
        p.price = '12.50'
        print("✅ Price set to:", p.price)
    except ValueError as e:
        print("❌", e)

    # Invalid assignment (negative value)
    try:
        p.price = -1
    except ValueError as e:
        print("❌", e)

    # Invalid assignment (non-numeric value)
    try:
        p.price = "abc"
    except ValueError as e:
        print("❌", e)


if __name__ == "__main__":
    main()
