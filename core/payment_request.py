from django.shortcuts import render, redirect
from account .models import Account
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from decimal import Decimal
from core.models import Transaction

@login_required
def search_users_request(request):
    account = Account.objects.all()
    query = request.POST.get("account_number")
    
    if query:
        account = account.filter(
            Q(account_number=query),
        ).distinct()
        
    context = {
        "account": account,
        "query": query,
    }
    
    return render(request, "payment_request/search_user.html", context)

def amount_request(request, account_number):
    account = Account.objects.get(account_number=account_number)
    
    context = {
        "account": account,
    }
    
    return render(request, "payment_request/amount-request.html", context)

def amount_request_process(request, account_number):
    account = Account.objects.get(account_number=account_number)
    request_sender = request.user
    request_recipient = account.user
    
    request_sender_account = request.user.account
    request_recipient_account = account
    
    if request.method == "POST":
        amount = request.POST.get("amount-request")
        description = request.POST.get("description")
        
        new_request = Transaction.objects.create(
            user=request.user,
            amount=amount,
            payment_description=description,
            
            sender=request_sender,
            recipient=request_recipient,
            
            sender_account=request_sender_account,
            recipient_account=request_recipient_account,
            
            status="requested",
            transaction_type="request",
        )
        new_request.save()
        
        transaction_id = new_request.transaction_id
        
        return redirect("core:amount-request-confirmation", account.account_number, transaction_id)        
    else: 
        messages.warning(request, "Error occurred. Try again later.")
        return redirect("account:dashboard")        

def amount_request_confirmation(request, account_number, transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)
    
    context = {
        "account": account,
        "transaction": transaction,
    }
    
    return render(request, "payment_request/amount-request-confirmation.html", context)