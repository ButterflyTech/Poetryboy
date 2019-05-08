from django.db import models


class AuthorModel(models.Model):

    class Meta:
        verbose_name = "作者"
        verbose_name_plural = "作者"

    name = models.CharField(null=False, default="", max_length=128, verbose_name="作者名")
    desc = models.TextField(null=False, default="", verbose_name="描述")
    dynasty = models.CharField(null=False, default="", max_length=128, verbose_name="朝代")

    def __str__(self):
        return self.name


class PoemModel(models.Model):

    class Meta:
        verbose_name = "诗歌"
        verbose_name_plural = "诗歌"

    title = models.CharField(null=False, default="", max_length=128, verbose_name="诗歌名")
    author = models.ForeignKey(AuthorModel, on_delete=models.SET_NULL, null=True, verbose_name="作者")
    paragraphs = models.CharField(null=False, default="", max_length=128, verbose_name="诗歌正文")
    strains = models.CharField(null=False, default="", max_length=128, verbose_name="唱法")
    dynasty = models.CharField(null=False, default="", max_length=128, verbose_name="朝代")
    audio = models.FileField(verbose_name="诗歌朗读文件", null=True)

    def __str__(self):
        return self.title
