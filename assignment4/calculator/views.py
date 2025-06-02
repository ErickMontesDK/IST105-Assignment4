from django.shortcuts import render
from .forms import InputForm

def calculate_view(request):
    form = InputForm(request.POST or None)
    error ="You send invalided values"
    result = error 

    if request.method == 'POST' and form.is_valid():
        a = form.cleaned_data['a']
        b = form.cleaned_data['b']
        c = form.cleaned_data['c']


        if a < 1:
            error = "A value is too small."
        elif b == 0:
            error ="B value will not affect the result"
        elif c < 0:
            error = "C must be bigger or equal to zero"
        else:
            calc = None
            c_cube = c ** 3
            
            if c_cube > 1000:
                calc = 10*(c_cube**.5)
            else:
                calc = (c_cube**.5) / a
            result = calc + b
    return render(request, 'result.html', {'form': form, 'result': result, 'error': error})
