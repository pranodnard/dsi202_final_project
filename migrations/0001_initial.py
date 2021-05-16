# Generated by Django 2.2.5 on 2021-04-24 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='product/1')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='product/2')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='product/3')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='product/4')),
                ('seller', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='myapp.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.DecimalField(decimal_places=1, max_digits=3)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='myapp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ShoeSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.DecimalField(decimal_places=1, max_digits=3)),
                ('inventory', models.IntegerField(default=1)),
                ('quantity_sold', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Size')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Type')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='myapp.Type'),
        ),
    ]
