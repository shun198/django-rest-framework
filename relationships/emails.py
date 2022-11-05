from django.core import mail
from django.template.loader import render_to_string


def send_password_reset(user_email, url):
    plaintext = render_to_string("../templates/reset_password.txt", {"url": url})
    html_text = render_to_string("../templates/reset_password.html", {"url": url})

    mail.send_mail(
        subject="パスワードリセットの依頼",
        message=plaintext,
        from_email="example@mail.com",
        recipient_list=[user_email],
        html_message=html_text,
    )


def send_welcome_email(user_email, username, url):
    plaintext = render_to_string("../templates/welcome_email.txt", {"username": username, "url": url})
    html_text = render_to_string("../templates/welcome_email.html", {"username": username, "url": url})

    mail.send_mail(
        subject="ようこそ",
        message=plaintext,
        from_email="example@mail.com",
        recipient_list=[user_email],
        html_message=html_text,
    )
