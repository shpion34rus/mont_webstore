from django.db import models


# Create your models here.
class Offer(models.Model):
    offer_id = models.IntegerField()
    available = models.BooleanField()

    def __str__(self):
        return str(self.offer_id)


class Category(models.Model):
    category_id = models.IntegerField()
    parent_id = models.IntegerField()


class OfferDetail(models.Model):
    offer_id = models.ForeignKey(Offer, on_delete=models.CASCADE)
    price = models.FloatField()
    currency_id = models.CharField(max_length=10)
    category_id = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)
    picture = models.TextField()
    delivery = models.BooleanField()
    vendor = models.TextField()
    model = models.TextField()
    description = models.TextField()


class OfferBarcode(models.Model):
    offer_id = models.ForeignKey(Offer, on_delete=models.CASCADE)
    barcode = models.TextField()


class OfferParams(models.Model):
    offer_id = models.ForeignKey(Offer, on_delete=models.CASCADE)
    available = models.TextField()
    MinRetailPrice = models.TextField()
    DeliveryDate = models.TextField()
    Multiplicity = models.TextField()
    DescrProductName = models.TextField()
    BrandId = models.TextField()
    ProductWeight = models.TextField()
    ProductVolume = models.TextField()
    ProductSales = models.TextField()
    ProductNew = models.TextField()
    RatingOrion = models.TextField()
    RatingCapital = models.TextField()
    DetailCharacteristics = models.TextField()
