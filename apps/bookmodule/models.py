from django.db import models
#lab8
class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)

class Address(models.Model):
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.city

# class Student(models.Model):
#     name = models.CharField(max_length=255)
#     age = models.IntegerField()
#     address = models.ForeignKey(Address, on_delete=models.CASCADE)  # ForeignKey إلى Address

#     def __str__(self):
#         return self.name
    
#lab9
# from django.db import models

# class Book(models.Model):
#     title = models.CharField(max_length=50)
#     author = models.CharField(max_length=50)
#     price = models.FloatField(default=0.0)
#     edition = models.SmallIntegerField(default=1)

# class Address(models.Model):
#     city = models.CharField(max_length=100)

#     def __str__(self):
#         return self.city

# class Card(models.Model):
#     card_number = models.IntegerField(unique=True)

#     def __str__(self):
#         return str(self.card_number)
    
# class Department(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
    
# class Course(models.Model):
#     title = models.CharField(max_length=100)
#     code = models.IntegerField()

#     def __str__(self):
#         return f"{self.title} ({self.code})"
    
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     address = models.ForeignKey(Address, on_delete=models.CASCADE)
#     card = models.OneToOneField(Card, on_delete=models.PROTECT, null=True, blank=True)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
#     course = models.ManyToManyField(Course)

#     def __str__(self):
#         return self.name
    


# lab11
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.city}"

class Card(models.Model):
    card_number = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.card_number)
    
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.code})"
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Address2(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}"

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address2)

    def __str__(self):
        return self.name
    
class BookCover(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='book_covers/')

    def __str__(self):
        return self.title