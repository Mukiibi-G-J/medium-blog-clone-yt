from django import forms
from django.forms import TextInput, Textarea
from .models import Comments


class EmailPostForm(forms.Form):
    name =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'margin-bottom: 20px;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email',  'class': 'form-control', 'id':"InputEmail"}))
    to =forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email-to',  'class': 'form-control', 'id':"InputEmail"}))
    comment=forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder':'Comment here please...', 'class':'form-control'}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields =['name', 'email', 'body']
        widgets ={
        "name":TextInput(attrs={
            "class":"form-control",
            "placeholder":"Your name",
            "id":"InputName",
            "name":"InputName",
            "required":"required",


            }),

        "email":TextInput(attrs={
            'placeholder':'Email address',
            'name':'InputEmail',
            'id':"InputEmail",
            "class":"form-control",
            "required":"required"
            }),
        "body":Textarea(attrs={
            "name":"InputComment" ,
            "id":"InputComment" ,
            "class":"form-control" ,
            "rows":"4" ,
            "placeholder":"Your comment here..." ,
            "required":"required"
            })

        
        }
        

