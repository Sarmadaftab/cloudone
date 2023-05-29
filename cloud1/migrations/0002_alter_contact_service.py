# Generated by Django 4.2.1 on 2023-05-26 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='service',
            field=models.CharField(choices=[(' Cloud Solutions', ' Cloud Solutions'), ('Consulting', 'Consulting'), ('Data Analytics', 'Data Analytics'), ('Graphic Design', 'Graphic Design'), ('Maintenance/Support', 'Maintenance/Support'), ('Mobile App Development', 'Mobile App Development'), ('Other', 'Other'), ('SEO', 'SEO'), ('Social Media', 'Social Media'), ('Software Development', 'Software Development'), ('Software Testing', 'Software Testing'), ('UI/UX Design', 'UI/UX Design'), ('Website Development', 'Website Development')], max_length=100),
        ),
    ]
