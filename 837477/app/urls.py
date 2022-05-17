from django.urls import path
from .views import sample


app_name = 'app'


urlpatterns = [
    path('sample/index', sample.index, name='index'),
    path('sample/model_test', sample.model_test, name='model_test'),
    path('sample/get_sample_list', sample.get_sample_list, name='get_sample_list'),
    path('sample/get_sample/<int:sample_id>', sample.get_sample, name='detail'),
    path('sample/reference/<int:sample_id>', sample.create_sample_ref, name='create_sample_ref')
]
