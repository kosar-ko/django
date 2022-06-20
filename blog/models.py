from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    description = models.CharField(_("توضيحات"), max_length=100)
    content = RichTextField()
    created_at = models.DateTimeField(_("زمان انتشار"), default=timezone.now )
    author = models.ForeignKey(User, verbose_name=_("نويسنده"), on_delete=models.CASCADE)
    image = models.ImageField(_("تصوير"), upload_to="blogs/", blank = True, null= True)
    category = models.ForeignKey("Category", related_name="blog",verbose_name=_("دسته بندي"), on_delete=models.CASCADE, null=True , blank=True)
    tags = models.ManyToManyField("Tag", verbose_name=_("تگ ها"), related_name="blogs", blank=True, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(_("عنوان"),max_length=50)
    slug = models.SlugField(_("عنوان لاتين"))
    published_at = models.DateTimeField(_("تاريخ انتشار"), auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(_("عنوان"),max_length=50)
    slug = models.SlugField(_("عنوان لاتين"))
    published_at = models.DateTimeField(_("تاريخ انتشار"), auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(_("تاريخ بروزرساني"), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

class Comments(models.Model):
    blog = models.ForeignKey("blog", verbose_name=_("مقاله"),related_name="comments" , on_delete=models.CASCADE)
    name = models.CharField(_("نام كاربر"), max_length=70)
    email = models.EmailField(_("آدرس الكترونيكي"),max_length=100)
    message = models.TextField(_("متن نظر"))
    date = models.DateTimeField(_("تاريخ انتشار"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "كامنت"
        verbose_name_plural = "كامنت ها"
    def __str__(self):
        return self.email
