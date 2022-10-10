# Generated by Django 4.1.1 on 2022-10-10 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
                ('image', models.ImageField(upload_to='media/category_image', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='CEO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
                ('image', models.ImageField(upload_to='media/ceo', verbose_name='image')),
                ('number', models.IntegerField(verbose_name='number')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
                ('number', models.IntegerField(verbose_name='number')),
                ('info', models.CharField(max_length=65, verbose_name='info')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('image', models.ImageField(upload_to='media/contact', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=65)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='InfoProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=65, verbose_name='size')),
                ('element', models.CharField(max_length=65, verbose_name='element')),
            ],
        ),
        migrations.CreateModel(
            name='InfoType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=65, verbose_name='size')),
                ('type_paper', models.CharField(max_length=65, verbose_name='type_paper')),
                ('one_site_print', models.CharField(max_length=65, verbose_name='one_site_print')),
                ('double_site_print', models.CharField(max_length=65, verbose_name='double_site_print')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_name_order', models.CharField(max_length=300)),
                ('name_client', models.CharField(max_length=65)),
                ('client_phone_number', models.CharField(max_length=65)),
                ('manager_name', models.CharField(max_length=65)),
                ('date_order', models.DateTimeField(auto_now_add=True)),
                ('ready_product_date_order', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
                ('image', models.ImageField(upload_to='media/portfolio', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('image', models.ImageField(upload_to='media/printer', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
                ('number', models.IntegerField(verbose_name='number')),
                ('image', models.ImageField(upload_to='media/social_media', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
                ('image', models.ImageField(upload_to='media/sponsor', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='TypeService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
                ('infotype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='myprint.infotype')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
                ('image', models.ImageField(upload_to='media/product', verbose_name='image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myprint.category')),
                ('info_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myprint.infoproduct')),
            ],
        ),
        migrations.CreateModel(
            name='OrderForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
                ('status_order', models.CharField(blank=True, choices=[('шт', 'шт'), ('усл', 'усл')], default='шт', max_length=20, null=True)),
                ('amount', models.IntegerField()),
                ('price', models.PositiveIntegerField()),
                ('price_free_VAT', models.PositiveIntegerField()),
                ('VAT', models.FloatField()),
                ('price_with_VAT', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('total_price_with_VAT', models.PositiveIntegerField()),
                ('total_price_ALL', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myprint.order', verbose_name='Zakazlar')),
            ],
        ),
        migrations.CreateModel(
            name='MenuTariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
                ('image', models.ImageField(upload_to='media/imagesTariff', verbose_name='image')),
                ('tariff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myprint.tariff')),
            ],
        ),
        migrations.CreateModel(
            name='MenuService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
                ('image', models.ImageField(upload_to='media/menuservice', verbose_name='image')),
                ('type_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myprint.typeservice')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=64, verbose_name='first_name')),
                ('full_name', models.CharField(blank=True, max_length=64, verbose_name='full_name')),
                ('phone_number', models.IntegerField(blank=True, unique=True, verbose_name='phone_number')),
                ('email', models.EmailField(max_length=25, null=True, verbose_name='email address')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Manager',
                'verbose_name_plural': 'Managers',
            },
        ),
    ]
