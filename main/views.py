from django.core import signing
from django.core.mail import send_mail
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from main.models import Customers, Cryptos, Amount
from main.permission import CheckUser, IsAdminOrReadOnly
from main.serializers import customer_serializer, update_avatar_serializer, Admin_users, CryptosSerializer, \
    AmountSerializer, AmountSerializerCreateorUpdate, CustomerUpdateSerializer, SignUp0authSerializer


class update_avatar_view(UpdateAPIView):
    queryset = Customers.objects.all()
    serializer_class = update_avatar_serializer
    permission_classes = [CheckUser, ]


@api_view(['GET'])
def test(request):
    send_mail(
        "Startris RestPassword",
        f"""
                Hello welcome to our website
                for verify click this link https://startrise.runflare.run/auth/resetpassword/
            """,
        "rosebetteam@gmail.com",
        ['www.salirezasaberi.com@gmail.com'],
        fail_silently=False,
    )
    return Response({'status': 'ok'})


class user(CreateAPIView):
    model = Customers
    serializer_class = customer_serializer


class Oauth(CreateAPIView):
    model = Customers
    serializer_class = SignUp0authSerializer


class OAuthLogin(TokenObtainPairView):
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        setattr(request,'_mutable',True)
        request.data['password'] = f"{request.data['username']}9430D3E65A917FC63D6308712C6C4363"
        response = super().post(request, *args, **kwargs)
        return response

class UpdateUserView(UpdateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerUpdateSerializer
    permission_classes = [CheckUser,]

class users(ListAPIView):
    queryset = Customers.objects.filter(is_superuser=False)
    serializer_class = Admin_users
    permission_classes = [IsAdminUser, ]


class CryptosView(CreateAPIView):
    model = Cryptos
    serializer_class = CryptosSerializer


class CryptoView(ListAPIView):
    queryset = Cryptos.objects.all()
    serializer_class = CryptosSerializer


class RUDCryptosView(RetrieveUpdateDestroyAPIView):
    queryset = Cryptos.objects.all()
    lookup_url_kwarg = 'pk'
    serializer_class = CryptosSerializer
    permission_classes = [IsAdminOrReadOnly, ]


class AmountView(CreateAPIView):
    model = Amount
    serializer_class = AmountSerializerCreateorUpdate

@api_view(['post'])
def ChangeAmountView(request):
    try:
        amount = Amount.objects.get(customer= request.user.id,crypto= request.data.get('crypto'),value= request.data.get('value'))
        if request.data.get('win'):  
            amount.value += int(request.data.get('profit'))
        else:
            amount.value -= int(request.data.get('profit'))
        amount.save()
        return Response(AmountSerializer(amount,many=False).data)
    except Exception as e:
        return Response({'text': 'error'})   
class AmountListView(ListAPIView):
    queryset = Amount.objects.all()
    serializer_class = AmountSerializer

class GetUserAmounts(ListAPIView):
    serializer_class = AmountSerializer
    def get_queryset(self):
        return Amount.objects.filter(customer_id = self.request.user.id)

@api_view(['post'])
def CheckAmount(request):
    try:
        amount = Amount.objects.get(customer_id = request.data.get('customer'),crypto__name = request.data.get('crypto'),value= request.data.get('value'))
        return Response(AmountSerializer(amount,many=False).data)
    except Exception as e:
        return Response({'not found ': 'we not found amount with this'}) 

@api_view(['post'])
def LowerAmount(request):
    try:
        amount = Amount.objects.get(customer_id = request.data.get('customer'),crypto__name = request.data.get('crypto'),value= request.data.get('value'))  
        # amount = Amount.objects.get(customer_id = 3)  
        amount.value = amount.value - int(request.data.get('NewValue'))
        if amount.value == 0:
            amount.delete()
            return Response(({'successful': 'Withdrawal was successful'}))
        amount.save()
        return Response(AmountSerializer(amount,many=False).data)
    except Exception as e:
        return Response({'not found ': 'we not found amount with this'}) 
    

@api_view(['post'])
def DisableUser(request):
    user = Customers.objects.get(id= request.data.get('customer'))
    user.is_active = False
    user.save()
    return Response(customer_serializer(user,many=False).data)


@api_view(['post'])
def VerifyUser(request):
    try:
        sign = signing.loads(request.data.get('token'), key='9430D3E65A917FC63D6308712C6C4363')
        user = Customers.objects.get(username=sign['email'])
        user.is_active = True
        user.save()
        return Response({'text': 'ok'})
    except:
        return Response({'text': 'bad'})
    
    
@api_view(['post'])
def ChangeLevelView(request):
    try:
        user = Customers.objects.get(customer= request.user.id)
        user.level += int(request.data.get('level'))
        user.save()
        return Response({'text': user.level})
    except Exception as e:
        return Response({'text': 'error'})
    
@api_view(['post'])
@permission_classes([IsAdminUser])
def ChnageActivityUserView(request):
    try:
        user = Customers.objects.get(username=request.data.get('email'))
        user.is_active = not(request.data.get('is_active'))
        user.save()
        return Response(Admin_users(user,many=False).data)
    except Exception as e:
        return Response({'text': 'error'})
    