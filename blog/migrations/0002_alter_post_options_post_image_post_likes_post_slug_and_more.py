# Generated by Django 5.0.6 on 2024-08-01 10:20

import autoslug.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='default-slug', editable=False, populate_from='title', unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Technology', 'Technology'), ('Programming', 'Programming'), ('Cybersecurity', 'Cybersecurity'), ('Data Science', 'Data Science'), ('AI & ML', 'AI & ML'), ('Gadgets', 'Gadgets'), ('Software Development', 'Software Development'), ('Hardware', 'Hardware'), ('Networking', 'Networking'), ('Cloud Computing', 'Cloud Computing'), ('DevOps', 'DevOps')], max_length=100, unique=True),
        ),
    ]