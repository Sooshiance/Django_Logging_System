from django.test import TestCase

from product.models import Product


class TestModel(TestCase):
    def setUp(self) -> None:
        self.prod = Product.objects.create(title='TShirt', price=12, description='This is XL TShirt')
        return super().setUp()
    
    def test_readDataBase(self):
        p = Product.objects.all()
        self.assertEqual(p.count(), 1)
    
    def test_createData(self):
        obj = Product.objects.create(title='Jeans', price=12, description='This is XL Jeans')
        p = Product.objects.all()
        self.assertEqual(p.count(), 2)
    
    def test_UpdateElement(self):
        pass

    def test_DeleteElement(self):
        pass
