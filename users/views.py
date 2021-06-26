from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import RedirectView, FormView
from django.http import HttpResponseRedirect, request

from users.forms import SortUserForm


class SortUserFormView(FormView):
    form_class = SortUserForm
    template_name = 'input_form.html'


    def get_success_url(self):
        form = self.request.POST
        age = form.get('age')
        gender = form.get('gender')
        english_level = form.get('english_level')
        if (gender == 'MALE' and age > str(20) and english_level >= str(4)) or (gender == 'FEMALE' and age > str(22) and english_level >= str(3)):
            return self.success_url
        else:
            self.success_url = 'reject.html'
            return self.success_url

