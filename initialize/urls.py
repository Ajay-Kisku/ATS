from django.contrib import admin
from django.urls import path
from initialize import views
# from initialize.views import PDFView

urlpatterns = [ 
    path("", views.index, name="home"),
    path("candidate", views.candidate, name="candidate"),
    path("hr", views.hr, name="hr_dashboard"),
    path("hr_login", views.login, name="hr_dashboard"),
    path("upload", views.upload_pdf, name="upload"), 
    path("screening", views.screening, name="first_round"),
    path("screening_login", views.screening_login, name="first_round"),
    # path('pdf-view/', PDFView.as_view(), name='pdf-view'),
    
]  