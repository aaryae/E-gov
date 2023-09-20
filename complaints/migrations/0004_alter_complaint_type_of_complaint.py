# Generated by Django 4.2.5 on 2023-09-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0003_complaint_action_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='type_of_complaint',
            field=models.CharField(choices=[('Traffic Violation', 'Traffic Violation'), ('Delayed Services', 'Delayed Services'), ('Service Quality', 'Service Quality'), ('Service Denial', 'Service Denial'), ('Missuse of Funds', 'Missuse of Funds'), ('Road and Transportatoin Issues', 'Road and Transportation Issues'), ('Healthcare Services', 'Healthcare Services'), ('Misconduct Allegations', 'Misconduct Allegations'), ('Abuse of Power', 'Abuse of Power'), ('Other', 'Other')], max_length=100),
        ),
    ]
