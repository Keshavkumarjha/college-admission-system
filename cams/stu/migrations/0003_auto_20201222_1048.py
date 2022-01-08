# Generated by Django 3.1.3 on 2020-12-22 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0002_auto_20201221_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_docoments',
            fields=[
                ('docsid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='stu.student')),
                ('photo', models.ImageField(upload_to='myimage/image')),
                ('sign', models.ImageField(upload_to='myimage/sign')),
                ('marksheet_10', models.FileField(null=True, upload_to='document_10')),
                ('marksheet_12', models.FileField(null=True, upload_to='document_12')),
                ('marksseet_graduation', models.FileField(null=True, upload_to='graduation_docs')),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='student',
            name='sign',
        ),
        migrations.AlterField(
            model_name='student_status',
            name='status',
            field=models.CharField(choices=[('pending', 'PENDING'), ('rejected', 'REJECTED'), ('selected', 'SELECTED')], max_length=300),
        ),
        migrations.AlterField(
            model_name='student_status',
            name='statusid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='stu.student'),
        ),
    ]
