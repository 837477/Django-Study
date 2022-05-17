from django.contrib import admin
from .models import Sample, SampleReference


class SampleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']  # 특정 컬럼들로 검색한다.


# Admin 페이지에서 해당 모델이 접근하기 위한 설정
admin.site.register(Sample, SampleAdmin)
admin.site.register(SampleReference)
