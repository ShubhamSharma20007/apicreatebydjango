from django.db import models
# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=52)
    location =  models.CharField(max_length=52)
    about = models.TextField()
    type = models.CharField(max_length=102,choices=
                            (('IT',"IT"),
                             ('None IT' ,'Non IT'),
                             ('Mobile Phone', 'Mobile Phone')))
    added = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name