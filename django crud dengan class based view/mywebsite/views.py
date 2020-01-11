from django.shortcuts import render

def index(request):
    context = {
        'title':'Home',
        'content':'Halaman Home',

    }

    return render(request, 'index.html', context)
