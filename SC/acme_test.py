import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        prod2 = Product('Test Product No 2')
        self.assertEqual(prod.weight, 20)

    def test_methods(self):
        prod3 = Product('Test Product No 3', price=int(20), weight=int(30), 
        flammability=float(0.8))
        self.assertEqual(prod3.stealability(), 'Kinda stealable')


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        self.assertEqual(len(generate_products(num_products=30)), 30)

    def test_legal_names(self):
        self.assertIn(any('ADJECTIVES') + any('NOUNS'), generate_products(num_products=30))

if __name__ == '__main__':
    unittest.main()