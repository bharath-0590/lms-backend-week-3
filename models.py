from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/')
    contact_info = models.CharField(max_length=255)

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    prerequisites = models.TextField()

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    module = models.ForeignKey(LearningModule, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()
    score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
class NotificationSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    receive_emails = models.BooleanField(default=True)
    receive_sms = models.BooleanField(default=False)
    receive_push_notifications = models.BooleanField(default=True)

