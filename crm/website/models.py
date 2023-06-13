from django.db import models

'''
Pas besoin de savoir faire du sql,
Django converti automatiquement 
les valeurs en SQL.
Il faut créer une migration et 
pousser cette migration dans la BDD.
'''
class Record(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone =  models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state =  models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    
    #show on the screen if we just access one of this record
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    
