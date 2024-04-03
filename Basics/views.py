from django.shortcuts import render

# Create your views here.
def calculation(request):
    if request.method=="POST":
        num1=int(request.POST.get('txtno1'))
        num2=int(request.POST.get('txtno2'))
        btn=request.POST.get('btnsubmit')
        if btn=="+":
             result =num1+num2
        elif btn=="-":
            result=num1-num2
        elif btn=="*":
            result=num1*num2
        elif btn=="/":
            result=num1/num2
        
        return render(request,"Basics/Calculator.html",{'res':result})
    else:
        return render(request,"Basics/Calculator.html")
