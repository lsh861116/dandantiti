from django.db import models

# Create your models here.
class KeyWordSpider(models.Model):
    id = models.AutoField(max_length=11, db_column="UID", primary_key=True)
    keyword=models.CharField(max_length=32, blank=False)
    userId=models.IntegerField()
    createTime=models.DateTimeField(auto_now_add=True)
    updateTime=models.DateTimeField(auto_now=True)#
    state=models.CharField(max_length=4,default=0)#状态0正常使用,1删除


    class Meta:
        db_table='keyword_spider'
