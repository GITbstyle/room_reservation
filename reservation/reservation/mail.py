from django.core.mail import EmailMessage

email = EmailMessage('Armagedon', 'Nastąpił.\n\nZlecenie zostało wykonane.', to=['karol.janus@gmail.com'])
email.send()
