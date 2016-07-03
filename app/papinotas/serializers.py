from rest_framework import serializers
from app.papinotas.models import *

class GroupsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Groups
		fields = '__all__'


class StudentsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Students
		fields = '__all__'