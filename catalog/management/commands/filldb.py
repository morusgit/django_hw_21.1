from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories_list = [
            {'name': 'Лицензии', 'description': 'Необходимое разрешение для работы такси.'},
            {'name': 'Автомобили',
             'description': 'Автотранспорт имеющий необходимое разрешение для работы такси.'},
            {'name': 'Водители', 'description': 'Водители имеющие необходимое разрешение для работы такси.'},
        ]

        product_list = [
            {'name': 'Uber',
             'description': 'Лицензия для работы такси на автомобиле по региону Андалуссия',
             'category_id': 1,
             'price': '90000'},
            {'name': 'Bolt', 'description': 'Лицензия для работы такси на автомобиле по определённому региону.', 'category_id': 1,
             'price': '85000'},
            {'name': 'Модели Volkswagen Transporter T6, Минивэн',
             'description': 'Volkswagen Transporter T6 – минивэн M-класса, передний и полный привод. Механика и робот. Дизельные и бензиновые двигатели мощностью от 84 до 204 лошадиных сил.',
             'category_id': 2, 'price': '48000'},
            {'name': 'Модели Volkswagen Transporter T6, Минивэн Long', 'description': 'Volkswagen Transporter T6 – минивэн long M-класса, передний и полный привод. Механика и робот. Дизельные и бензиновые двигатели мощностью от 84 до 204 лошадиных сил.', 'category_id': 2,
             'price': '45000'},
            {'name': 'Juan Ermosa',
             'description': 'Возраст 38 лет. Стаж 12 лет.', 'category_id': 3,
             'price': '1280'},
            {'name': 'Jose Gonsales',
             'description': 'Возраст 32 года. Стаж 10 лет.', 'category_id': 3,
             'price': '1300'}
        ]

        for model in (Product, Category):
            model.objects.all().delete()
            table_name = model._meta.db_table

            # сбрасываем счетчик
            with connection.cursor() as cursor:
                query = f"SELECT setval(pg_get_serial_sequence('{table_name}', 'id'), 1, false);"
                cursor.execute(query)

        category_for_create = []
        for category_item in categories_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)

        products_for_create = []
        for product_item in product_list:
            products_for_create.append(Product(**product_item))

        Product.objects.bulk_create(products_for_create)