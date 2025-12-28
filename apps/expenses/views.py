from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from apps.groups.models import Group
from apps.expenses.services import calculate_group_settlements, simplify_settlements


@login_required
def group_settlements_view(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    balances = calculate_group_settlements(group)
    settlements = simplify_settlements(balances)

    data = [
        {
            "from": s["from"].username,
            "to": s["to"].username,
            "amount": str(s["amount"]),
        }
        for s in settlements
    ]

    return JsonResponse(data, safe=False)
