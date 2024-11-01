from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(null=True, blank=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    air_conditioning = models.BooleanField(default=False)
    power_steering = models.BooleanField(default=False)
    electric_windows = models.BooleanField(default=False)
    trunk_electric = models.BooleanField(default=False)
    number_of_doors = models.IntegerField(choices=[(2, '2 portas'), (3, '3 portas'), (4, '4 portas')], default=4)
    transmission = models.CharField(max_length=10, choices=[('Manual', 'Manual'), ('Automático', 'Automático')], default='Manual')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model


class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'