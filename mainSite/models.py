from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    #定义排序方式
    class Meta:
        ordering = ('-pub_date',)
    #定义返回缩略短语类型
    def __unicode__(self):
        return self.title

