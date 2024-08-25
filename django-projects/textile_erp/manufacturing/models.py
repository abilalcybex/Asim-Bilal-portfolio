from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_information = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.quantity} in stock"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact_information = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.product.name} for {self.customer.name}"

class Production(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    production_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Production {self.id} - {self.product.name}"
