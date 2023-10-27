from django.contrib.auth.hashers import make_password
from django.core import signing
from django.core.mail import send_mail, EmailMultiAlternatives
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from main.models import Customers, Cryptos, Amount


class customer_serializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        exclude = ['is_superuser']

    def create(self, validated_data):
        validated_data['username'] = validated_data.get('email')
        validated_data['password'] = make_password(validated_data.get('password'))
        validated_data['is_active'] = 0
        validated_data['is_staff'] = 0
        sign = signing.dumps({'email': validated_data.get('email')}, key='9430D3E65A917FC63D6308712C6C4363')
        html_content = render_to_string('email/verify.html', context={'email': validated_data.get('email'),
                                                                      'link': f"""http://localhost:3000/auth/verifypassword/{sign}"""})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            'Verify email',
            text_content,
            "rosebetteam@gmail.com",
            [validated_data.get('email'),]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        return super(customer_serializer, self).create(validated_data)


class Admin_users(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['is_active', 'first_name', 'last_name', 'level', 'email', 'last_login']


class CustomerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['first_name', 'last_name']

class update_avatar_serializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['avatar']


class CryptosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptos
        fields = '__all__'


class AmountSerializer(serializers.ModelSerializer):
    crypto = CryptosSerializer()
    class Meta:
        model = Amount
        fields = '__all__'


class AmountSerializerCreateorUpdate(serializers.ModelSerializer):
    def create(self, validated_data):
        try:
            amount = Amount.objects.get(customer = validated_data.get('customer'),crypto =validated_data.get('crypto'))
            amount.value += validated_data.get('value')
            amount.save()
            return amount
        except:
            return super(AmountSerializerCreateorUpdate,self).create(validated_data)
    class Meta:
        model = Amount
        fields = '__all__'


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, Customers):
        token = super().get_token(Customers)
        token['is_superuser'] = Customers.is_superuser
        token['level'] = Customers.level
        token['avatar'] = Customers.avatar
        token['first_name'] = Customers.first_name
        token['last_name'] = Customers.last_name
        token['email'] = Customers.email
        token['level'] = Customers.level
        return token

class SignUp0authSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        exclude = ['is_superuser',]
    def create(self, validated_data):
        validated_data['password'] = make_password(f"{validated_data.get('email')}9430D3E65A917FC63D6308712C6C4363")
        validated_data['username'] = validated_data.get('email')
        return super(SignUp0authSerializer, self).create(validated_data)
