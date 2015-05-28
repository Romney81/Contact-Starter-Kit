from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
import django.contrib.auth
import homepage.models as hmod
from django.core import validators
from django.core.validators import validate_email
from django.forms import fields, util
from django.core import exceptions
from django.core.mail import send_mail, EmailMessage
from django_mako_plus.controller.router import MakoTemplateRenderer, get_renderer
from django_mako_plus.controller import view_function
from django.template.loader import render_to_string, get_template
import hashlib, datetime, random
from django.template import Context

templater = get_renderer('homepage')

@view_function
def process_request(request):
    params = {}
    form_errors = []

    errors = 'true'
    form = ContactUsForm()
    # if request.method == 'POST':
    #     form = ContactUsForm(request.POST)
    #     if form.is_valid():
    #
    #         #get information from the form for the email
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         message = form.cleaned_data['message']
    #
    #         #send email
    #         subject = "Hi there!"
    #         from_email = 'From:' + email
    #         to = ['scott@getlured.com']
    #         msg = EmailMessage(subject, message, to = to, from_email = from_email )
    #         msg.send()
    #
    #         #redirects back to the contact page.
    #         return HttpResponseRedirect('/contact/')

    params['form'] = form
    params['errors'] = errors
    params['form_errors'] = form_errors

    return templater.render_to_response(request, 'contact.html', params)

@view_function
def contactForm(request):
    params = {}
    form_errors = []

    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():

            #get information from the form for the email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            #send email
            subject = "Hi there!"
            from_email = 'From:' + email
            to = ['scott@getlured.com']
            msg = EmailMessage(subject, message, to = to, from_email = from_email )
            msg.send()
            errors = 'false'
            form = ContactUsForm()
            #return HttpResponseRedirect('/contact/')
        else:
            errors = 'true'

            for v in form.errors.values():
                form_errors.append(v[0])

    params['form'] = form
    params['errors'] = errors
    params['form_errors'] = form_errors

    return templater.render_to_response(request, 'contact.contactForm.html', params)


class ContactUsForm(forms.Form):

    email_errors = {

        'required': 'It looks like you forgot to enter your email.',
        'invalid': 'That doesn\'t look like a valid email.',
    }
    name_errors = {

        'required': 'We need your name!',
    }
    message_errors = {

        'required': 'We need a message!',
    }

    name = forms.CharField(error_messages=name_errors, required = True, widget = forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Name', 'id': 'name', 'name': 'Name'}))
    email = forms.EmailField(error_messages=email_errors, required=True, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Email', 'id': 'email', 'name': 'Email'}))
    message = forms.CharField(error_messages=message_errors, required = True, widget = forms.Textarea(attrs={'class': 'form-control input-lg', 'placeholder': 'Message', 'name': 'Message'}))
