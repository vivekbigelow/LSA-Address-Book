from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.db.models import Q
from .models import Contact
from .forms import ContactCreateForm

# Create your views here.

def register_view(request):
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
    form.save()
    user = form.cleaned_data.get('username')
    messages.success(request, 'Account was created for '+ user)
    return redirect('login')
  context ={
    'form':form
  }

  return render(request,'register.html',context)

def login_view(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.info(request,'Username or password is incorrect')
      
  return render(request,'login.html')

def logout_view(request):
  logout(request)
  return redirect('home')
   

def home_view(request):
  return render(request,'home.html')

def contacts_view(request):
  obj = Contact.objects.all()
  context = {
    "contact_list": obj
  }
  return render(request,'contacts.html', context)

def contact_details_view(request,id):
  obj = get_object_or_404(Contact, id=id)
  context = {
    "obj" :obj
  }
  return render(request,'contact_details.html', context)

def contact_create_view(request):
  form = ContactCreateForm(request.POST or None)
  if form.is_valid():
    instance = form.save(commit=False)
    instance.user = request.user
    instance.save()
    return redirect('contacts')
    
  context = {
    'form':form
  }
  return render(request,"contact_create.html", context)

def contact_delete_view(request, id):
  obj = get_object_or_404(Contact, id=id)
  if request.method == 'POST':
    obj.delete()
    return redirect('contacts')
  context = {
    "obj":obj
  }

  return render(request,"contact_delete.html" , context)

def contact_edit_view(request, id):
  obj = get_object_or_404(Contact, id=id)
  form = ContactCreateForm(request.POST or None, instance=obj)
  if form.is_valid():
    form.save()
    return redirect('contacts')

  context = {
    'form':form
  }

  return render(request,"contact_edit.html", context)

def search_view(request):
  return render(request,"search.html")

def search_results_view(request):
  query = request.GET.get('q')
  object_list = []
  for contact in Contact.objects.all():
    if contact.firstName.lower() == query or contact.lastName.lower() == query:
      object_list.append(contact)
  
  context = {
    'object_list':object_list
  }
  return render(request,"search_results.html",context)