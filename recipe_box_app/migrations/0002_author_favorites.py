# Generated by Django 3.1.1 on 2020-09-10 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_box_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorite_recipes', to='recipe_box_app.Recipe'),
        ),
    ]