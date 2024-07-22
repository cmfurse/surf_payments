from datetime import date

from dateutil.relativedelta import relativedelta
from django.core.management import BaseCommand

from payments.models import Fee, PaymentRequest
from payments.services import generate_recurring_fee_requests


class Command(BaseCommand):
    help = "Generates payment requests for recurring fees"

    def handle(self, *args, **options):
        fees = Fee.objects.filter(recurring=True)
        for fee in fees:
            # only generate requests if they don't yet exist
            due_date = (date.today() + relativedelta(months=2)).replace(day=fee.recurring_day_of_month)
            requests = PaymentRequest.objects.filter(due_date=due_date, fee=fee)
            if requests.count() > 0:
                break
            generate_recurring_fee_requests(fee)

