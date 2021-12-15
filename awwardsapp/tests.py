from django.test import TestCase
from django.contrib.auth.models import User
from .models import  Profile,Project

# Create your tests here.
class ProjectTestClass(TestCase):
  def setUp(self):
        user = User.objects.create(username="test_user")
        self.project = Project(title="Test Title",image="image.url",description="Test Project description",link="https://kips-alih.github.io/Quotes-App/",user=user)

  def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

  def test_save_project(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

class ProfileTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(username="test_user")
        self.profile = Profile(profile_pic="",bio="Test Profile_pic",user=user,contact="My contact")

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_update_profile(self):
        self.profile.update_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

