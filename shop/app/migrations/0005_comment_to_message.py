# Generated by Django 3.1.5 on 2021-01-21 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='to_message',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.comment'),
        ),
    ]