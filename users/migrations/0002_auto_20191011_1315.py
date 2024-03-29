# Generated by Django 2.2.6 on 2019-10-11 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20191006_1759'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=6),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='occupation',
            field=models.CharField(choices=[('Developer', 'Developer'), ('Artist', 'Artist'), ('Gamer', 'Gamer'), ('Movie Buff', 'Movie Buff'), ('Student', 'Student'), ('Normal User', 'Normal User')], default='Normal User', max_length=20),
        ),
        migrations.CreateModel(
            name='InAppSearchHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
