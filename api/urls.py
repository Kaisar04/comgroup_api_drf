from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('emp-list/', views.empList, name="emp-list"),
	path('emp-detail/<str:pk>/', views.empDetail, name="emp-detail"),
	path('emp-create/', views.empCreate, name="emp-create"),

	path('emp-update/<str:pk>/', views.empUpdate, name="emp-update"),
	path('emp-delete/<str:pk>/', views.empDelete, name="emp-delete"),
]