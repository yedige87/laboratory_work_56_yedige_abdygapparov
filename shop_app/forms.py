from django.forms import ModelForm

from shop_app.models import Product


# Create the form class.
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'photo', 'qty', 'category']
        labels = {
            'title': 'Наименование',
            'description': 'Описание',
            'price': 'Стоимость',
            'photo': 'Изображение',
            'qty': 'Остатки',
            'category': 'Категория'
        }