
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponseRedirect

from school_bg.core.email_utils import send_email_with_template

from django.contrib.auth import logout
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver

UserModel = get_user_model()


@receiver(user_logged_out)
def handle_user_logout(sender, request, user, **kwargs):
    # Check if the logout was triggered after a password change
    if request.session.get('password_changed', False):
        # logout(request)  # Log out the user
        del request.session['password_changed']  # Remove the session variable



def send_successful_registration_email(user):
    context = {
        'user': user,
    }
    send_email_with_template(
        subject='Registration greetings',
        template_name='emails/email_greeting.html',
        context=context,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(user.email,)
    )


@receiver(post_save, sender=UserModel)
def user_created(instance, created, **kwargs):
    if created:
        send_successful_registration_email(instance)
