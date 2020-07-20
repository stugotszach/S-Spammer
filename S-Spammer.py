import smtplib, time, os, sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep
from sys import platform
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
greybg='\033[47m'
reset='\033[0m'
grey='\033[37m'
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 

# This will start our email server
smtp = "smtp.gmail.com" 
port = 587
server = smtplib.SMTP(smtp,port)
server.starttls()

banner=("""
    ███████╗      ███████╗██████╗  █████╗ ███╗   ███╗███████╗███╗   ███╗██████╗ 
    ██╔════╝      ██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝████╗ ████║██╔══██╗
    ███████╗█████╗███████╗██████╔╝███████║██╔████╔██║█████╗  ██╔████╔██║██████╔╝
    ╚════██║╚════╝╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██╔══██╗
    ███████║      ███████║██║     ██║  ██║██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║██║  ██║
    ╚══════╝      ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝
    
 (TURN ON LESS SECURE APPS OR THIS WONT WORK)""")

login = True
while login:
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')
    prYellow(banner)
    prYellow("Your E-Mail:")
    gmail=input(" ")

    prYellow("Password:")
    password=input(" ")

    try:
        server.login(gmail,password)
        break
    except smtplib.SMTPAuthenticationError:
        prRed("[!]" + reset + " Something went wrong, did you turn on less secure apps? or did you input a wrong pass or E-Mail?")
        sleep(4)
        login = True
if platform == "linux" or platform == "linux2":
    os.system('clear')
elif platform == "win32":
    os.system('cls')
prYellow(banner)
loop = True
while loop:
    
    prYellow("Here you need to determine the victims carrier: ")
    prYellow("""
[1] AT&T
[2] SPRINT
[3] T-MOBILE
[4] VERIZON
[5] BOOST MOBILE
[6] CRICKET
[7] METRO PCS
[8] TRACFONE
[9] U.S. Cellular
[0] VIRGIN MOBILE
""")
    carrier=input("")
    if carrier=="1":
        sms_gateway='@txt.att.net'
        break
    elif carrier=="2":
        sms_gateway='@messaging.sprintpcs.com'
        break
    elif carrier=="3":
        sms_gateway='@tmomail.net'
        break
    elif carrier=="4":
        sms_gateway='@vtext.com'
        break
    elif carrier=="5":
        sms_gateway='@myboostmobile.com'
        break
    elif carrier=="6":
        sms_gateway='@sms.mycricket.com'
        break
    elif carrier=="7":
        sms_gateway='@mymetropcs.com'
        break
    elif carrier=="8":
        sms_gateway=='@mmst5.tracfone.com'
        break
    elif carrier=="9":
        sms_gateway='@email.uscc.net'
        break
    elif carrier=="0":
        sms_gateway='@vmobl.com'
        break
    else:
        print("Thats not one of the options!")
        sleep(2)
        loop=True

print("Now the number of the target (make sure to include area code!): ")
target_number=input(" ")
number = (target_number + sms_gateway)

msg = MIMEMultipart()
msg['From'] = gmail
msg['To'] = sms_gateway

if platform == "linux" or platform == "linux2":
    os.system('clear')
elif platform == "win32":
    os.system('cls')
prYellow(banner)

print("Message body (leave blank if none): ")
message_body=input(" ")

print("Message: ")
message=input(" ")
msg['Subject'] = (message)
body = (message_body)

print("Number of messages to send: ")
total = int(input(" "))

msg.attach(MIMEText(message_body, 'plain'))

sms = msg.as_string()

for i in range(int(total)):
    server.sendmail(gmail,number,sms)

#quit the server
server.quit()
print("Sent!")
sleep(2)
exit()
