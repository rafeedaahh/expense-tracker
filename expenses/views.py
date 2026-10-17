from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .models import Transaction
from .forms import TransactionForm


def dashboard(request):
    transactions = Transaction.objects.all()

    total_income = transactions.filter(
        transaction_type="income"
    ).aggregate(total=Sum("amount"))["total"] or 0

    total_expenses = transactions.filter(
        transaction_type="expense"
    ).aggregate(total=Sum("amount"))["total"] or 0

    balance = total_income - total_expenses

    context = {
    "transactions": transactions,
    "total_income": total_income,
    "total_expenses": total_expenses,
    "balance": balance,
}

    return render(request, "expenses/dashboard.html", context)
@login_required(login_url="/admin/login/")
def add_expense(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)

       if form.is_valid():
    transaction = form.save(commit=False)
    transaction.user = request.user
    transaction.save()
    return redirect("dashboard")
    else:
        form = TransactionForm()

    return render(request, "expenses/add_expense.html", {"form": form})
# Create your views here.
