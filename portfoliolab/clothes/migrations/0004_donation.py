# Generated by Django 3.0.6 on 2021-10-21 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clothes', '0003_institution_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=9)),
                ('city', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=5)),
                ('pick_up_date', models.DateField(auto_now_add=True)),
                ('pick_up_time', models.TimeField(auto_now_add=True)),
                ('pick_up_comment', models.TextField(max_length=1024)),
                ('categories', models.ManyToManyField(to='clothes.Category')),
                ('institution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clothes.Institution')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]