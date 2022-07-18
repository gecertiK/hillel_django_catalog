from django.urls import path

from triangle.views import PersonIndexView, get_form, person_create_form, person_update_form, first_page

app_name = 'triangle'
urlpatterns = [
    path('', get_form, name='triangle'),
    path('first-page/', first_page, name='first_page'),
    path('person-list/', PersonIndexView.as_view(), name='person_list'),
    path('person/', person_create_form, name='person_create_form'),
    path('person/<int:pk>/', person_update_form, name='person_update_form'),
]

