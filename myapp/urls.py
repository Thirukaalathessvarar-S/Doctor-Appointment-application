from django.urls import path
from myapp import views
urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
   path('home/',views.home_view,name='home'),
   path('register/',views.register_view,name='register'),
   path('book_appointment/<int:id>',views.book_appoint,name='book_appointment')
]