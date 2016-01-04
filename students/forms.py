from django import forms

from exams.models import Subject

class MarkForm(forms.Form):
    subject = forms.ModelChoiceField(queryset=Subject.objects, to_field_name="id", widget=forms.Select(attrs={'class':'ui search dropdown',}))
    mark = forms.IntegerField(label='Mark', min_value=0, max_value=20)
    count = forms.BooleanField(label='CountInAverage',required=False, initial=True)
    comment = forms.CharField(label='Comment', widget=forms.TextInput(attrs={'placeholder':'Comment',}))