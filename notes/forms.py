from django import forms
from .models import Note
class AddNoteForm(forms.Form):

    COLOR_CHOISES = (
    ('teal', 'Teal'),
    ('grey lighten-2', 'Grey'),
    ('red lighten-1', 'Red'),
    )

    class Meta:
        model= Note
        fields = ('title', 'note', 'color')
        # widgets = {
        #     'color': forms.Select(attrs={})
        # }


    # title = forms.CharField(max_length=500, label='Title')
    # note = forms.Textarea()
    # colors = (('teal', 'Teal'),
    #  ('red lighten-1', 'Red'),
    #  ('grey lighten-2', 'Grey'))
    # color = forms.ChoiceField(choices=colors, required=True, initial='grey lighten-2')

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=500)