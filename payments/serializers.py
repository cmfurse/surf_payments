from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Fee, PaymentRequest
from .services import generate_single_fee_requests, generate_recurring_fee_requests


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'phone', 'is_staff', 'is_active', 'player_name',
                  'balance']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).update(instance, validated_data)


class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = '__all__'
        # TODO: add validator? recurring or due date required but not both

    def create(self, validated_data):
        fee = super(FeeSerializer, self).create(validated_data)
        if fee.due_date is not None:
            generate_single_fee_requests(fee)
        elif fee.recurring:
            generate_recurring_fee_requests(fee)
        return fee


class PaymentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentRequest
        fields = '__all__'
