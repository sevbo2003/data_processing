from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('atc/', views.AtcView.as_view(), name='atc'),
    path('atc/download/<str:file_uuid>', views.DownloadATCFileView.as_view(), name='download_atc_file'),
    path('presentations/', views.PresentationsView.as_view(), name='presentations'),
    path('presentations/download/<str:file_uuid>', views.DownloadPresentationsFileView.as_view(), name='download_presentations_file'),
    path('active-ingredients/', views.ActiveIngredientsView.as_view(), name='active_ingredients'),
    path('active-ingredients/download/<str:file_uuid>', views.DownloadActiveIngredientsFileView.as_view(), name='download_active_ingredients_file'),
    # path('languages/', views.LanguageView.as_view(), name='languages'),
    path('languages/', views.LanguageCreateView.as_view(), name='languages'),
    path('languages/<str:language>/', views.LanguageView.as_view(), name='languages'),
    path('languages/download/<str:language>', views.DownloadLanguageFileView.as_view(), name='download_lang_file'),
    path('read/csv/', views.read_csv, name='read_csv'),
]