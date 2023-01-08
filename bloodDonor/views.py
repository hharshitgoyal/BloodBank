from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DonorDetail
from .serializers import DonorDetailSerializer


# Create your views here.
class BloodDonorView(APIView):

    def post(self, request):
        """
                API to create Blood Donor Details
        """
        serializer_data = DonorDetailSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return JsonResponse(serializer_data.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
                API to get all Donor Details
        """
        data = DonorDetail.objects.all().order_by('id')
        serialize_list = DonorDetailSerializer(data, many=True)
        return JsonResponse(serialize_list.data, safe=False)


class BloodDonorViewById(APIView):

    def put(self, request, pk):
        """
                API to update a particular Donor Detail
        """
        try:
            data = DonorDetail.objects.get(pk=pk)
        except DonorDetail.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        serializer = DonorDetailSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        """
                API to get a particular Donor Detail
        """
        try:
            data = DonorDetail.objects.get(pk=pk)
        except DonorDetail.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        serializer = DonorDetailSerializer(data)
        return Response(serializer.data)

    def delete(self, request, pk):
        """
                API to delete a particular Donor Detail
        """
        try:
            report = DonorDetail.objects.get(pk=pk)
        except DonorDetail.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        report.delete()
        return Response(status=status.HTTP_200_OK)
