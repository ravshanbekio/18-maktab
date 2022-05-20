from unittest import TestCase
from maktab_18.models import Home, Member

class TestHome(TestCase):
    def setUp(self):
        self.user = Home.objects.all()

    def test_get_all_users(self):
        assert self.user
    
    def test_get_user(self):
        self.assertIsNotNone(self.user[1].id)

    def test_create_user(self):
        name = "Test User 1"
        phone_number = "+998901234567"
        email = "ravshanbekrm06@gmail.com"

        user = Home.objects.create(
            name=name,
            phone_number=phone_number,
            email=email
        ).save()

class TestMember(TestCase):
    def create_member(self):
        email = "ravshanbekrm06@gmail.com"

        member = Member.objects.create(
            email=email
        )