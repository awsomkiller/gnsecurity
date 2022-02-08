from django.shortcuts import  render

def home(request):
    return render(request, 'index.html')

def contactus(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')
