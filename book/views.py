from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyzed(request):
    djtext = request.POST.get('text','default')
    capitalize = request.POST.get('capitalize','Off')
    print(djtext)    

    removepun = request.POST.get('removepunc', 'Off')
    if removepun == "on":
        print(removepun)
        
        analyze = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char
        djtext = analyze
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyze}
        print(analyze)
        #return HttpResponse("This is remove punchuation page......")
        #return render(request, 'analyzed.html', params)
    
    if capitalize =="on":
        analyze = ""
        for char in djtext:
            analyze = analyze + char.upper()

        params = {'purpose':'Your Uppercase paragraph :', 'analyzed_text':analyze}
       # return render(request, 'analyzed.html', params)
     

    if removepun != "on" and capitalize != "on":
        return HttpResponse("Please Select The action......")
    #else:
     #   return HttpResponse("Please Select The action......")
    return render(request, 'analyzed.html', params)

# def product(request):
#     return HttpResponse('<h1>This is product site page</h1>')

# def navbar(request):
#     return HttpResponse("Navbar text with an inline element  <a href='/kirshna.png'> Image</a>")

# def youtube(request):
#     return HttpResponse("This is Youtube site <a href='https://www.youtube.com/watch?v=Lg8KPi8nY1E'> Yotube</a>")

# def capitalize(request):
#     return render(request, 'index.html')

def removepunc(request):
    djtext = request.POST.get('text','default')
    print(djtext)

    
    return HttpResponse("This is remove punchuation page......")