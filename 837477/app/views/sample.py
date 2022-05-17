from random import random
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from app.models import Sample, SampleReference


def index(request):
    return HttpResponse("Hello 837477 !")


def get_sample_list(request):
    sample_list = Sample.objects.order_by('-created_at')
    result = {'sample_list': sample_list}
    return render(request, 'app/sample_list.html', result)


def get_sample(request, sample_id):
    # sample = Sample.objects.get(id=sample_id)
    sample = get_object_or_404(Sample, pk=sample_id)
    result = {'sample': sample}
    return render(request, 'app/sample_detail.html', result)


def create_sample_ref(request, sample_id):
    sample = get_object_or_404(Sample, pk=sample_id)

    # 첫 번째 방법
    # sample.samplereference_set.create(
    #     content=request.POST.get('content'),
    #     created_at=timezone.now()
    # )

    # 두 번째 방법
    sample_ref = SampleReference(
        sample=sample,
        content=request.POST.get('content'),
        created_at=timezone.now()
    )
    sample_ref.save()
    return redirect('app:detail', sample_id=sample.id)


def model_test(request):
    # sample 데이터 생성
    sample = Sample(
        title=f"TITLE {str(random())}",
        content=f"CONTENT {str(random())}",
        created_at=timezone.now()
    )
    sample.save()

    # 방금 생성된 데이터 id 출력
    print(sample.id)

    # 저장된 모든 데이터 반환
    print(Sample.objects.all())

    # id가 1인 데이터 반환 (주의: 리스트로 반환 / 만약 없으면, 빈 리스트)
    print(Sample.objects.filter(id=1))
    # id가 1인 데이터 반환 (주의: 단일 반환 / 만약 없으면, 에러 발생)
    print(Sample.objects.get(id=1))

    # 특정 데이터 수정
    sample = Sample.objects.filter(id=1)
    sample[0].title = f"TEST {str(random())}"

    # 특정 데이터 삭제
    # sample = Sample.objects.get(id=1)
    # sample.delete()

    # sample_reference 데이터 생성 (참조키는, sample(id=1)로 설정)
    sample_ref = SampleReference(
        sample=sample[0],
        content=f"SAMPLE_REF {str(random())}",
        created_at=timezone.now()
    )
    sample_ref.save()

    # 현재 sample(id=1) 인 친구랑 참조된(연결된) 모든 sample_reference 데이터 가져오기
    print(sample[0].samplereference_set.all())

    return HttpResponse("Model Test !")
