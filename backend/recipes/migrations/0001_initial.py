# Generated by Django 2.2.19 on 2022-12-05 17:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название продукта')),
                ('measurement_unit', models.CharField(max_length=256, verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='QuantityOfIngredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Минимальное количество - 1')], verbose_name='Количество ингридиентов')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.Ingredient', verbose_name='Ингредиенты')),
            ],
            options={
                'verbose_name': 'Ингридиент',
                'verbose_name_plural': 'Количество ингридиентов',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Название тега')),
                ('color_code', models.CharField(max_length=6, unique=True, verbose_name='Цвет тега')),
                ('slug', models.SlugField(max_length=256, unique=True, verbose_name='Адрес тега')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='Автор на которого подписываются')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL, verbose_name='Подписчик')),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название блюда')),
                ('image', models.ImageField(upload_to='recipes/', verbose_name='Фотография блюда')),
                ('description', models.TextField(max_length=2000, verbose_name='Текстовое описание')),
                ('cooking_time', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Минимальное время приготовления - 1 минута')], verbose_name='Время приготовления(в минутах)')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Автор публикации')),
                ('favorite', models.ManyToManyField(related_name='favorites_recipes', to=settings.AUTH_USER_MODEL, verbose_name='Избранные рецепты')),
                ('ingredient', models.ManyToManyField(related_name='recipes', through='recipes.QuantityOfIngredients', to='recipes.Ingredient', verbose_name='Ингредиенты')),
                ('purchase', models.ManyToManyField(related_name='purchases', to=settings.AUTH_USER_MODEL, verbose_name='Список покупок')),
                ('tag', models.ManyToManyField(related_name='recipes', to='recipes.Tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
        migrations.AddField(
            model_name='quantityofingredients',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.Recipe', verbose_name='Рецепты'),
        ),
        migrations.AddConstraint(
            model_name='subscription',
            constraint=models.UniqueConstraint(fields=('user', 'author'), name='unique_object'),
        ),
        migrations.AddConstraint(
            model_name='quantityofingredients',
            constraint=models.UniqueConstraint(fields=('ingredient', 'recipe'), name='unique_object'),
        ),
    ]