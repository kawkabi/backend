# Generated by Django 4.2.13 on 2024-06-09 09:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_auth_method_remove_user_creationdate_and_more'),
        ('quiz', '0002_adminfinalanswer_adminmultiplechoiceanswer_h1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedQuestion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('creationDate', models.DateTimeField(auto_now=True, null=True)),
                ('question', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.question')),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('solved', models.BooleanField(blank=True, default=False)),
                ('question', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.question')),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user')),
            ],
        ),
    ]
