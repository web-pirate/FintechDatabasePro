from django.shortcuts import render, redirect
from account .models import Account
from django.contrib.auth.decorators import login_required

@login_required
def search_users_by_account_number(request):
    # account = Account.objects.filter(account_status="active")
    account = Account.objects.all()
    context = {
        "account": account,
    }
    return render(request, "transfer/search-user-by-account-number.html", context)