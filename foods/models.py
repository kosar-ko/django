from django.db import models
from django.utils.translation import gettext as _

class Food(models.Model):
    FOOD_TYPE=[
        ("breakfast","صبحانه"),
        ("drinks","نوشيدني"),
        ("dinner", "شام"),
        ("lunch","ناهار")
    ]
    name = models.CharField(max_length=100)
    descrription = models.CharField(_("توضيحات"),max_length=50)
    rate = models.IntegerField(_("امتياز") , default=0)
    price = models.IntegerField(_("(تومان) قيمت"))
    time = models.IntegerField(_(" زمان لازم براي پخت"))
    pub_date = models.DateField(_("تاريخ انتشار"), auto_now=False, auto_now_add=True)
    photo = models.ImageField(upload_to='foods/')
    type_food = models.CharField(_("نوع غذا"), max_length=10, choices=FOOD_TYPE,default="drinks")

    def __str__(self):
        return self.name
