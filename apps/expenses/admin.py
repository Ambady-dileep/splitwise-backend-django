from django.contrib import admin
from .models import Expense, ExpenseShare
# Register your models here.

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("id","description","amount","paid_by","group")
    list_filter = ("group",)
    search_fields = ("description",)

@admin.register(ExpenseShare)
class ExpenseShareAdmin(admin.ModelAdmin):
    list_display = ("expense","user","share_amount")

