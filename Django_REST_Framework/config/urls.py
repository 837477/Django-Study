from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('pure/snippets/', views.pure_snippet_list),
    path('pure/snippets/<int:pk>/', views.pure_snippet_detail),
    path('func/snippets/', views.func_api_view_snippet_list),
    path('func/snippets/<int:pk>', views.func_api_view_snippet_detail),
    path('class/snippets/', views.ClassSnippetList.as_view()),
    path('class/snippets/<int:pk>/', views.ClassSnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)