
from django.urls import path
from bookings_v2.views import SignUpView,AppoinmentListCreateView,AppointmentRetrieveUpdateDelete

urlpatterns = [
            path('signup/',SignUpView.as_view()),
            # for appoinments
            path('appointments/',AppoinmentListCreateView.as_view()),
            path('appointments/<int:pk>/',AppointmentRetrieveUpdateDelete.as_view()),  
]