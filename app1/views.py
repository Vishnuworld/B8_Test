from django.shortcuts import render, HttpResponse
# Create your views here.

# atomic transaction
# View
# - Class based view
# - Function based view

from .models import Student

# view -- function based view
# def welcome(request):   # reserved keyword # business logic
    # print(request.method)
    # print(request.user)
    # print(request.GET["age"])  # http://127.0.0.1:8000/home/?name=abc&surname=pqr&age=25
    # studs = Student.objects.get(id=2)
    # studs = Student.objects.values("name")
    # final_studs = list(map(lambda x: x["name"], studs))
    # return HttpResponse(f"Welcome to the Django Application...!!{final_studs}")

def welcome1(request):  # http request
    print(request.user, request.method)
    print(request.__dict__)
    return render(request, "home.html")


def welcome(request):  # http request
    return render(request, "home.html")

def welcome2(request):  # http request
    print(request.user, request.method)
    print(request.__dict__)
    return render(request, "home.html")


def landing_page(request):
    return HttpResponse("on landing page")

# query params - Query Parameter