from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Lots, CutOfBanana
from .forms import LotForm, CutForm
from django.views.generic import ListView
# -----------------------
    
# Based functions
def listLots(request):
    if request.method == 'POST':
        form = LotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = LotForm()
            return render(request, 'partials/list-lots.html', {'form': form})
    else:
        form = LotForm()

        # search system
        search = request.GET.get('search')
        
        if search:
            
            lots = Lots.objects.filter(local__icontains=search)
        else:

            # definir variavel com todos os objetos
            lots = Lots.objects.all()
        
        return render(request, 'partials/list-lots.html', {'lots':lots, 'form': form})

def deleteLot(request, id):
     lot = get_object_or_404(Lots, pk=id)
     cuts = CutOfBanana.objects.filter(id_lot=id)
     cuts.delete()
     lot.delete()
     messages.info(request, 'Lote deletado com sucesso!')
     return redirect('/')
 
def deleteCut(request, id):
    cut = get_object_or_404(CutOfBanana, pk=id)
    id_lot = cut.id_lot
    cut.delete()
    messages.info(request, 'Corte deletado com sucesso!')
    return redirect('/lot/'+str(id_lot))

def viewLot(request, id):
    if request.method == 'POST':
        form = CutForm(request.POST)
        if form.is_valid():
            cutLot = form.save(commit=False)
            cutLot.id_lot = int(id)
            primeira = form.cleaned_data['primeira']
            segunda = form.cleaned_data['segunda']
            cutLot.porcentagem = round(100*float(primeira/(primeira+segunda)))
            cutLot.save()
            return redirect('/lot/'+str(id))
        else: 
            form = CutForm()
            return render(request, 'partials/lot.html', {'form': form})
    else:
        form = CutForm()
        
        search = request.GET.get('search')
        
        if search:
            cuts = CutOfBanana.objects.filter(id_lot=id,data__icontains=search)
        else:
            cuts = CutOfBanana.objects.filter(id_lot=id).order_by('-data')
    
        lot_current = get_object_or_404(Lots, pk=id)
        
        return render(request, 'partials/lot.html', {'lot': lot_current, 'cuts': cuts, 'form': form})

def editLot(request, id):
    lot = get_object_or_404(Lots, pk=id)
    form = LotForm(instance=lot)
    if request.method == 'POST':
        form = LotForm(request.POST, instance=lot)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'partials/edit-lot.html', {'lot': lot, 'form': form})
    else:
        return render(request, 'partials/edit-lot.html', {'lot': lot, 'form': form})

def editCut(request, id):
    cut = get_object_or_404(CutOfBanana, pk=id)
    form = CutForm(instance=cut)
    if request.method == 'POST':
        form = CutForm(request.POST, instance=cut)
        if form.is_valid():
            form.save() 
            return redirect('/lot/'+str(cut.id_lot))
        else:
            return render(request, 'partials/edit-cut.html', {'cut': cut, 'form': form})
    else:
        return render(request, 'partials/edit-cut.html', {'cut': cut, 'form': form})