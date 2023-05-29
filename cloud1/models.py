from django.db import models


# Create your models here.
service_choices = [
        (' Cloud Solutions', ' Cloud Solutions'),
        ('Consulting', 'Consulting'),
        ('Data Analytics', 'Data Analytics'),
        ('Graphic Design', 'Graphic Design'),
        ('Maintenance/Support', 'Maintenance/Support'),
        ('Mobile App Development', 'Mobile App Development'),
        ('Other', 'Other'),
        ('SEO', 'SEO'),
        ('Social Media', 'Social Media'),
        ('Software Development', 'Software Development'),
        ('Software Testing', 'Software Testing'),
        ('UI/UX Design', 'UI/UX Design'),
        ('Website Development', 'Website Development'),
    ]

class Contact(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    service = models.CharField(max_length=100, choices=service_choices, null=False, blank=False, verbose_name="Select A Service Type")
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name


class Email(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True, blank=True, related_name='emails')
    mail = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
