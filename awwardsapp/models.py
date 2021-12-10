from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=300,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact=models.CharField(max_length=100,null=True)


    
    def save_profile(self):
        self.save()

    def update_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    def _str_(self):
        return self.user.username     
