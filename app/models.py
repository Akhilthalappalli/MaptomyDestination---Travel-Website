from django.db import models

# Create your models here.

class State(models.Model):
    description = models.CharField(max_length=40,unique=True)

    def __str__(self):
        return self.description

class District(models.Model):
    description = models.CharField(max_length=40,unique=True)    

    def __str__(self):
        return self.description

class Season(models.Model):
    description = models.CharField(max_length=40,unique=True)    

    def __str__(self):
        return self.description

class Place_type(models.Model):
    description = models.CharField(max_length=40,unique=True)    

    def __str__(self):
        return self.description


class Place(models.Model):
    # placeid = models.CharField(max_length=10,unique=True)
	# img = models.ImageField(null=True)
	# name = models.CharField(max_length=20)
    district = models.ForeignKey(District,on_delete=models.CASCADE,null=True, blank=True)
    state = models.ForeignKey(State,on_delete=models.CASCADE,)
    map = models.CharField(max_length=1000)
    description = models.CharField(max_length=1500)
    place_name = models.CharField(max_length=100)
    place_link = models.CharField(max_length=1000)
    season = models.ForeignKey(Season,on_delete=models.CASCADE, null=True, blank=True)
    place_type = models.ForeignKey(Place_type,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.place_name


class Top_list(models.Model):
    number = models.CharField(max_length=100)
    t_list = models.CharField(max_length=100)
    district = models.ForeignKey(District,on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(State,on_delete=models.CASCADE,)
    t_description = models.CharField(max_length=1500)
    t_link = models.CharField(max_length=1000)
    t_map = models.CharField(max_length=1000)

