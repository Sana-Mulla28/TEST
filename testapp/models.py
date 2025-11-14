from django.db import models
from django.core.exceptions import ValidationError
from testapp.descriptors import StringValidator, AgeValidator

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def clean(self):
        """
        Override Django's built-in clean() method to include our
        descriptor-based validation logic.
        """
        # Create descriptor instances and manually trigger their validation
        name_validator = StringValidator("name")
        age_validator = AgeValidator("age")

        try:
            name_validator.__set__(self, self.name) 
            age_validator.__set__(self, self.age)
        except ValueError as e:
            raise ValidationError(str(e))

    def __str__(self):
        return f"{self.name} ({self.age})"
