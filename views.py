from django.shortcuts import render
from rest_framework import generics
from .models import Profile
from .models import Course 
from .models import Enrollment 
from .models import LearningModule
from .serializers import UserSerializer
from .serializers import ProfileSerializer
from .serializers import CourseSerializer
from .serializers import EnrollmentSerializer
from .serializers import LearningModuleSerializer
from .models import Feedback
from .serializers import FeedbackSerializer
from .models import Notification
from .serializers import NotificationSerializer
from .models import NotificationSetting
from .serializers import NotificationSettingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


# Create your views here.

class UserCreate(generics.CreateAPIView):
    """Create a new user. """
    serializer_class = UserSerializer

class ProfileDetail(generics.RetriveUpdateAPIView):
    """Get and update a user profile. """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentList(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    
class LearningModuleList(generics.ListCreateAPIView):
    queryset = LearningModule.objects.all()
    serializer_class = LearningModuleSerializer

class LearningModuleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LearningModule.objects.all()
    serializer_class = LearningModuleSerializer
    
class FeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class NotificationList(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationSettingDetail(generics.RetrieveUpdateAPIView):
    queryset = NotificationSetting.objects.all()
    serializer_class = NotificationSettingSerializer
    
class LMSIntegration(APIView):
    def get(self, request, format=None):
        # Mock integration logic
        data = {"message": "LMS integration successful"}
        return Response(data)

class DataSynchronization(APIView):
    def post(self, request, format=None):
        # Mock synchronization logic
        data = {"message": "Data synchronization successful"}
        return Response(data)

class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('user-create')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


