from django.urls import path
from .views import sample


app_name = 'app'


urlpatterns = [
    path('sample/index', sample.index, name='index'),
    path('sample/model_test', sample.model_test, name='model_test'),
    path('sample/model_dummy', sample.model_dummy, name='set_dummy'),
    path('sample/', sample.get_sample_list, name='main'),
    path('sample/<int:sample_id>', sample.get_sample, name='detail'),
    path('sample/create', sample.create_sample, name='create_sample'),
    path('sample/create/reference/<int:sample_id>', sample.create_sample_ref, name='create_sample_ref'),
    path('sample/update/<int:sample_id>/', sample.update_sample, name='sample_modify'),
    path('sample/delete/<int:sample_id>/', sample.delete_sample, name='sample_delete'),
    path('sample/vote/<int:sample_id>/', sample.sample_vote, name='sample_vote'),
]
