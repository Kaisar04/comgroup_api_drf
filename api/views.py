from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EmpSerializer

from .models import Employer
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/api/emp-list/',
		'Detail View':'/api/emp-detail/<str:pk>/',
		'Create':'/api/emp-create/',
		'Update':'/api/emp-update/<str:pk>/',
		'Delete':'/api/emp-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def empList(request):
	emps = Employer.objects.all().order_by('-id')
	serializer = EmpSerializer(emps, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def empDetail(request, pk):
	emps = Employer.objects.get(id=pk)
	serializer = EmpSerializer(emps, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def empCreate(request):
	serializer = EmpSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def empUpdate(request, pk):
	emp = Employer.objects.get(id=pk)
	serializer = EmpSerializer(instance=emp, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def empDelete(request, pk):
	emp = Employer.objects.get(id=pk)
	emp.delete()

	return Response('Item succsesfully delete!')