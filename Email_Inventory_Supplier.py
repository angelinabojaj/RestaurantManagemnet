import smtplib
import webbrowser
import SQLConnection

def contactInventory():
    
    email = "theanythingconeyisland@gmail.com"
    emailPassword = "vnow rynt hwot rmaw"
    receiverEmail = "inventorysupplierou@gmail.com"

    subjectEmail = "Contact Needed - The Anything Coney Island"
    messageEmail = "Dear Inventory Supplier,\nPlease contact us immediately given there is we have a current issue to discuss.\n\nSincerely,\n\nThe Anything Coney Island\ntheanythingconeyisland@gmail.com"

    text = f"Subject: {subjectEmail}\n\n{messageEmail}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    
    server.login(email, emailPassword)
    
    server.sendmail(email, receiverEmail, text)
    
    print("Email Sent")
    
    server.quit()

def placeOrderRestock():
    connection = SQLConnection
    
    outOfStock_Query = "SELECT itemName FROM inventory WHERE ranOut = 1"
    
    try:
        mycursor = SQLConnection.connection.cursor()
        mycursor.execute(outOfStock_Query)
        items_Result = SQLConnection.fetch_all(outOfStock_Query)
        
        outOfStock_Items = [row[0] for row in items_Result]
        
        if outOfStock_Items:
                email = "theanythingconeyisland@gmail.com"
                emailPassword = "vnow rynt hwot rmaw"
                receiverEmail = "inventorysupplierou@gmail.com"

                subjectEmail = "Fufillment Needed - The Anything Coney Island"
                messageEmail = "Dear Inventory Supplier,\n\nThe Anything Conney Island needs a restock done on the following:\n\n" f"{'. '.join(outOfStock_Items)}\n\nSincerely,\n\nThe Anything Coney Island\ntheanythingconeyisland@gmail.com"

                text = f"Subject: {subjectEmail}\n\n{messageEmail}"
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(email, emailPassword)
                server.sendmail(email, receiverEmail, text)
                print("Email Sent!")
                server.quit()
        
    except:
        print(f"Database error: {ImportError}")

def requestTimeOff_Button():
    googleMail = "https://mail.google.com/mail/u/3/#inbox" # Login To Your Email To See Scheduele
    webbrowser.open(googleMail)