from django.urls import path
from core import views
from core import transfer

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    
    # Money Transfers
    path("search-account/", transfer.search_users_by_account_number, name="search-account")


]
