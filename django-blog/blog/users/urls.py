from django.conf.urls import url
import views


urlpatterns=[
    url(r'register/$',views.register,name='register'),
]