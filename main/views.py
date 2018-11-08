from django.shortcuts import render
from .forms import questionForms
from .models import question
import sympy

def index_page(request):

    flag = 0

    if request.method == "POST":

        value = request.POST.get('value')
        variable = request.POST.get('variable')
        diffequation = ''

        form = questionForms({'value': value, 'variable': variable})

        if value and variable:
            if request.POST.get('action') == "Türev al":
                try:
                    diffequation = sympy.latex(sympy.diff(value, variable))
                except:
                    flag = 1
            elif request.POST.get('action') == "İntegral al":
                try:
                    diffequation = sympy.latex(sympy.integrate(value, (variable,variable)))
                except:
                    flag = 2
        else:
            flag = 3

        context = {
            'form': form,
            'value': value,
            'diff': diffequation,
            'flag': flag,
        }

    else:

        form = questionForms({'value': '', 'variable': 'x'})

        context = {
            'form': form,
        }

    return render(request, 'base.html', context)