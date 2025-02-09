
# Create your views here.



from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderForm
from django.db.models import Sum


def order_list(request):

    orders = Order.objects.all()

    return render(request , 'order_list.html' , {'orders':orders})


def creat_order(request):

    if request.method == "POST":

        form  = OrderForm(request.POST)
        order = form.save(commit=False)
        order.total_price = calculate_total_price(order.items)
        order.save()
        return redirect('order_list')
    else:
        form = OrderForm()
    return render(request , 'order_form.html' ,{'form':form})

def update_order(request , pk):

    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = calculate_total_price(order.items)
            order.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'order_form.html', {'form': form})



def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order.delete()
        return redirect('order_list')
    return render(request, 'order_confirm_delete.html', {'order': order})

def total_revenue(request):
    revenue = Order.objects.filter(status='paid').aggregate(Sum('total_price'))['total_price__sum'] or 0
    return render(request, 'revenue.html', {'revenue': revenue})

# Функция для расчета общей стоимости заказа
def calculate_total_price(items_text):
    total = 0
    items = items_text.split(',')
    for item in items:
        try:
            name, price = item.strip().rsplit(' ', 1)
            total += float(price)
        except ValueError:
            pass  # Игнорируем ошибки парсинга
    return total