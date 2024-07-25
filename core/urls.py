from django.urls import path
from core import views
from core import transfer
from core import transaction
from core import payment_request

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    
    # Money Transfers
    path("search-account/", transfer.search_users_by_account_number, name="search-account"),
    path("amount-transfer/<account_number>/", transfer.amount_transfer, name="amount-transfer"),
    path("amount-transfer-process/<account_number>/", transfer.amount_transfer_process, name="amount-transfer-process"),
    path("transfer-confirmation/<account_number>/<transaction_id>/", transfer.transfer_confirmation, name="transfer-confirmation"),
    path("transfer-process/<account_number>/<transaction_id>/", transfer.transfer_process, name="transfer-process"),
    path("transfer-completed/<account_number>/<transaction_id>/", transfer.transfer_completed, name="transfer-completed"),

    # Transactions
    path("transactions/", transaction.transaction_list, name="transactions"),
    path("transaction-detail/<transaction_id>", transaction.transaction_detail, name="transaction-detail"),
    
    # Paymennt Requests
    path("request-search-users/", payment_request.search_users_request, name="request-search-users"),
    path("amount-request/<account_number>/", payment_request.amount_request, name="amount-request"),
]
