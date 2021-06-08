from django.core.mail import send_mail

send_mail(
    'Subject',
    'Message.',
    'from@example.com',
    ['john@example.com', 'jane@example.com'],
    fail_silently=False,
)