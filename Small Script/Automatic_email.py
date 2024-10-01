import win32com.client as win32

def send_email_via_outlook(subject, body, to):
    # Create an instance of the Outlook application
    outlook = win32.Dispatch('outlook.application')
    
    # Create a new email
    mail = outlook.CreateItem(0)  # 0: olMailItem
    mail.Subject = subject
    mail.Body = body
    mail.To = to

    # You can also add CC and BCC if needed
    # mail.CC = "cc@example.com"
    # mail.BCC = "bcc@example.com"

    # Send the email
    mail.Send()
    print("Email sent successfully!")

# Usage example
subject = "Test Email from Python"
body = "This is a test email sent from Python using the Outlook application."
to = "vinh@cadencesolutions.ca"

send_email_via_outlook(subject, body, to)
