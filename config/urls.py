from django.contrib import admin
from django.urls import path
from expenses.views import dashboard, add_expense


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path("add-expense/", add_expense, name="add_expense"),
]