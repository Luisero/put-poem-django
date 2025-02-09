from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/others/index.html')



#def add_poem(request):
    