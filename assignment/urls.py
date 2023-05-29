from django.urls import re_path

from . import views

urlpatterns = [
    re_path(
        "^company-info/$",
        views.CompanyInfoView().as_view(),
        name="company-info",
    )
    ]

