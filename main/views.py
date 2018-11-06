from django.shortcuts import render, get_object_or_404
from .forms import questionForms
from .models import question
import sympy

def wait_page(request):

    if request.method == "POST":

        value = request.POST.get('value')
        variable = request.POST.get('variable')

        form = questionForms({'value': value, 'variable': variable})

        if value and variable:
            if request.POST.get('action') == "Türev al":
                try:
                    diffequation = sympy.latex(sympy.diff(value, variable))
                except:
                    diffequation = 'Türev alınamadı.'
            elif request.POST.get('action') == "İntegral al":
                try:
                    diffequation = sympy.latex(sympy.integrate(value, (x)))
                except:
                    diffequation = 'İntegral alınamadı.'
        else:
            diffequation = 'Denklemi girmediniz.'

        context = {
            'form': form,
            'value': value,
            'diff': diffequation,
        }
    else:

        form = questionForms({'value': '', 'variable': 'x'})

        context = {
            'form': form,
        }

    return render(request, 'base.html', context)