# Generated by Django 4.0.3 on 2022-04-18 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FileField(upload_to='user_<django.db.models.fields.AutoField>/<function user_directory_path at 0x0000027CAD647AC0>'),
        ),
    ]
