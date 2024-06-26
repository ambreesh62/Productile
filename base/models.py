from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(("created_at"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(("updated_at"), auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
