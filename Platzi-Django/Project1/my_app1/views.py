from django.shortcuts import render

# Create your views here.
def my_view(request):
    car_list = [
        {"title":"BMW"},
        {"title":"Mazda"},
    ]

    # Contexto es lo que se le va a pasar al template
    context = {
        "car_list":car_list
    }
    return render(request, "car_list.html", context)