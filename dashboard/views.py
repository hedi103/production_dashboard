from django.shortcuts import render
from .models import production_pvrmt


def dashboard(request):
    temps = []
    charge = []
    decharge = []
    
    productionpvrmt = production_pvrmt.objects.exclude(charge=0).exclude(decharge=0).order_by('-dt_utc')[:30]

    for prod in productionpvrmt :
        temps.append(prod.dt_utc.strftime("%Y-%m-%d %H:%M:%S"))
        charge.append(prod.charge)
        decharge.append(prod.decharge)

    return render(
        request, 
        "dashboard.html",
        {
            'labels': temps,
            'charge': charge,
            'decharge': decharge,
            'colors': []
        }

        )