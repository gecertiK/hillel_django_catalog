from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from triangle.forms import GetForm, PersonForm
from triangle.models import Person


def first_page(request):
    return render(request, "triangle/first_page.html")


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


def person_create_form(request):
    if request.method == 'POST':
        person_form = PersonForm(data=request.POST)
        if person_form.is_valid():
            person_form.save()
            return redirect('triangle:person_list')
    else:
        person_form = PersonForm()
    return render(
        request,
        "triangle/person_create_form.html",
        {
            'person_form': person_form
        }
    )


def person_update_form(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person_form = PersonForm(data=request.POST, instance=person)
        if person_form.is_valid():
            person_form.save()
            return redirect('triangle:person_list')
    else:
        person_form = PersonForm(instance=person)
    return render(
        request,
        "triangle/person_update_form.html",
        {
            'person_form': person_form,
            'person': person,
        }
    )


class PersonIndexView(generic.ListView):
    template_name = 'triangle/person_list.html'
    context_object_name = 'person_list'

    def get_queryset(self):
        return Person.objects.all()
