from rest_framework import serializers
from .models import UserProfile,UserAddress
from django.contrib.auth.models import User
from .constants import GENDER_TYPE
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    dp = serializers.ImageField(required=False, allow_null=True)
    gender = serializers.ChoiceField(choices=GENDER_TYPE)
    phone_number = serializers.CharField(max_length=15)
    city = serializers.CharField(max_length=50)
    street_address = serializers.CharField(max_length=100)
    street_number = serializers.CharField(max_length=20)
    postal_code = serializers.CharField(max_length=10)
    country = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'dp', 'gender','phone_number', 'city', 'street_address', 'street_number', 'postal_code', 'country']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        dp = self.validated_data.get('dp')
        gender = self.validated_data['gender']
        phone_number = self.validated_data['phone_number']
        city = self.validated_data['city']
        street_address = self.validated_data['street_address']
        street_number = self.validated_data['street_number']
        postal_code = self.validated_data['postal_code']
        country = self.validated_data['country']

        if password != password2:
            raise serializers.ValidationError({'error': "Password Doesn't Matched"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "Email Already exists"})

        # Create User instance
        user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        # user.is_active = False
        user.save()

        # Create UserProfile instance
        profile = UserProfile.objects.create(user=user, dp=dp, gender=gender, phone_number=phone_number)

        # Create UserAddress instance
        address = UserAddress.objects.create(user=user, city=city, street_address=street_address,street_number=street_number, postal_code=postal_code, country=country)

        return user



class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)