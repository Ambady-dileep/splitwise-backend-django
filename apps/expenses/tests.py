from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal
from django.contrib.auth import get_user_model

from apps.groups.models import Group
from apps.expenses.models import Expense, ExpenseShare

User = get_user_model()


class SettlementAPITest(TestCase):

    def test_settlement_api_authenticated(self):
        client = Client()

        user1 = User.objects.create_user(username="u1", password="123")
        user2 = User.objects.create_user(username="u2", password="123")

        group = Group.objects.create(name="Dinner")
        group.members.set([user1, user2])

        expense = Expense.objects.create(
            group=group,
            paid_by=user1,
            amount=Decimal("200.00"),
            description="Dinner"
        )

        ExpenseShare.objects.create(expense=expense, user=user1, share_amount=100)
        ExpenseShare.objects.create(expense=expense, user=user2, share_amount=100)

        client.login(username="u1", password="123")

        url = reverse("group-settlements", args=[group.id])
        response = client.get(url)

        self.assertEqual(response.status_code, 200)
