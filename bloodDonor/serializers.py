from rest_framework import serializers
from .models import DonorDetail

class DonorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorDetail
        fields = "__all__"