from django.shortcuts import render
from django.db.models import Case, When, Value, IntegerField
from .models import Kruzok

def zoznam_kruzkov(request):
    # Bonus: Zoradenie podľa dní pomocou podmienok
    kruzky = Kruzok.objects.annotate(
        den_poradie=Case(
            When(den='Pondelok', then=Value(1)),
            When(den='Utorok', then=Value(2)),
            When(den='Streda', then=Value(3)),
            When(den='Štvrtok', then=Value(4)),
            When(den='Piatok', then=Value(5)),
            default=Value(6),
            output_field=IntegerField(),
        )
    ).order_by('den_poradie')

    return render(request, 'kruzky.html', {'kruzky': kruzky})