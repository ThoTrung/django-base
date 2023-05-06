from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    class Meta:
        abstract=True
class CustomerManager(BaseModel):
    customer_code = models.CharField(max_length=50, unique=True, blank=False)
    customer_name = models.CharField(max_length=255, blank=False)
    customer_email = models.EmailField(max_length=255, unique=True, blank=False)
    customer_expose = models.CharField(max_length=255, blank=False)
    customer_style = models.TextField(blank=False)
    customer_description = models.TextField(blank=False)
    customer_namepay = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.customer_name
