from djongo import models

# Create your models here.
class Product(models.Model):
    idProduct = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
    class Meta:
        abstract = True

class Bill(models.Model):
    idCliente =models.CharField(max_length=300)
    idBill = models.IntegerField(primary_key=True, auto_created=True)
    total = models.FloatField()
    date = models.DateTimeField()
    user = models.CharField(max_length=100)
    state= models.CharField(max_length=50, default='Pendiente')
   # products = models.IntegerField()
    products = models.ArrayField(
        model_container=Product
    )
    def __str__(self):
        return self.name