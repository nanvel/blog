labels: Blog
        Django
        Server
created: 2012-12-12T00:00
place: Alchevs'k, Ukraine
comments: true

# Exim mail server installation

![Exim mail server](exim.png)

```bash
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install exim4-daemon-light mailutils

$ sudo dpkg-reconfigure exim4-config

General type of mail configuration: internet site ...
System mail name: site name (e.g. nanvel.name)
IP-addresses to listen ...: 127.0.0.1
Other destinations for which mail is accepted: site.name; localhost
Domains to relay mail for: [blank]
Machines to relay mail for: [blank]
Keep number of DNS-queries ...: No
Delivery mail for local mail: Maildir format in home directory
Split configuration into small files?: No
```

Test send email:
```bash
echo "This is a test." | mail -s Testing someone@somedomain.com
```

Send email in django code:
```python
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_mail(template, context, emails, from_email=None):
    if not from_email:
        from_email = settings.DEFAULT_FROM_EMAIL
    txt_content = render_to_string('{template}.txt'.format(template=template), context)
    html_content = render_to_string('{template}.html'.format(template=template), context)
    subject = render_to_string('{template}_subject.txt'.format(template=template), context)
    subject = ' '.join(subject.split('\n'))
    msg = EmailMultiAlternatives(subject, txt_content, from_email, emails)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

    # send_mail('some_template', context, ['mail@mail.com'])
```

You need to add 3 templates:

- my_template.txt
- my_template.html
- my_template_subject.txt

Links:

- [http://library.linode.com/email/exim/send-only-mta-debian-6-squeeze](http://library.linode.com/email/exim/send-only-mta-debian-6-squeeze)
- [http://www.exim.org/](http://www.exim.org/)
