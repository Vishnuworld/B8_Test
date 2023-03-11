from django.db import models

# Create your models here.
# ORM -- Object Relational Mapper

class ActivePersons(models.Manager): # Custom Model Manager
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True) # Model.objects.all()

# Define class for InActivePersons

class Person(models.Model): # Table # app1_person
    # default id
    name = models.CharField(max_length=200) # db_column="nm"
    age = models.IntegerField()
    mobile_num = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    date_joined = models.DateTimeField(auto_now=True, null=True)
    date_updated = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)
    activep = ActivePersons()
    objects = models.Manager()  # objects

    class Meta:
        db_table = "person"

    def __str__(self):
        return f"{self.name} -- {self.address}"

    def show_details(self):
        print(f"""-----------------------------------
Person Name:- {self.name}
Person Age:- {self.age}
Person Mobile:- {self.mobile_num}
Person Address:- {self.address}""")

    @classmethod
    def get_data_above_age(cls):   
        return cls.objects.filter(age__gte=25) # gt, gte, lt, lte, startswith, endswith

    @classmethod
    def get_avg_age(cls):
        '''average age of all persons'''
        data = cls.objects.all().values("id", "name", "age")
        lst = list(map(lambda x: x['age'], list(data)))
        return sum(lst)//len(lst)  

    @classmethod
    def get_active_data(cls):
        return cls.objects.filter(is_active=True)

    # define method for inactive

# startproject, startapp, runserver, makemigrations, 

# class User(models.Model):
    # first_name = 
    # email_id = 
    # is_active = 

class CommonClass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class College(CommonClass):
    adr = models.CharField(max_length=500)
    est_date = models.DateField(auto_now=True)

    class Meta:
        db_table = "college"

class Principal(CommonClass):
    exp = models.FloatField()
    qual = models.CharField(max_length=50)
    college = models.OneToOneField(College, on_delete=models.CASCADE, related_name="princi")

    class Meta:
        db_table = "principal"

class Department(CommonClass): # small letters
    dept_str = models.IntegerField()
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="depts")  # OneToManyField

    class Meta:
        db_table = "dept"
        # unique_together = (("name", "college"),)

class Student(CommonClass):
    marks = models.IntegerField()
    age = models.IntegerField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="studs", null=True) #  OneToManyField

    class Meta:
        db_table = "student"  

class Subject(CommonClass):
    is_practical = models.BooleanField(default=False)
    student = models.ManyToManyField(Student, related_name="subjs")
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="subjs")

    class Meta:
        db_table = "subject"


# get models from database
# ERD -- Entity Relationship Diagram

# https://www.javatpoint.com/composite-key-in-dbms

# ------------------------------------------------------------------------
# from django.db import models


class FuelType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class CarModel(models.Model):
    name = models.CharField(max_length=255)
    fueltype = models.ManyToManyField(FuelType, related_name='carmodels')

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
