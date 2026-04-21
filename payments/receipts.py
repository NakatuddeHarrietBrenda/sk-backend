from reportlab.pdfgen import canvas
import os

def generate_receipt(payment):

    if not os.path.exists("receipts"):
        os.makedirs("receipts")

    file_path = f"receipts/{payment.id}.pdf"

    c = canvas.Canvas(file_path)
    c.drawString(100, 750, "PAYMENT RECEIPT")
    c.drawString(100, 700, f"Amount: {payment.amount}")
    c.drawString(100, 680, f"Method: {payment.method}")
    c.drawString(100, 660, f"Status: {payment.status}")
    c.save()

    return file_path