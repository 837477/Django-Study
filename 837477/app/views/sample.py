from random import random
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator  # 꽤나 괜찮네
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from app.forms import SampleForm
from app.models import Sample, SampleReference


def index(request):
    return HttpResponse("Hello 837477 !")


def get_sample_list(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    sample_list = Sample.objects.order_by('-created_at')
    if kw:
        sample_list = sample_list.filter(
            Q(title__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(samplereference__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(samplereference__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()

    paginator = Paginator(sample_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    result = {'sample_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'app/sample_list.html', result)


def get_sample(request, sample_id):
    # sample = Sample.objects.get(id=sample_id)
    sample = get_object_or_404(Sample, pk=sample_id)
    result = {'sample': sample}
    return render(request, 'app/sample_detail.html', result)


@login_required(login_url='common:login')
def create_sample(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            sample = form.save(commit=False)
            sample.author = request.user  # author 속성에 로그인 계정 저장
            sample.created_at = timezone.now()
            sample.save()
            return redirect('app:main')
    else:
        form = SampleForm()
    return render(request, 'app/sample_form.html', {'form': form})


@login_required(login_url='common:login')
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
        created_at=timezone.now(),
        author=request.user
    )
    sample_ref.save()
    return redirect('app:detail', sample_id=sample.id)


@login_required(login_url='common:login')
def update_sample(request, sample_id):
    sample = get_object_or_404(Sample, pk=sample_id)
    if request.user != sample.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('app:detail', sample_id=sample_id)
    if request.method == "POST":
        form = SampleForm(request.POST, instance=sample)
        if form.is_valid():
            sample = form.save(commit=False)
            sample.updated_at = timezone.now()
            sample.save()
            return redirect('app:detail', sample_id=sample.id)
    else:
        form = SampleForm(instance=sample) # instance는 해당 데이터로 질문을 수정하는 화면에서 제목과 내용이 채워진 채로 보임
    return render(request, 'app/sample_form.html', {'form': form})


@login_required(login_url='common:login')
def delete_sample(request, sample_id):
    sample = get_object_or_404(Sample, pk=sample_id)
    if request.user != sample.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('app:detail', sample_id=sample.id)
    sample.delete()
    return redirect('app:main')


@login_required(login_url='common:login')
def sample_vote(request, sample_id):
    sample = get_object_or_404(Sample, pk=sample_id)
    if request.user == sample.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        sample.voter.add(request.user)
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


def model_dummy(request):
    for num in range(1, 300):
        sample = Sample(
            title=f"TITLE {num}",
            content=f"CONTENT {num}",
            created_at=timezone.now()
        )
        sample.save()
