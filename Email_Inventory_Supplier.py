import smtplib
import SQLConnection

def contactInventory():
    
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

def placeOrderRestock():
    connection = SQLConnection
    
    outOfStock_Query = "SELECT itemName FROM inventory WHERE ranOut = 1"
    
    try:
        mycursor = SQLConnection.connection.cursor()
        mycursor.execute(outOfStock_Query)
        items_Result = mycursor.SQLConnection.fetch_all()
        
        outOfStock_Items = [row[0] for row in items_Result]
        
        if outOfStock_Items:
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
        
    except:
        print(f"Database error: {ImportError}")