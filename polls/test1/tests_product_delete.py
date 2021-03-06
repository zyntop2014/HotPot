from django.test import TestCase

from polls.models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Introduction to computer system", price=100, description= "user1", username = "user1")
        Product.objects.create(name="Introduction to database", price=200, description= "user2",username = "user2")
        Product.objects.create(name="Introduction to algorithms", price=300, description= "user3", username = "user3")
        Product.objects.create(name="Introduction to computer science", price=400, description= "user4", username = "user4")
        Product.objects.create(name="Introduction to operating system", price=500, description= "user5", username = "user5")
        Product.objects.create(name="Introduction to computer network", price=600, description= "user6",username = "user6")
        Product.objects.create(name="Introduction to UI design", price=700, description= "user7", username = "user7")
        Product.objects.create(name="Introduction to machine learning", price=800, description= "user8", username = "user8")
        Product.objects.create(name="Introduction to software engineering", price=900, description= "user9", username = "user9")
        Product.objects.create(name="Introduction to data science", price=1000, description= "user10", username = "user10")
        

    def test_delete_product1 (self):
        w = Product.objects.get(name= "Introduction to computer system")    
        self.assertTrue(isinstance(w, Product))
        Product.deleteProduct(name = w.name, username = w.username)
        self.assertFalse(Product.objects.filter(name = "Introduction to computer system").exists())


    def test_delete_product2 (self):
        w = Product.objects.get(name= "Introduction to database")    
        self.assertTrue(isinstance(w, Product))
        Product.deleteProduct(name = w.name, username = w.username)
        self.assertFalse(Product.objects.filter(name = "Introduction to database").exists())


    def test_delete_product3 (self):
        w = Product.objects.get(name= "Introduction to algorithms")    
        self.assertTrue(isinstance(w, Product))
        Product.deleteProduct(name = w.name, username = w.username)
        self.assertFalse(Product.objects.filter(name = "Introduction to algorithms").exists())

    def test_delete_product4 (self):
        w = Product.objects.get(name= "Introduction to computer science")    
        self.assertTrue(isinstance(w, Product))
        Product.deleteProduct(name = w.name, username = w.username)
        self.assertFalse(Product.objects.filter(name = "Introduction to computer science").exists())

    def test_delete_product5 (self):
        w = Product.objects.get(name= "Introduction to operating system")    
        self.assertTrue(isinstance(w, Product))
        Product.deleteProduct(name = w.name, username = w.username)
        self.assertFalse(Product.objects.filter(name = "Introduction to operating system").exists())


    def test_delete_product6 (self):
        w = Product.objects.get(name= "Introduction to computer network")    
        self.assertTrue(isinstance(w, Product))
        Product.deleteProduct(name = w.name, username = w.username)
        self.assertFalse(Product.objects.filter(name = "Introduction to computer network").exists())

    def test_delete_product7 (self):
        w = Product.objects.get(name= "Introduction to UI design")    
        self.assertTrue(isinstance(w, Product))
        Product.deleteProduct(name = w.name, username = w.username)
        self.assertFalse(Product.objects.filter(name = "Introduction to UI design").exists())


    def test_delete_product8 (self):
        w = Product.objects.get(name= "Introduction to machine learning")    
        self.assertTrue(isinstance(w, Product))
        Product.deleteProduct(name = w.name, username = w.username)
        self.assertFalse(Product.objects.filter(name = "Introduction to machine learning").exists())

    def test_delete_product9 (self):
        w = Product.objects.get(name= "Introduction to software engineering")    
        self.assertTrue(isinstance(w, Product))
        Product.deleteProduct(name = w.name, username = w.username)
        self.assertFalse(Product.objects.filter(name = "Introduction to software engineering").exists())

    def test_delete_product10 (self):
        w = Product.objects.get(name= "Introduction to data science")    
        self.assertTrue(isinstance(w, Product))
        Product.deleteProduct(name = w.name, username = w.username)
        self.assertFalse(Product.objects.filter(name = "Introduction to data science").exists())

   
