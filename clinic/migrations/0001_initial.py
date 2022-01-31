# Generated by Django 3.2.5 on 2022-01-28 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('contactnumber', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('prescription', models.CharField(max_length=200, null=True)),
                ('position', models.CharField(max_length=200, null=True)),
                ('dateOFBirth', models.CharField(default='none', max_length=200)),
                ('bill', models.IntegerField(null=True)),
            ],
        ),
    ]