# from reportlab.pdfgen import canvas
# import os

# def generate_receipt(payment):

#     if not os.path.exists("receipts"):
#         os.makedirs("receipts")

#     file_path = f"receipts/{payment.id}.pdf"

#     c = canvas.Canvas(file_path)
#     c.drawString(100, 750, "PAYMENT RECEIPT")
#     c.drawString(100, 700, f"Amount: {payment.amount}")
#     c.drawString(100, 680, f"Method: {payment.method}")
#     c.drawString(100, 660, f"Status: {payment.status}")
#     c.save()

#     return file_path
from reportlab.pdfgen import canvas
from django.conf import settings
import os

def generate_receipt(payment):
    # Create a 'receipts' folder inside your Media directory
    receipts_dir = os.path.join(settings.MEDIA_ROOT, "receipts")
    if not os.path.exists(receipts_dir):
        os.makedirs(receipts_dir)

    filename = f"receipt_{payment.transaction_id}.pdf"
    file_path = os.path.join(receipts_dir, filename)

    # Generate PDF
    c = canvas.Canvas(file_path)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, "SK PROPERTY KINGS - RECEIPT")
    c.setFont("Helvetica", 12)
    c.line(100, 780, 500, 780)
    
    c.drawString(100, 750, f"Transaction ID: {payment.transaction_id}")
    c.drawString(100, 730, f"Property: {payment.property.title}")
    c.drawString(100, 710, f"Customer: {payment.user.username}")
    c.drawString(100, 690, f"Amount: UGX {payment.amount}")
    c.drawString(100, 670, f"Payment Method: {payment.method}")
    c.drawString(100, 650, f"Status: {payment.status.upper()}")
    c.drawString(100, 630, f"Date: {payment.created_at.strftime('%Y-%m-%d %H:%M')}")
    
    c.showPage()
    c.save()

    return f"{settings.MEDIA_URL}receipts/{filename}"