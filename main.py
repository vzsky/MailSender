from emails import *
from sendMail import *

if __name__ == "__main__" : 

    mailfrom = 'web@simpic2024.com'
    recipients = ['']

    ses = getSES()
    sendmails(ses, mailfrom, recipients, TemplateEmail)
