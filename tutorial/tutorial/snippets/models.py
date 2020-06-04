from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# 提取出了 pygments 支持的所有语言的词法分析程序
LEXERS = [item for item in get_all_lexers() if item[1]]
# 提取出了 pygments 支持的所有语言列表
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# 提取出了 pygments 支持的所有格式化风格列表
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)  # 是否显示行号
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)
        
class TUser(models.Model):
    user_mobile = models.CharField(max_length=11)
    user_name = models.CharField(max_length=20, blank=True, null=True)
    user_password = models.CharField(max_length=255, blank=True, null=True)
    user_img = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=50, blank=True, null=True)
    user_status = models.IntegerField(blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    token = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'


class TUserCodeRecord(models.Model):
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_code_record'


class TUserOperateRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    class_name = models.CharField(max_length=32)
    method_name = models.CharField(max_length=32)
    created_user = models.CharField(max_length=32, blank=True, null=True)
    created_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_user_operate_record'


class TUserThird(models.Model):
    openid = models.CharField(max_length=255, blank=True, null=True)
    account_name = models.CharField(max_length=20)
    account_img = models.CharField(max_length=255)
    user_id = models.IntegerField(blank=True, null=True)
    bind_mobile = models.CharField(max_length=11, blank=True, null=True)
    login_type = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_third'