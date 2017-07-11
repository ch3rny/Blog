from django import forms
from .models import Comment, User, UserProfile, Post, Category
from ckeditor.fields import RichTextFormField


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


class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text','category')
    #title = forms.CharField()
    #text = RichTextFormField()
    #cat = forms.ModelChoiceField(queryset=Category.objects.all().order_by('category'))
    #cat = forms.ChoiceField(choices=[(category.category, category.category) for category in category],
    #                           widget=forms.Select(),label='Category')