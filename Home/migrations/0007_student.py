# Generated by Django 3.2.9 on 2021-12-27 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Home', '0006_rename_enroll_datasheet_frontimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('branch', models.CharField(choices=[('CIVIENG', 'CIVIENG'), ('COMPENG', 'COMPENG'), ('ECIENG', 'ECIENG'), ('ECTELEG', 'ECTELEG'), ('ITENG', 'ITENG'), ('MECHENG', 'MECHENG')], max_length=100)),
                ('course', models.CharField(choices=[('BTECH', 'BTECH'), ('MTECH', 'MTECH')], max_length=100)),
                ('Reg_no', models.CharField(max_length=10, unique=True)),
                ('roll_no', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('session', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]