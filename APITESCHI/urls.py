from django.contrib import admin
from django.urls import path
from api.views import Home, About, Blog, Contact, Elements, Portfolio, Services, Single
from api import views

urlpatterns = [
    #path('admin/', admin.site.urls),
     path('', Home.as_view(),name='index'),
     path('about/', About.as_view(),name='about'),
     path('blog/', Blog.as_view(),name='blog'),
     path('contact/', Contact.as_view(),name='contact'),
     path('elements/', Elements.as_view(),name='elements'),
     path('portfolio/', Portfolio.as_view(),name='portfolio'),
     path('services/', Services.as_view(),name='services'),
     path('single/', Single.as_view(),name='single'),
     path('signin/', views.signin,name='signin'),
     path('signup/', views.signup,name='signup'),
     path('logout/',views.signout, name='logout'),
     path('enviar_correo/<str:correo>/<str:usuario>/<str:contra>/', views.enviar_correo, name='enviar_correo'),
]
