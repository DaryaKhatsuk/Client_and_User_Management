from django.core.mail import EmailMessage, get_connection
from Client_and_User_Management.settings import EMAIL_ADMIN


def support_email(date='', email='', message='', user='', cookies='', meta=''):
    with get_connection() as connection:
        EmailMessage(subject='Need support for User', body=f"Date: {date}\n"
                                                           f"Email: {email}\n"
                                                           f"Message: {message}\n"
                                                           f"Request User: {user}\n"
                                                           f"Request COOKIES: {cookies}\n"
                                                           f"Request META: {meta}\n",
                     from_email=EMAIL_ADMIN, to=[EMAIL_ADMIN],
                     connection=connection).send()
