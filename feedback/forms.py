from feedback.models import Review
from django import forms

class AddReview(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('author','mail','theme','text','attachment',)