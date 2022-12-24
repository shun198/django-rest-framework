import pytest
from django.core import mail
from rest_framework.test import APIClient


@pytest.mark.django_db()
class TestInviteUser:
    client = APIClient()
    url = "/api/users/send_invite_user_mail/"

    def test_management_user_can_send_invite_user_email(self, management_user, email_data):
        self.client.login(username=management_user[0], password=management_user[1])
        response = self.client.post(self.url, email_data, format='json')
        assert response.status_code == 200
        # メールを一通受信したことを確認
        assert len(mail.outbox) == 1
        assert mail.outbox[0].subject == "ようこそ"
        assert mail.outbox[0].from_email == "example@mail.com"
        assert mail.outbox[0].to[0] == email_data["email"]
