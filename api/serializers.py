from rest_framework import serializers
from .models import Employer

class EmpChildrenSerializer(serializers.ModelSerializer): 
	class Meta:
		model = Employer
		fields ='__all__'

class RecursiveField(serializers.Serializer):
    """
    Self-referential field for MPTT.
    """
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class EmpSerializer(serializers.ModelSerializer): 
	children = RecursiveField(many=True, required=False)
	class Meta:
		model = Employer
		fields = ("id", "full_name", "job_title", "start_date", "salary", "parent", "children")