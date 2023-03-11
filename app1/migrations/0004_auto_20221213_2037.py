# Generated by Django 3.2 on 2022-12-13 15:07

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20221212_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('adr', models.CharField(max_length=500)),
                ('est_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'college',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dept_str', models.IntegerField()),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.college')),
            ],
            options={
                'db_table': 'dept',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('marks', models.IntegerField()),
                ('age', models.IntegerField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.department')),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.AlterModelManagers(
            name='person',
            managers=[
                ('activep', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_practical', models.BooleanField(default=False)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.department')),
                ('student', models.ManyToManyField(to='app1.Student')),
            ],
            options={
                'db_table': 'subject',
            },
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('exp', models.FloatField()),
                ('qual', models.CharField(max_length=50)),
                ('college', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.college')),
            ],
            options={
                'db_table': 'principal',
            },
        ),
    ]