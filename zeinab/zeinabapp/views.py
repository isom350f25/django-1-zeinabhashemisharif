from django.shortcuts import render
from django.shortcuts import render


# Create your views here.
def zeinab_view(request):
    x="zeinab"
    y="2221192153"
    return render (request,"zeinab.html",
                    context={"name":x, "ID":y})

def myclasses_view(request):
    return render(request,"myclasses.html")

