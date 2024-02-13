from django.shortcuts import render, redirect
from .models import Item
from django.contrib import messages
from django.http import HttpResponse
from .forms import Itemforms
from django.contrib.auth import authenticate, login


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page or dashboard
            return redirect('item_list')  # Replace 'item_list' with the appropriate URL name
        else:
            messages.error(request, 'Invalid username or password')
    return render(request,'homepage.html')



def item_list(request):
    showall = Item.objects.all()
    return render(request,'index.html',{"data": showall})


def form_display(request):
    if request.method == "POST":
        if request.POST.get('itemname') and request.POST.get('amount') and request.POST.get('bought_from') and request.POST.get('bought_on') and request.POST.get('price') and request.POST.get('ref'):
            saverecord = Item()
            saverecord.itemname = request.POST.get('itemname')
            saverecord.amount = request.POST.get('amount')
            saverecord.bought_from = request.POST.get('bought_from')
            saverecord.bought_on = request.POST.get('bought_on')
            saverecord.price = request.POST.get('price')
            saverecord.ref = request.POST.get('ref')
            saverecord.save()

            messages.success(request,f'Item "{saverecord.itemname}" has been added successfully')
            return render(request,'form.html')

    else:
        return render(request,'form.html')

    
def Edit_item(request,id):
    Edit_item_obj = Item.objects.get(id=id)
    return render(request,'Edit.html',{"Item":Edit_item_obj})

def Update_item(request,id):
    Update_item_obj = Item.objects.get(id=id)
    print(request.POST.get('amount'))
    Update_item_obj.amount = f"{request.POST.get('amount')} units"
    Update_item_obj.save()
    messages.success(request,'Record updated successfully!')
    return render(request,'Edit.html',{"Item":Update_item_obj})
    

def Delete_item(request,id):
    Delete_item_obj = Item.objects.get(id=id)
    Delete_item_obj.delete()
    showdata = Item.objects.all
    return render(request,'Index.html',{"data":showdata})

