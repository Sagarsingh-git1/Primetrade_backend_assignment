from rest_framework import serializers
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):

    password=serializers.CharField(write_only=True,min_length=8)

    class Meta:
        model=User
        fields=['username','email','password','first_name','last_name','phone','address']

        extra_kwargs={
            'email':{'required':True},
        }

        

    def create(self,validated_data):
        password=validated_data.pop('password')
        user=User(**validated_data)
        user.set_password(password)
        user.save()
        return user




