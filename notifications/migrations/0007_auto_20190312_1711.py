# Generated by Django 2.1.7 on 2019-03-12 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('notifications', '0006_indexes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='recipient',
        ),
        migrations.AddField(
            model_name='notification',
            name='recipient_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='notification',
            name='recipient_object_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
