from django.db import models
from django.contrib.auth import get_user_model
from apps.groups.models import Group

# Create your models here.

User = get_user_model()


class Expense(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="expenses"
    )
    paid_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="paid_expenses"
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.amount}"


class ExpenseShare(models.Model):
    expense = models.ForeignKey(
        Expense,
        on_delete=models.CASCADE,
        related_name="shares"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="expense_shares"
    )
    share_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.user} owes {self.share_amount}"