# Generated by Django 3.1.7 on 2021-06-17 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smiley', '0002_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='profileimg',
            new_name='impf',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='@gmail.com', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
