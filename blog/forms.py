from django import forms
from .models import Comment, User, UserProfile


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class EditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

class EditUserPic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_image',)