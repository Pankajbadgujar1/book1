from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")

def product(request):
    return HttpResponse('<h1>This is product site page</h1>')

def navbar(request):
    return HttpResponse("Navbar text with an inline element")

def youtube(request):
    return HttpResponse("This is Youtube site <a href='https://www.youtube.com/watch?v=Lg8KPi8nY1E'> Yotube</a>")