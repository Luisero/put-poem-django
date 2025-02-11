from django.shortcuts import render, redirect
from .forms import PoemForm
from .models import Poem
# Create your views here.
def index(request):
    poems = Poem.objects.all()
    return render(request, 'core/others/index.html',{'poems':poems})



def create(request):
    if request.method == 'POST':
        form = PoemForm(request.POST)
        if form.is_valid():
            poem = form.save(commit=False)
            poem.author = request.user
            poem.save()
            
            return redirect('index')    
        
    else:
        form = PoemForm()

    return render(request,'core/others/create_poem.html',{'form': form})


def profile(request):
    return render(request, 'core/others/profile.html')