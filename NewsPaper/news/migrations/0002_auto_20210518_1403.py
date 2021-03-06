# Generated by Django 3.2.3 on 2021-05-18 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='post_name',
        ),
        migrations.AddField(
            model_name='author',
            name='author',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='rating_auth',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating_comm',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating_post',
            field=models.IntegerField(default=0),
        ),
    ]
