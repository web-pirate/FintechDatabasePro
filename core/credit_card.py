from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.models import CreditCard
from account.models import Account
from decimal import Decimal

def card_detail(request, card_id):
    card = CreditCard.objects.get(card_id=card_id, user=request.user)
    account = Account.objects.get(user=request.user)
    
    context = {
        "card":card,
        "account":account,
    }
    return render(request, "cards/card-details.html", context)

def fund_card(request, card_id):
    card = CreditCard.objects.get(card_id=card_id, user=request.user)
    account = request.user.account 
    
    if request.method =="POST":
        amount = request.POST.get("funding-amount")
        
        if Decimal(amount) <= account.account_balance: 
            account.account_balance -= Decimal(amount)
            account.save()
            
            card.amount += Decimal(amount)
            card.save()
            
            messages.success(request, "Card funded successfully.")
            return redirect('core:card-details', card.card_id)
        else: 
            messages.warning(request, "Insufficient funds.")
            return redirect('core:card-details', card.card_id)
