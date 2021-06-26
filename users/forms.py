from django.forms import ModelForm

from users.models import SortUser


class SortUserForm(ModelForm):
    class Meta:
        model = SortUser
        fields = ['gender', 'age', 'english_level']
