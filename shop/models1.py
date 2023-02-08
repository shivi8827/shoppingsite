from django.db import models

# Create your models here.
class Product(models.Model):
    Product_id = models.AutoField
    Product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.Product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=300, default="")
    

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)       
    item_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=110)
    email = models.CharField(max_length=110)
    address = models.CharField(max_length=110)
    city = models.CharField(max_length=110)
    state = models.CharField(max_length=110)
    zip_code = models.CharField(max_length=110)
    phone = models.CharField(max_length=110)








class Customer(models.Model):
  
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    phone = models.CharField(max_length=110)
    email = models.CharField(max_length=110)
    password = models.CharField(max_length=110)

    

    @staticmethod
    def get(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email= self.email):
            return True
        return False    



