from django.core.mail import send_mail


def send_confirmation_email(email, code):
    full_link = f'http://localhost:8000/v1/api/account/activate/{code}'
    send_mail(
        'User activation',
        full_link,
        'aliyakomanovaa@gmail.com',
        [email, ]
    )