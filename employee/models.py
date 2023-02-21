from django.db import models


# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=20)
    efamily = models.CharField(max_length=30)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=11)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.ename + ' ' + self.efamily
