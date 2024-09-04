from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306245863',
        'name': 'Aliya Zahira Nadra',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
