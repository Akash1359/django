from django.shortcuts import render, HttpResponse

# Create your views here.
def Home(request):
    context ={
        "variable1":"this is sent",
        "variable2":"lol"
    }
    return render(request, "index.html", context)

def about(request):
     return render(request, "about.html")
   # return HttpResponse("this is About page")

def services(request):
     return render(request, "services.html")
   # return HttpResponse("This is service page")

def contact(request):
      return render(request, "contact.html")
   # return HttpResponse("This is my contact")
