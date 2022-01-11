from django.shortcuts import  render

def wait(request):
    return render(request, 'wait.html')