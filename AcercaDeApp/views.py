from django.shortcuts import render


def acerca_de(request):

    return render(request, "AcercaDeApp/acerca_de.html", {})