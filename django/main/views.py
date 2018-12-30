from django.shortcuts import render
import sympy

def page(request):

    flag = 0
    equation = ''

    value = request.POST.get('value')
    variable = request.POST.get('variable')

    if request.method == "POST":

        # Türev veya İntegral alma
        if value and variable:
            if request.POST.get('action') == "Türev al":
                try:
                    equation = sympy.latex(sympy.diff(value, variable))
                except:
                    flag = 1
            elif request.POST.get('action') == "İntegral al":
                try:
                    equation = sympy.latex(sympy.integrate(value, (variable,variable)))
                except:
                    flag = 2
        else:
            flag = 3

        context = {
            'value': value,
            'diff': equation,
            'flag': flag,
            'variable': variable
        }

    else:
        context = {
            'value': value,
            'diff': equation,
            'flag': flag,
            'variable': 'x',
        }

    return render(request, 'base.html', context)