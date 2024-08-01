from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.models import CreditCard
from account.models import Account

def card_detail(request, card_id):
    card = CreditCard.objects.get(card_id=card_id, user=request.user)
    account = Account.objects.get(user=request.user)
    
    context = {
        "card":card,
        "account":account,
    }
    return render(request, "cards/card-details.html" ,context)