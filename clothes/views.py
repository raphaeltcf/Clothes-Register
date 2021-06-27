from django.shortcuts import render, redirect, get_object_or_404
from .models import Clothes
from .forms import ClothesForm
from django.views.generic import ListView, DetailView



class IndexView(ListView):
    template_name = 'clothes/index.html'
    context_object_name = 'clothes_list'
    
    def get_queryset(self):
        return Clothes.objects.all()

class ClothesDetailView(DetailView):
    model = Clothes
    template_name = 'clothes/clothes-detail.html'

def create(request):
    if request.method == 'POST':
        form = ClothesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ClothesForm()

    return render(request,'clothes/create.html',{'form': form})

def edit(request, pk, template_name='clothes/edit.html'):
    clothes = get_object_or_404(Clothes, pk=pk)
    form = ClothesForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='clothes/confirm_delete.html'):
    clothes = get_object_or_404(Clothes, pk=pk)
    if request.method=='POST':
        clothes.delete()
        return redirect('index')
    return render(request, template_name, {'object':clothes})