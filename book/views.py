from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyzed(request):
    djtext = request.GET.get('text','default')
    capitalize = request.GET.get('capitalize','Off')
    print(djtext)    

    removepun = request.GET.get('removepunc', 'Off')
    if removepun == "on":
        print(removepun)
        
        not_punc = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        
        for char in djtext:
            if char not in punctuations:
                not_punc = not_punc + char
        
        params = {'purpose':'Removed Punctuations', 'analyzed_text':not_punc}
        print(not_punc)
        #return HttpResponse("This is remove punchuation page......")
        return render(request, 'analyzed.html', params)
    
    elif capitalize =="on":
        capital = ""
        for char in djtext:
            capital = capital + char.upper()

        params = {'purpose':'Your Uppercase paragraph :', 'analyzed_text':capital}
        return render(request, 'analyzed.html', params)
     
    else:
        return HttpResponse("Please Select The action......")
    

# def product(request):
#     return HttpResponse('<h1>This is product site page</h1>')

# def navbar(request):
#     return HttpResponse("Navbar text with an inline element  <a href='/kirshna.png'> Image</a>")

# def youtube(request):
#     return HttpResponse("This is Youtube site <a href='https://www.youtube.com/watch?v=Lg8KPi8nY1E'> Yotube</a>")

# def capitalize(request):
#     return render(request, 'index.html')

def removepunc(request):
    djtext = request.GET.get('text','default')
    print(djtext)

    
    return HttpResponse("This is remove punchuation page......")