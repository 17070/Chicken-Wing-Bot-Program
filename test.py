#s2 = "$Invalid"
#check_s2 = s2.isalpha()
#print(check_s2)

#customer details dictionary
customer_details = {}

#Blank Input         
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response !="":
            return response.title()
        else:
            print("This cannot be blank")   
            

def collect():  

  question = ("Please enter your name ")
  customer_details['name'] = not_blank(question )
  print (customer_details['name'])
  
  
collect()