from django.shortcuts import render
def home(request):
    template_name="index.html"
    Content={"name":"Anuj"}
    return render(request,template_name,Content)