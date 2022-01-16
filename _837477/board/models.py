"""
Board 앱에 대한 모델 초기화
- Model이 생성되거나 수정되면, makemigrations 명령을 필수로 진행하고, migrate를 실행
- makemigrations 명령을 수행하더라도 실제로 테이블이 생성되지는 않는다.
- makemigrations 명령은 장고가 테이블 작업을 수행하기 위한 작업 파일(예: migrations/0001_initial.py)을 생성하는 명령어다.
- 실제 테이블 생성은 migrate 명령을 통해서만 가능하다.
"""
from django.db import models


class Question(models.Model):
    """
    질문 테이블을 생성
    """
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()


class Answer(models.Model):
    """
    답변 테이블을 생성
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
