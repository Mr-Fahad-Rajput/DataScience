import re
file = open("Regex/test_emails.txt", "r")
 
a_list = list(file)

a_list_string = ",".join(str(x) for x in a_list) # converts the list to a string
# Extracting Names From the String using Raw Python 
name= a_list_string[209:232] # the best way to Extract Names from a String  Using pure Python Was by using the indexes of "From:" Key word
name2= a_list_string[3927:3953]
 
# print (a_list_string.find("From:", 220))
print("\nThe Emails Were Sent:")
print (name + " and ")
print (name2)
 
# Extracting Just Names Of The Senders Using RE Module
regex_Names = re.findall("From:.+\"",a_list_string)
print("\nNames Using Regex:")
print(regex_Names)

#Extracting Email Adresses Of Senders Using Regex
regex_Emails = re.findall("From:.+",a_list_string)
regex_Emails = ",".join(str(x) for x in regex_Emails) 
regex_Emails = re.sub('From:' , ' ', regex_Emails)
regex_Emails = re.findall("\S+@\S+",regex_Emails)
print("\nThe Emails Of The Senders Extracted Using Regex:")
print(regex_Emails)

#First Part Of the Email Using regex
regex_Emails_string = ",".join(str(x) for x in regex_Emails) 
regex_Emails_string = re.sub(',' , ' ', regex_Emails_string)
fp_Emails = re.findall("\S+@",regex_Emails_string)
print("\nFirst Part Of the Emails:")
print(fp_Emails)

#Last Part Of the Email Using regex
lp_Emails = re.findall("@\S+",regex_Emails_string)
print("\nLast Part Of the Emails:")
print(lp_Emails)

# sender_Name
print("\n Senders Names:")
print(regex_Names)
# sender_Address
print("\nSenders Emails:")
print(regex_Emails)
# rec_Name
print("\nNo Reciepent Names Were Found In The Mails")
# rec_Address
print("\nRecievers Addresses")
rec_Address = re.findall("[^-]To:.+",a_list_string)
print(rec_Address)
# date_Sent
print("\nDate Sent")
date_Sent = re.findall("Date:.+",a_list_string)
print(date_Sent)

# subject
print("\nSubjects Of The Emails")
subject = re.findall("Subject:.+",a_list_string)
print(subject)

# email_body
print("\nBody Of The Emails")
email_Body = re.findall("(Status:[\S\s]+man\n)|(Status: RO\n,[\S\s]+bbot)",a_list_string)
print(email_Body)

file.close()

#Note: I did not split the Emails Into Two As it was easier To Use Regex on Both Using OR character for the searches in  the RE Module