from django.shortcuts import render

from triangle.forms import GetForm


def get_form(request):
    hypotenuse = None
    if 'submit' in request.GET:
        get_form = GetForm(request.GET)
        if get_form.is_valid():
            leg1 = get_form.cleaned_data['leg1']
            leg2 = get_form.cleaned_data['leg2']
            hypotenuse = round(((leg1 ** 2 + leg2 ** 2) ** 0.5), 2)
    else:
        get_form = GetForm()
    return render(
        request,
        'triangle/triangle.html',
        {'get_form': get_form,
         'hypotenuse': hypotenuse, }
    )
