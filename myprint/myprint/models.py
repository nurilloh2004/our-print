from django.utils.translation import gettext_lazy as _
from unicodedata import category
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class MyUserManager(BaseUserManager):


    def create_user(self, first_name, phone_number, password=None):
        if not phone_number:
            raise ValueError('Users must have an phone number')
        user = self.model(
            first_name=first_name,
            phone_number = phone_number
           
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name,phone_number,  password):
        user = self.create_user(first_name,phone_number, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first_name'), max_length=64, blank=True)
    full_name = models.CharField(_('full_name'), max_length=64, blank=True)
    phone_number = models.IntegerField(_('phone_number'), blank=True, unique=True)
    email = models.EmailField(verbose_name='email address', null=True, max_length=25)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name']

    objects = MyUserManager()

    def get_full_name(self):
        return self.full_name 
        
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'

    def __str__(self) -> str:
        return self.full_name

    def save(self, *args, **kwargs):
        # password = self.password
        # self.set_password(password)
        return super(User,self).save(*args, **kwargs)

#Banner
class Banner(models.Model):
    name = models.CharField(_('name'), max_length=65)

    def __str__(self):
        return self.name

#detail product
class InfoProduct(models.Model):
    size = models.CharField(_('size'), max_length=65)
    element = models.CharField(_('element'), max_length=65)


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(_('name'), max_length=65)
    image = models.ImageField(_('image'), upload_to='media/category_image')
    

#Product
class Product(models.Model):
    name = models.CharField(_('name'), max_length=65)
    image = models.ImageField(_('image'), upload_to='media/product')
    info_product = models.ForeignKey(InfoProduct, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(_('description'), blank=True, null=True)





    def __str__(self):
        return self.name


#печать.
class Printer(models.Model):
    name = models.CharField(_('name'), max_length=65)
    description = models.TextField(_('description'), blank=True, null=True)
    image = models.ImageField(_('image'), upload_to='media/printer')


class InfoType(models.Model):
    size = models.CharField(_('size'), max_length=65)
    type_paper = models.CharField(_('type_paper'), max_length=65)
    one_site_print = models.CharField(_('one_site_print'), max_length=65)
    double_site_print = models.CharField(_('double_site_print'), max_length=65)
    

    def __str__(self) -> str:
        return self.size
#Размер бумага 	Тип бумага 	Односторонняя печать (4+0) 	Двухсторонняя печать (4+4)

class Type(models.Model):
    name = models.CharField(_('name'), max_length=65)
    infotype = models.ForeignKey(InfoType, on_delete=models.CASCADE, related_name="types")
    

    def __str__(self) -> str:
        return self.name
    
# Reklama , Poligrafia, Suviner
class TypeService(models.Model):
    name = models.CharField(_('name'), max_length=65)


    def __str__(self) -> str:
        return self.name


class MenuService(models.Model):
    name = models.CharField(_('name'), max_length=65)
    image = models.ImageField(_('image'), upload_to='media/menuservice')
    type_service = models.ForeignKey(TypeService, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

#Mы предлагаем
class Tariff(models.Model):
    name = models.CharField(_('name'), max_length=65)

    def __str__(self) -> str:
        return self.name


class MenuTariff(models.Model):
    name = models.CharField(_('name'), max_length=65)
    image = models.ImageField(_('image'), upload_to='media/imagesTariff')
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)


    def __str__(self) -> str:
            return self.name


class CEO(models.Model):
    name = models.CharField(_('name'), max_length=65)
    image = models.ImageField(_('image'), upload_to='media/ceo')
    number = models.IntegerField(_('number'), )
    description = models.TextField(_('description'), blank=True, null=True)


    def __str__(self) -> str:
                return self.name


class Sponsors(models.Model):
    name = models.CharField(_('name'), max_length=65)
    image = models.ImageField(_('image'), upload_to='media/sponsor')


    def __str__(self) -> str:
                return self.name


class Contact(models.Model):
    name = models.CharField(_('name'), max_length=65)
    number = models.IntegerField(_('number'))
    info = models.CharField(_('info'), max_length=65)
    description = models.TextField(_('description'), blank=True, null=True)
    image = models.ImageField(_('image'), upload_to='media/contact')


    def __str__(self) -> str:
                return self.name

#Наши работы.   
class Portfolio(models.Model):
    name = models.CharField(_('name'), max_length=65)
    image = models.ImageField(_('image'), upload_to='media/portfolio')

    def __str__(self) -> str:
                return self.name


class SocialMedia(models.Model):
    name = models.CharField(_('name'), max_length=65)
    number = models.IntegerField(_('number'))
    image = models.ImageField(_('image'), upload_to='media/social_media')

    def __str__(self) -> str:
                return self.name






class OrderForm(models.Model):
    Product_Status = (
        ('шт', 'шт'),
        ('усл', 'усл'),
    )
    name = models.CharField(max_length=65)
    status_order = models.CharField(max_length=20, choices=Product_Status, default='шт', null=True, blank=True)
    amount = models.IntegerField()
    price = models.PositiveIntegerField()
    price_free_VAT = models.PositiveIntegerField()
    VAT = models.FloatField()
    price_with_VAT = models.PositiveIntegerField()
    total = models.PositiveIntegerField()    
    total_price_with_VAT = models.PositiveIntegerField()    
    total_price_ALL = models.PositiveIntegerField()        
    

    def __str__(self) -> str:
                return self.name
    

class Order(models.Model):
    id_name_order = models.CharField(max_length=300)
    name_client = models.CharField(max_length=65)
    client_phone_number = models.CharField(max_length=65)
    manager_name = models.CharField(max_length=65)
    date_order = models.DateTimeField(auto_now_add=True)
    ready_product_date_order = models.DateTimeField()


    def __str__(self) -> str:
                return self.id_name_order
    

class Form(models.Model):
    full_name = models.CharField(max_length=65)
    phone_number = models.CharField(max_length=15)

    def __str__(self) -> str:
                return self.full_name