import smtplib  #simple mail transfer protocol library
import time

def mail(encrypted):
    #smtp port and server address
    server = smtplib.SMTP_SSL("smtp.gmail.com",465) #587 port is not secure
    #( your email, password)
    server.login("Your_Email","Your_Password")
    #(your mail, friend's mail, message)
    server.sendmail("Your_Email","Friend's Email",encrypted)
    server.quit()


def encrypt_message():
    message = "I will become a Software Engineer one Day and this will surely happen"
    key = 3
    encrypted = ""
    series="abcdefghijklmnopqrstuvwxyz"
    series+=series.upper()
    series+=" "
    for letter in message:
        position = series.find(letter)
        new_position = (position + key)%52
        if letter == " ":
            encrypted +=" "
        else:
            encrypted += series[new_position]
    print(encrypted)
    mail(encrypted)
    time.sleep(2)
    decrypt_message(encrypted,series,key)



def decrypt_message(encrypted,series,key):
    decrypted =""
    for letter in encrypted:
        position2 = series.find(letter)
        new_position2 = (position2 - key)%52
        if letter ==" ":
            decrypted += " "
        else:
            decrypted += series[new_position2]
    print(decrypted)


encrypt_message()
        

