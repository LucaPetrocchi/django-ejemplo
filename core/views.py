
from django.http import HttpResponse

def index(request):
    return HttpResponse("EL SORTREPO")

def about(request):
    return HttpResponse("rer")
