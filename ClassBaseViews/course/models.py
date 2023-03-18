from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=200)
    describe=models.CharField(max_length=500)
    ratings=models.IntegerField()
    
    def __str__(self) -> str:
        return self.name+""+self.describe+""+self.ratings
