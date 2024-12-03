from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# CarMake model
class CarMake(models.Model):
    name = models.CharField(max_length=100)  # Name of the car make
    description = models.TextField()  # Description of the car make
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)  # Optional field for country of origin

    def __str__(self):
        return self.name  # String representation of the car make


# CarModel model
class CarModel(models.Model):
    # Choices for car type
    CAR_TYPE_CHOICES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
    ]

    name = models.CharField(max_length=100)  # Name of the car model
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-one relationship with CarMake
    car_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES)  # Type of the car
    year = models.IntegerField(
        validators=[MinValueValidator(2015), MaxValueValidator(2023)]  # Year validation
    )
    dealer_id = models.IntegerField()  # ID of the dealer (optional field for dealer reference)

    def __str__(self):
        return f"{self.car_make.name} {self.name}"  # String representation of the car model
