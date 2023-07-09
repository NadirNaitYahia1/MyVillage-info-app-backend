from rest_framework import serializers
from .models import Bus,Users,Pharmacies,Admin
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = '__all__'
	def create(self, clean_data):
		user_obj = UserModel.objects.create_user(email=clean_data['email'], password=clean_data['password'])
		user_obj.username = clean_data['username']
		user_obj.save()
		return user_obj

class UserLoginSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField()
	##
	def check_user(self, clean_data):
		user = authenticate(username=clean_data['email'], password=clean_data['password'])
		if not user:
			raise ValidationError('user not found')
		return user

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = ('email', 'username')

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

class BusUsers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class PharmaciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacies
        fields = '__all__'
	

class AdminSerializer(serializers.ModelSerializer):
	class Meta:
		model = Admin
		fields = '__all__'