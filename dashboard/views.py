from django.shortcuts import render
from .models import production_pvrmt


def dashboard(request):
    temps = []
    charge = []
    decharge = []
    
    productionpvrmt = production_pvrmt.objects.order_by('-dt_utc')[2000:2888]

    for prod in productionpvrmt :
        temps.append(prod.dt_utc.strftime("%H:%M"))
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