# Generated by Django 4.1.7 on 2023-02-28 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('other', 'Разное'), ('smartphone', 'Смартфоны'), ('laptop', 'Ноутбуки'), ('refrigerator', 'Холодильники'), ('TV', 'Телевизоры')], default='other', max_length=20, verbose_name='Категория')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование продукта')),
                ('description', models.TextField(max_length=2000, verbose_name='Описание продукта')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Стоимость продукта')),
                ('photo', models.CharField(max_length=200, verbose_name='Изображение продукта')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('qty', models.PositiveSmallIntegerField(default=0, verbose_name='Остатки продукта')),
            ],
            options={
                'verbose_name': 'Товары',
                'verbose_name_plural': 'Товары',
                'ordering': ['category', 'title'],
            },
        ),
    ]
