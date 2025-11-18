from django import forms
from .models import CommunityPost

class CommunityPostForm(forms.ModelForm):
    class Meta:
        model = CommunityPost
        fields = ['name', 'title', 'content', 'high_salinity_solution']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name (optional)'}),
            'title': forms.TextInput(attrs={'placeholder': 'Post title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Share your experience, soil/crop data, or solution...','rows':4}),
        }
