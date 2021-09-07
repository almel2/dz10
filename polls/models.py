from django.db import models


class City(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.title


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    product = models.ManyToManyField('Product')
    city = models.ForeignKey("City", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Product(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.price}$'


class Provider(models.Model):
    title = models.CharField(max_length=50)
    city = models.OneToOneField("City", on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.title
