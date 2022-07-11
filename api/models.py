from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Employer(MPTTModel):
  full_name = models.CharField(max_length=200)
  job_title = models.CharField(max_length=200)
  start_date = models.DateField(auto_now_add=True)
  salary = models.DecimalField(decimal_places=2, max_digits=10)
  parent = TreeForeignKey(
    'self', 
    blank=True, 
    null=True, 
    on_delete=models.CASCADE,
    related_name="children"
    )

      
  def __str__(self):
    return self.job_title