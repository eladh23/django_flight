from django.http import HttpResponse
from django.shortcuts import render,redirect

from flight.models import Flight

def buy_ticket(request, flight_id):
    if request.method == 'POST':
        number = request.POST.get('number', '0') 
        print("NUMBER IS", number)
        if number:
            flight = Flight.objects.get(id=flight_id)
            flight.tickets = flight.tickets - int(number)
            flight.save()
            return redirect('all_flights')


    return HttpResponse('Invalid request')

    

def flights(request):
    
    all_flights = Flight.objects.all()
    context = {
        'flights': all_flights  
    }
    return render(request, 'flights_list.html', context)

def flights_text(request):
    all_flights = Flight.objects.all()
    mystr = ""
    for flight in all_flights:
        mystr += str(flight)
        mystr += "<br>"
    return HttpResponse(f"This is a list of flights!<br>{mystr}")