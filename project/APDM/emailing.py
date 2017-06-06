# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models import signals
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

def welcome_new_user(sender, instance, created, **kwargs):
    '''Welcome the new client by sending him an email.'''
    if created:
        print "created a new user"
        subject = 'Bienvenue à la plateforme APDM'
        message = 'Bonjour cher client '+instance.username+' \nVous pouvez désormais vous connecter à la plateforme APDM en utilisant les informations de connexion suivantes : \nNom d\'utilisateur : '+ instance.username+'\nMot de passe : aitech'+instance.username+'\n\n Accéder à la plateforme à partir du lien suivant : http://localhost:4200/login'
        from_addr = 'no-reply@example.com'
        recipient_list = (instance.email,)
        send_mail(subject, message, from_addr, recipient_list,fail_silently=False)
        # subject, from_email, to = 'Bienvenue à la plateforme APDM', 'no-reply@example.com', instance.email
        # text_content = 'This is an important message.'
        # html_content = '<p>This is an <strong>important</strong> message.</p>'
        # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        # msg.attach_alternative(html_content, "text/html")
        # msg.send()
