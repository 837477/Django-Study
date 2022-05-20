from django.db import models
from django.contrib.auth.models import User


class Sample(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_sample')
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    updated_at = models.DateTimeField(null=True, blank=True) # blank = form.is_valid()를 통한 입력 데이터 검증 시 값이 없어도 된다는 의미
    created_at = models.DateTimeField(null=True, default=None)
    voter = models.ManyToManyField(User, related_name='vote_sample')  # 추천인 추가

    # 나중에 ORM으로 다룰 때, filter / all 등의 메소드로 데이터를 출력시 아래의 정보로출력됨.
    def __str__(self):
        return self.title


class SampleReference(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    updated_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, default=None)
