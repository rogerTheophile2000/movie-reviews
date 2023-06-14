from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs) 
        
        self.fields['headline'].widget.attrs.update(
            {'class': 'form-control'})
        
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control'})
        
        self.fields['date'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'date',
            }
        )

      
    class Meta:
        model = News
        fields = ['headline','body','date']
            
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4}),
            'date': forms.DateInput(
                attrs={
                    'type':'date'
                }
            )
        }