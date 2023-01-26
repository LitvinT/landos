from django.forms import EmailField, EmailInput, Form, TextInput, Textarea, CharField, ModelForm
from .models import Contact


class ContactForm(ModelForm):
    name = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Name'
            }
        ),
        max_length=64
    )

    email = EmailField(
        widget=EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Email'
            }
        )
    )

    message = CharField(
        widget=Textarea(
            attrs={
                'class': 'form-control',
                'id': 'message',
                'style': 'height: 12rem',
                'placeholder': 'Message'
            }
        ),
        max_length=1024
    )

    subject = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'id': 'subject',
                'placeholder': 'Subject'
            }
        )
    )

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message', 'subject')



