# Generated by Django 3.1.3 on 2020-12-30 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0003_auto_20201222_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(choices=[('btch', 'B.TECH'), ('mtech', 'M.TCH'), ('mca', 'MCA'), ('bca', 'BCA')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='coursename',
            field=models.CharField(choices=[('btch', 'B.TECH'), ('mtech', 'M.TCH'), ('mca', 'MCA'), ('bca', 'BCA')], max_length=20),
        ),
    ]
