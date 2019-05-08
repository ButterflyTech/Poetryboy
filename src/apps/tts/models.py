from django.db import models

# Create your models here.


class TTSProviderModel(models.Model):

    class Meta:
        verbose_name = "语音合成提供商"
        verbose_name_plural = "语音合成提供商"

    name = models.CharField(null=False, default="", max_length=128, verbose_name="供应商名字")
    api_url = models.CharField(null=False, default="", max_length=512, verbose_name="请求URL")
    app_id = models.CharField(null=False, default="", max_length=128, verbose_name="应用ID")
    app_key = models.CharField(null=False, default="", max_length=512, verbose_name="应用Key")
