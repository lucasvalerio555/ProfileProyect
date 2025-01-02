from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
	return render(request, 'templetes/index.html')

def Work(request):
	return HttpResponse("Work....")

def About(request):
	return HttpResponse("About me....")

def Contact(request):
	return HttpResponse("Contact....")