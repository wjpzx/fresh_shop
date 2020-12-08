from datetime import datetime
from DjangoUeditor.models import UEditorField

from django.db import models

# Create your models here.


class GoodsCategory(models.Model):
    """商品分类"""
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )

    name = models.CharField(default="",max_length=30,help_text="类别名",verbose_name="类别名")
    code = models.CharField(default="",max_length=30,help_text="类别code",verbose_name="类别code")
    desc = models.TextField(default="",help_text="类别描述",verbose_name="类别描述")
    # 目录树级别
    category_type = models.IntegerField(choices=CATEGORY_TYPE,help_text="类目级别",verbose_name="类目级别")
    # 设置models有一个指向自己的外键
    parent_category = models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True,verbose_name="父类目级别",help_text="父目录",related_name="sub_cat")
    is_tab = models.BooleanField(default=False,help_text="是否导航",verbose_name="是否导航")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        db_table = "tb_goods_category"
        verbose_name = "商品类别"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
    某一大类下的宣传商标
    """
    category = models.ForeignKey(GoodsCategory,on_delete=models.CASCADE,related_name='brands',null=True,blank=True,verbose_name="商品类目")
    name = models.CharField(default="",max_length=30,help_text="品牌名",verbose_name="品牌名")
    desc = models.TextField(default="",max_length=200,help_text="品牌描述",verbose_name="品牌描述")
    image = models.ImageField(max_length=200,upload_to="brands/")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        db_table="tb_goods_category_brand"
        verbose_name="宣传品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    商品
    """
    category = models.ForeignKey(GoodsCategory,on_delete=models.CASCADE,verbose_name="商品分类")
    goods_sn = models.CharField(max_length=50,default="",verbose_name="商品唯一货号")
    name = models.CharField(max_length=100,verbose_name="商品名")
    click_num = models.IntegerField(default=0,verbose_name="点击数")
    sold_num = models.IntegerField(default=0,verbose_name="商品销售量")
    fav_num = models.IntegerField(default=0,verbose_name="收藏数")
    goods_num = models.IntegerField(default=0,verbose_name="库存数")
    market_price = models.FloatField(default=0,verbose_name="市场价格")
    shop_price = models.FloatField(default=0,verbose_name="本店价格")
    goods_brief = models.TextField(max_length=500,verbose_name="商品简短描述")
    goods_desc = UEditorField(verbose_name="内容",imagePath="goods/images",width=1000,filePath="goods/images",default="")
    ship_free = models.BooleanField(default=True,verbose_name="是否承担运费")
    # 首页展示的商品封面图
    goods_front_image = models.ImageField(upload_to="goods/images",null=True,blank=True,verbose_name="封面图")
    # 首页中新品展示
    is_new = models.BooleanField(default=True,verbose_name="是否新品")
    # 商品详情页的热卖商品，自行设置
    is_hot = models.BooleanField(default=False,verbose_name="是否热销")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        db_table = "tb_goods"
        verbose_name = "商品信息"
        verbose_name_plural = verbose_name
        ordering = ['-market_price']

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """商品轮播图"""
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name="商品",related_name='images')
    image = models.ImageField(upload_to="",verbose_name="图片",null=True,blank=True)
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        db_table="tb_goods_image"
        verbose_name = "商品轮播"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """首页轮播的商品"""
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name="商品")
    image = models.ImageField(upload_to='banner',verbose_name="轮播图片")
    index = models.IntegerField(default=0,verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        db_table="tb_banner"
        verbose_name="首页轮播"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.goods.name


class IndexAd(models.Model):
    """商品广告"""
    category = models.ForeignKey(GoodsCategory,on_delete=models.CASCADE,related_name='category',verbose_name="商品类目")
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,related_name='goods')

    class Meta:
        db_table="tb_indexad"
        verbose_name="首页广告"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.goods.name


class HotSearchWords(models.Model):
    """搜索栏下方热搜词"""
    keywords = models.CharField(default="",max_length=20,verbose_name="热搜词")
    index = models.IntegerField(default=0,verbose_name="排序")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        db_table="tb_hotsearch_words"
        verbose_name="热搜排行"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.keywords