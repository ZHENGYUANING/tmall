from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200,db_index=True)#商品名称
    pid = models.BigIntegerField()
    sku = models.CharField(max_length=200)#SKU
    # slug = models.SlugField(max_length=200,db_index=True)#商品链接
    # image = models.ImageField(upload_to='products/%Y/%m/%d',
    #                           blank=True)#商品图片
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 价格
    stock = models.PositiveIntegerField()  # 库存
    # created = models.DateTimeField(auto_now_add=True) # 更新时间
    addtime = models.CharField(max_length=200)  # 上架时间\
    
    class Meta:
        ordering = ['-addtime']
        ordering = ('name',)
        # index_together = (('id','slug'))

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

