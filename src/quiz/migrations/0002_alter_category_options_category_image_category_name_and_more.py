# Generated by Django 5.0.4 on 2024-05-10 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AddField(
            model_name="category",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/category/covers"
            ),
        ),
        migrations.AddField(
            model_name="category",
            name="name",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="choice",
            name="is_correct",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="choice",
            name="text",
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="question",
            name="order_number",
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="question",
            name="text",
            field=models.CharField(default=1, max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="quiz",
            name="description",
            field=models.TextField(blank=True, max_length=1025, null=True),
        ),
        migrations.AddField(
            model_name="quiz",
            name="image",
            field=models.ImageField(
                default="default.png", upload_to="media/quiz/covers"
            ),
        ),
        migrations.AddField(
            model_name="quiz",
            name="level",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Basic"), (1, "Medium"), (2, "Advanced")], default=0
            ),
        ),
        migrations.AddField(
            model_name="quiz",
            name="title",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="result",
            name="count_of_correct_answers",
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
