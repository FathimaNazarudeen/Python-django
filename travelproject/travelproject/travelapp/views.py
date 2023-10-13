from django.http import HttpResponse
from django.shortcuts import render
from . models import Place1
from . models import Team
# Create your views here.
def demo(request):
    #name="India"
    obj=Place1.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html", {'result':obj, 'res': obj1})


#def about(request):
 #   return render(request,"result.html")
#def contact(request):
 #   return HttpResponse("hellooooo")

#def addition(request):
   # x=int(request.GET['num1'])
    #y = int(request.GET['num2'])
    #add=x+y
    #sub=x-y
    #mul=x*y
    #div=x/y

    #return render(request,"result.html", {'add_result': add, 'sub_result': sub, 'mul_result': mul, 'div_result': div  })