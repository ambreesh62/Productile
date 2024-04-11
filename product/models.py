from django.db import models
from base.models import BaseModel


class Product(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(("Name"), max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="Product_image/", blank=True, null=True)
    category_id = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.name},{self.price}"


class Category(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(("Name"), max_length=50)

    def __str__(self) -> str:
        return self.name
