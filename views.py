# views.py

from django.shortcuts import render, HttpResponse
from reportlab.pdfgen import canvas
from .models import models  # Replace 'YourModel' with your actual model name

def generate_pdf(request):
    if request.method == 'POST':
        # Fetch data from the database instead of using input text
        data_from_database = YourModel.objects.all()  # Query your model to get the data

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'

        # Create a canvas
        p = canvas.Canvas(response)

        # Draw things on the PDF, including data from the database
        y_coordinate = 800  # Initial Y coordinate for drawing
        for obj in data_from_database:
            # Adjust Y coordinate and draw each data element from the database
            p.drawString(100, y_coordinate, f"Field 1: {obj.field1}")
            y_coordinate -= 20  # Adjust Y coordinate for next line

        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()
        return response
    return HttpResponse("Method Not Allowed", status=405)

def pdf_generator_view(request):
    return render(request, 'pdf_generator.html')
