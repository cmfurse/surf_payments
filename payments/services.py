from payments.models import User, PaymentRequest
from datetime import date
from dateutil.relativedelta import relativedelta


def generate_single_fee_requests(fee):
    users = User.objects.filter(is_active=True)
    amount = _calculate_amount(fee, users)

    for user in users:
        PaymentRequest.objects.create(
            user=user,
            fee=fee,
            due_date=fee.due_date,
            amount=amount
        )


def generate_recurring_fee_requests(fee):
    users = User.objects.filter(is_active=True)
    amount = _calculate_amount(fee, users)
    due_date = (date.today() + relativedelta(months=2)).replace(day=fee.recurring_day_of_month)

    for user in users:
        PaymentRequest.objects.create(
            user=user,
            fee=fee,
            due_date=due_date,
            amount=amount
        )


def _calculate_amount(fee, users):
    amount = fee.amount
    if fee.split_per_player:
        amount = fee.amount // users.count()
    return amount

