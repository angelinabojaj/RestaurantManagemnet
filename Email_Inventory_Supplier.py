import smtplib

def sendEmail():
    
    email = "theanythingconeyisland@gmail.com"
    emailPassword = "vnow rynt hwot rmaw"
    receiverEmail = "inventorysupplierou@gmail.com"

    subjectEmail = "Fufillment Needed"
    messageEmail = "Dear Inventory Supplier,\nThe Anything Conney Island needs a restock done please.\n\nSincerely,\n\nThe Anything Coney Island\ntheanythingconeyisland@gmail.com"

    text = f"Subject: {subjectEmail}\n\n{messageEmail}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    
    server.login(email, emailPassword)
    
    server.sendmail(email, receiverEmail, text)
    
    print("Email Sent")