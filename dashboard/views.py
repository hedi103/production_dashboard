import json
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import production_pvrmt
from django.views.decorators.http import require_POST


def dashboard(request):
    temps = []
    charge = []
    decharge = []
    ids = []
    
    productionpvrmt = production_pvrmt.objects.order_by('-dt_utc')[2000:2888]

    for prod in productionpvrmt :
        temps.append(prod.dt_utc.strftime("%H:%M"))
        charge.append(prod.charge)
        decharge.append(prod.decharge)
        ids.append(prod.id);

    return render(
        request, 
        "dashboard.html",
        {
            'labels': temps,
            'charge': charge,
            'decharge': decharge,
            'ids': ids,
            'colors': [],
            'nbar':'dashboard'
        }

        )

def lissage(request):
    return render(
        request, 
        "lissage.html",
        {'nbar':'lissage'}
        )

def decalage_prod(request):
    return render(
        request, 
        "decalage_prod.html",
        {'nbar':'decalage_prod'}
        )

def regulation_freq(request):
    return render(
        request, 
        "regulation_freq.html",
        {'nbar':'regulation_freq'}
        )

@require_POST
def update_prod_graph(request):
    charge = json.loads(request.POST.get('charge'))
    decharge = json.loads(request.POST.get('decharge'))
    ids = json.loads(request.POST.get('ids'))

    for i in range(len(ids)):
        production_pvrmt.objects.filter(id=ids[i]).update(charge=charge[i], decharge=decharge[i])

    return HttpResponse('Ok')