from django.shortcuts import render

# Create your views here.
def babu(request):
    d={'username':'this my frist web page'}
    return render(request,'babu.html',context=d)

def sai(request):
    c={'name':'nagendra','location':'proddatur'}
    return render(request,'sai.html',context=c)
