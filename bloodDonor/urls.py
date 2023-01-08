from django.conf.urls import url
from bloodDonor import views

urlpatterns = [
    url('donorDetails', views.BloodDonorView.as_view()),
    url('donorDetailsById/(?P<pk>[0-9]+)$', views.BloodDonorViewById.as_view()),
]
