from django.db import models

# Create your models here.
class Lion_Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now = True)
 
    def __str__(req):
        return req.title
    
class Ex_Post(models.Model):
    user = models.ForeignKey('auth.User' , on_delete=models.CASCADE) 
    title = models.CharField(max_length=500) 
    content = models.TextField() 
    create_time = models.DateTimeField(auto_now_add=True) 
    updated_time = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.title