'''''''''
email = input("  enter your email address : \n")
clean_email = email.lower().replace(" ", "")
index_at = email.find("@")

if index_at == -1:
    print("wrong email format")
    print(clean_email)

else:
    username = clean_email[:index_at]
    print(f"your email is {username}")




print(f"the index of @ Is {index_at}")
print (f"the lengnth od the email is: {len(clean_email)}")
       
'''''''''
       

''''''''''''''''
email_address = input("please enter your email:")
fix_email = email_address.lower().strip().replace(" ","")
index_email= email_address.find("@")

if index_email==-1:

  print("wrong email")

else:
  
  username = fix_email[:index_email]
  print(f"your username is: {username}")

  print(f"if the index of @ is: {username}")
  print(f"the lenth of the is: {len(username)}")

'''''''''''''''''
  

gmail = input("please enter your email:")
arrange_email = gmail.lower().strip().replace(' ','')
finding_at = gmail.find('@')
if finding_at==-1:
 print('wrong email')

else:

  username=arrange_email[:finding_at]
  print(f'your username is:{username}')







       
       
