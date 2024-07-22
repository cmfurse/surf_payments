from rest_framework import generics
from .models import User, Fee, PaymentRequest
from .serializers import UserSerializer, FeeSerializer, PaymentRequestSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FeeList(generics.ListCreateAPIView):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer


class FeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer


class PaymentRequestList(generics.ListCreateAPIView):
    queryset = PaymentRequest.objects.all()
    serializer_class = PaymentRequestSerializer


class PaymentRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentRequest.objects.all()
    serializer_class = PaymentRequestSerializer
