"""
URL configuration for careconnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from staff.views import DoctorListCreateView
from staff.views import DoctorRetriveUpdateDeleteView
from staff_v2 import views
from bookings.views import AppointmentListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctor/',DoctorListCreateView.as_view()),
    path('doctor/<int:pk>/',DoctorRetriveUpdateDeleteView.as_view()),
    #v2
    path('v2/doctor/',views.DoctorListCreateV2.as_view()),
    path('v2/doctor/<int:pk>/',views.DoctorFilterDeleteUpdateView.as_view()),
    #v2 user
    path('v2/admin-register/',views.AdminCreateView.as_view()),
    #booking
    path('appointments/',AppointmentListCreateView.as_view()),

    # Application Routing for urls
    path('v2/bookings/',include('bookings_v2.urls'))

]
