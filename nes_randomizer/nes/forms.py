from django import forms

class GameForm(forms.Form):
    selectios = ('all', 'pick')