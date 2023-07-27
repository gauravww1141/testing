from django.shortcuts import render
from django.views import View
from nysapp.apis.email_template import send_email_to_sales
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.urls import reverse
# Create your views here.


class Home(View):
    template_name = 'central/home.html'

    def get(self, request):
        send_email_to_sales("mysucskdjf")
        host = request.get_host()
        print(host)
        paypal_dict = {
                    'business': settings.PAYPAL_RECEIVER_EMAIL,
                    'amount': 2,
                    'item_name': 'Order nyse trade',
                    'currency_code': 'USD',
                    'custom_value':"gaurav rjaput",
                    'notify_url': 'http://{}{}'.format(host,
                                    reverse('paypal-ipn')),
                    'return_url': 'http://{}{}'.format(host,
                                                    reverse("payment-success")),
                    'cancel_return': 'http://{}{}'.format(host,
                                                        reverse('payment-failed')),
                
                        }
        form = PayPalPaymentsForm(initial=paypal_dict)
        context = {"payment_button":form}

        return render(request, self.template_name, context)
    


class Failed(View):
    template_name = 'central/failed_payment.html'

    def get(self, request):
        return render(request, self.template_name)
    
class Success(View):
    template_name = 'central/success_payment.html'

    def get(self, request):
        return render(request, self.template_name)