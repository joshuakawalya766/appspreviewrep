from django.db import models
from PIL import Image
from datetime import date
from django.utils import timezone
from django.conf import settings
import os
# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='House')
    """docstring for Post."""

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 800 or img.width > 800:
            output_size = (800, 800)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


# ---------------Extars----------------------------------


class Person(models.Model):
    # myid=
    nin=models.CharField(max_length=20,primary_key=True)
    fname = models.CharField(max_length=60, error_messages={'blank':'can no be blank. fill it now!'} )
    lname = models.CharField(max_length=60, help_text='Its like a family name' )
    # fullname = str(models.Index(fields=['lname', 'fname'])) #????
    age=models.IntegerField()
    email=models.EmailField()
    afile = models.FileField(upload_to='Files/%Y/%m/%d/', max_length=100)
    # afilepath=models.FilePathField(match='*.txt' ,path=os.path.join(settings.BASE_DIR,'media'))
    # height_field=500, width_field=500, ?????????
    profile = models.ImageField(upload_to='ProfilePics/', default='default.jpg')
    ShirtSize = models.TextChoices('ShirtSize', 'SMALL MEDIUM LARGE')  # Choises declarration
    size = models.CharField(verbose_name="body size", choices=ShirtSize.choices, max_length=10, blank=True)  # choices usage
    height=models.IntegerField()
    salary=models.IntegerField()
    etime=models.DateField(default=date.today)
    etzone=models.DateTimeField(default=timezone.now)
    fazno=models.DecimalField(max_digits=5,decimal_places=2)
    ipadd = models.GenericIPAddressField(default='::ffff:10.10.10.10',protocol='both',unpack_ipv4='True')

    @property
    def fullname(self):
        "Returns the person's full name."
        return '%s %s' % (self.fname, self.lname)
    
    def __str__(self):
        return self.fullname

# Getting IP address
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        ordering=['?','height']#- or ? for randomly on just blank ??????????
        # ordering=['?','nin']
        # ordering = ['-pub_date', 'author']
        # from django.db.models import F
        # ordering = [F('author').asc(nulls_last=True)]
        # permitions = [('can_deliver_pizzas', 'Can deliver pizzas')] #?????
        # permitions = [(permission_code, human_readable_permission_name)]
        indexes = [
            # models.Index(F('salary') * 0.1 , name='tax_idx'), #????
            models.Index(fields=['lname', 'fname']),
            models.Index(fields=['fname'], name='fname_idx'),
        ]
        constraints = [
            models.CheckConstraint(check=models.Q(
                age__gte=18), name='age_gte_18'),
        ]
        

        
    

class Group(models.Model):
    name = models.CharField(max_length=128)
    models.ManyToManyField("Person", through='Membership')
    def __str__(self):
        return self.name
class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return 'Group: %s Name: %s Reason: %s' % (self.group, self.person, self.invite_reason)
    

# ----------------------------------------
class Question(models.Model):
    text = models.TextField()
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    class Meta:
        order_with_respect_to = 'question'


# question = Question.objects.get(id=1)
# question.get_answer_order()[1, 2, 3]
# question.set_answer_order([3, 1, 2])
# answer = Answer.objects.get(id=2)
# answer.get_next_in_order()<Answer: 3 >
# answer.get_previous_in_order()<Answer: 1>
# --------------------------------------------------
class Manufacturer(models.Model):
    maname=models.CharField(max_length=50)
class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE) #many to one relationship


class Topping(models.Model):
    topname=models.CharField(max_length=50)
    topingredients = models.TextChoices('topingredients','meat veg grass')
    ingredientschoice = models.CharField(choices=topingredients.choices,max_length=10 ,blank=True)
class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)#many topping type on same pizza


class Card(models.Model):

    class Suit(models.IntegerChoices):
        DIAMOND = 1
        SPADE = 2
        HEART = 3
        CLUB = 4

    suit = models.IntegerField(choices=Suit.choices)


# -------------------Saving----------------------------------
# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()

#     def save(self, *args, **kwargs):
#         do_something()
#         super().save(*args, **kwargs)  # Call the "real" save() method.
#         do_something_else()

# ----------------------inheriting class and meta-------------------------------


# class CommonInfo(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.PositiveIntegerField()
#     m2m = models.ManyToManyField(
#         OtherModel,
#         related_name="%(app_label)s_%(class)s_related",
#         related_query_name="%(app_label)s_%(class)ss",
#     )

#     class Meta:
#         abstract = True
#         ordering = ['name']


# class Unmanaged(models.Model):
#     class Meta:
#         abstract = True
#         managed = False


# class Student(CommonInfo, Unmanaged):
#     home_group = models.CharField(max_length=5)

#     class Meta(CommonInfo.Meta, Unmanaged.Meta):
#         ordering = [] # Remove parent's ordering effect if not abstract( i think )
    

# ------------------Multi-table inheritance----------------------
# class Place(models.Model):
#     name = models.CharField(max_length=50)
#     address = models.CharField(max_length=80)


# class Restaurant(Place):
#     serves_hot_dogs = models.BooleanField(default=False)
#     serves_pizza = models.BooleanField(default=False)
# Place.objects.filter(name="Bob's Cafe")
# Restaurant.objects.filter(name="Bob's Cafe")
# p = Place.objects.get(id=12) # If p is a Restaurant object, this will give the child class:
# p.restaurant #<Restaurant: ... >

# -------------------proxy-----------------------
class OrderedPerson(Person):
    class Meta:
        ordering = ["lname"]
        proxy = True


# -------------------AutoField-----------------
# class Article(models.Model):
#     article_id = models.AutoField(primary_key=True)
#     ...


# class Book(models.Model):
#     book_id = models.AutoField(primary_key=True)
#     ...


# class BookReview(Book, Article):
#     pass








