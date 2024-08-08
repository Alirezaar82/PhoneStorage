from django.urls import path

from . import views

app_name = 'phones'

urlpatterns = [
    path('',views.PhonesListView.as_view(),name='phone-list'),
    path('phone-create',views.PhoneCreatedView.as_view(),name='phone-create'),
    path('phone-update/<int:pk>/',views.PhoneUpdatedView.as_view(),name='phone-update'),
]
