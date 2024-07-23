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
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'phone', 'is_active', 'player_name', 'balance']

    def validate(self, data):
        if not data['is_superuser'] and data['player_name'] is None:
            raise serializers.ValidationError("Player name must be provided for non-superuser")
        return data

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        validated_data['username'] = validated_data.get('email')
        return super(UserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        validated_data['username'] = validated_data.get('email')
        return super(UserSerializer, self).update(instance, validated_data)


class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = '__all__'

    def validate(self, data):
        if data['recurring'] is True and data['due_date'] is not None:
            raise serializers.ValidationError("Due date is not needed for recurring fee")
        if data['recurring'] is False and data['due_date'] is None:
            raise serializers.ValidationError("Due date is required if non-recurring fee")
        if data['recurring'] is True and (data['recurring_day_of_month'] < 1 or data['recurring_day_of_month'] > 31):
            raise serializers.ValidationError("Invalid recurring day of month")
        return data

    def create(self, validated_data):
        fee = super(FeeSerializer, self).create(validated_data)
        if fee.due_date is not None:
            generate_single_fee_requests(fee)
        elif fee.recurring:
            generate_recurring_fee_requests(fee)
        return fee


class PaymentRequestSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    fee = FeeSerializer(read_only=True)

    class Meta:
        model = PaymentRequest
        fields = '__all__'
