from django.db import models

# Create your models here.


class Parameter(models.Model):
    key_choices = (('str_type', '文本'), ('image_type', '图片'))
    key_type = models.CharField(
        '类型', choices=key_choices, max_length=10, default='str_type'
    )
    key_key = models.CharField('参数名', max_length=32, null=False)
    key_value = models.CharField('参数值', max_length=128, null=True, blank=True)
    key_remark = models.CharField('备注', max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = '参数设置'
        verbose_name_plural = verbose_name
        db_table = 'xcx_parameter'
