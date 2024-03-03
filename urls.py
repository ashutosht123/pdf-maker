# urls.py

from django.urls import path
from pdfgenerator.views import generate_pdf, pdf_generator_view, generate_pdf_from_database

urlpatterns = [
    path('', pdf_generator_view, name='pdf_generator'),
    path('generate-pdf/', generate_pdf, name='generate_pdf'),
    path('generate-pdf-from-database/', generate_pdf_from_database, name='generate_pdf_from_database'),
]
