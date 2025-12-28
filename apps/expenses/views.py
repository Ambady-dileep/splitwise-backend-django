from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from apps.groups.models import Group
from .services import calculate_group_settlements, simplify_settlements


@login_required
def group_settlements_view(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    # 🔐 permission check
    if request.user not in group.members.all():
        return HttpResponseForbidden("You are not a member of this group")

    balances = calculate_group_settlements(group)
    settlements = simplify_settlements(balances)

    data = [
        {
            "from": s["from"].username,
            "to": s["to"].username,
            "amount": float(s["amount"])
        }
        for s in settlements
    ]

    return JsonResponse({"settlements": data})
