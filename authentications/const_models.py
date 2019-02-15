from django.db import models
from datetime import datetime



# class BaseModel(models.Model):

#     name = models.CharField(max_length=50,null=True,blank=True)

#     created_at= models.DateTimeField(auto_now_add=True)

#     class Meta:
#         abstract = True

#     # def __str__(self): 
#     #     return str(self.id)



class Country(models.Model):
    id = models.CharField(primary_key=True, max_length=3)
    name = models.CharField(max_length=50,null=True,blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
 
    class Meta:
        db_table = 'country'

    def __str__(self): 
        return str(self.name)


class State(models.Model):
    id = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=50,null=True,blank=True)
    country = models.ForeignKey('authentications.Country', on_delete=models.CASCADE, blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    # country_id =  models.CharField(max_length=3,null=True,blank=True)
 
    class Meta:
        db_table = 'state'

    def __str__(self): 
        return str(self.name)


class LocalArea(models.Model):
    id = models.CharField(primary_key=True, max_length=3)
    name = models.CharField(max_length=50,null=True,blank=True)
    state = models.ForeignKey('authentications.State', on_delete=models.CASCADE, blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    # state_id =  models.CharField(max_length=4, null=True, blank=True)
 
    class Meta:
        db_table = 'localarea'

    def __str__(self): 
        return str(self.name)





