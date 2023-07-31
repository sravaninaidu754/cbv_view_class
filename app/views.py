from django.shortcuts import render
from django.views.generic import View,TemplateView
# Create your views here.
from django.http import HttpResponse

def fbv_string(request):
    return HttpResponse("<h1> This is fbv_string response</h1>")



def fbv_temp(request):
    return render(request,'fbv_temp.html')



class cbv_string(View):
    def get(self,request):
        return HttpResponse("this is cbv_string response")

class cbv_temp(TemplateView):
    template_name='cbv_temp.html'