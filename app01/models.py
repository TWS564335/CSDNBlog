from django.db import models

# Create your models here.

class Book(models.Model):
    nid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=32,unique=True)
    price=models.DecimalField(max_digits=8,decimal_places=2,null=True)# 999999.99
    pub_date=models.DateField()
    publish=models.CharField(max_length=32)
    is_pub=models.BooleanField(default=True)

    def __str__(self):
        return self.title
