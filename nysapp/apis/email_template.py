
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.conf import settings
EMAIL_ADMIN  = settings.EMAIL_HOST_USER


def send_email_to_sales(request):
    message = get_template("emailtemplate/email_template.html").render({
        'data': "customer_detail"
    })
    
    mail = EmailMessage(
        subject=f"New Customer email status {request}",
        body=message,
        from_email=EMAIL_ADMIN,
        to=["grr@mailinator.com"],
        reply_to=[EMAIL_ADMIN],
    )
    mail.content_subtype = "html"
    return mail.send()