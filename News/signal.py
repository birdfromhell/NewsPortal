from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Subscriber
from .models import Posts


@receiver(post_save, sender=Posts)
def send_email_on_new_post(sender, instance, created, **kwargs):
    if created:
        # Ambil semua user yang terdaftar
        users = Subscriber.objects.all()
        # Looping untuk setiap user
        for user in users:
            # Kirim email ke user
            send_mail(
                'Postingan Baru',
                'Halo, ada postingan baru di website kami. Silakan kunjungi website untuk melihat postingan terbaru.',
                'admin@website.com',
                [user.email],
                fail_silently=False,
            )
