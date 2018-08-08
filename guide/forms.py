from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    sex = forms.ChoiceField(
        choices=[('M', 'Male'), ('F', 'Female')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    weight = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    height = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Profile
        fields = ('sex', 'date_of_birth', 'weight', 'height',)
