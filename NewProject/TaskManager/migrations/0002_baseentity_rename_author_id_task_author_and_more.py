# Generated by Django 5.1.4 on 2025-01-29 11:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("TaskManager", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BaseEntity",
            fields=[
                (
                    "id",
                    models.CharField(
                        editable=False,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name="task",
            old_name="author_id",
            new_name="author",
        ),
        migrations.RemoveField(
            model_name="project",
            name="id",
        ),
        migrations.RemoveField(
            model_name="task",
            name="id",
        ),
        migrations.AddField(
            model_name="project",
            name="baseentity_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to="TaskManager.baseentity",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="task",
            name="baseentity_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to="TaskManager.baseentity",
            ),
            preserve_default=False,
        ),
    ]
