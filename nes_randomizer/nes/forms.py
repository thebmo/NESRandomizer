from django import forms

class GameForm(forms.Form):
    selections = ('all', 'pick')