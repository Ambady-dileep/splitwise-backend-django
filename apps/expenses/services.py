from decimal import Decimal
from collections import defaultdict
from apps.expenses.models import ExpenseShare


def calculate_group_settlements(group):
    """
    Returns: dict {user: net_balance}
    +ve => user should receive money
    -ve => user owes money
    """
    balances = defaultdict(Decimal)
    shares = ExpenseShare.objects.filter(
        expense__group = group
    ).select_related("user","expense")

    for share in shares:
        balances[share.user] -= share.share_amount
        balances[share.expense.paid_by] += share.share_amount

    return balances


def simplify_settlements(balances):
    """
    Converts net balances into transactions.
    """

    debtors = []
    creditors = []

    for user, balance in balances.items():
        if balance < 0:
            debtors.append([user, -balance])
        elif balance > 0:
            creditors.append([user, balance])

    settlements = []

    i = j = 0

    while i < len(debtors) and j < len(creditors):
        debtor, debt = debtors[i]
        creditor, credit = creditors[j]

        amount = min(debt, credit)

        settlements.append({
            "from": debtor,
            "to": creditor,
            "amount": amount
        })

        debtors[i][1] -= amount
        creditors[j][1] -= amount

        if debtors[i][1] == 0:
            i += 1
        if creditors[j][1] == 0:
            j += 1

    return settlements
