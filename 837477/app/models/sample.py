from django.db import models


class Sample(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, default=None)

    # 나중에 ORM으로 다룰 때, filter / all 등의 메소드로 데이터를 출력시 아래의 정보로출력됨.
    def __str__(self):
        return self.title


class SampleReference(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField()
