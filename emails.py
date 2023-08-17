class Email():
    content : str
    def __init__(self, subject):
        self.subject = subject

TemplateEmail = Email("test ja")
with open('./emails/template.html') as file : 
  TemplateEmail.content = file.read()
