from django import forms
from .models import Sample


class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample  # 사용할 모델
        fields = ['title', 'content']  # SampleForm에서 사용할 Sample 모델의 속성
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10})
        }
        labels = {
            'title': '제목',
            'content': '내용'
        }
