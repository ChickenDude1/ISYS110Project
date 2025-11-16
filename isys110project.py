import pandas as pd
import datetime

current_date = datetime.date.today()
formatted_date = current_date.strftime("%Y,%m,%d")

print ("Greeting customer, welcome to The Bloom House. " \
"We have the best arrangments of flowers just for you!\n")

#Using magic, reads the csv file and turns it into a dictionary.
#Prints the list of flowers and their price afterwards.
df = pd.read_csv('Project/Flower.csv')
flower_dict = df.set_index ('Flowers')['Price'].to_dict()
print (df.head(10), "\n")

#Variable is assigned to the user's input for what flowers they want to choose.
flower_arrangment_picked = input("Please choose" \
"a flower arrangment from our list.\n")
#The while loop will check to see if the variable flower_arrangment
#is the same as one of the key in the dictionary.
while True:
    #If it is true, it will print out the dedicated phrase and break the loop.
    if flower_arrangment_picked in flower_dict: 
        price = flower_dict[flower_arrangment_picked]
        print (f"\nThe cost for {flower_arrangment_picked} will be ${price}.")
        break
    #Else it will tell the user that their input doesn't match with any
    #keys in the dictionary and they will have to redo their input
    #until they match it with a corresponding key.
    else:
        print (f"\nSorry, but that's not a flower arrangement" \
           "in our list.")
        flower_arrangment_picked = input("Please try again.\n")

print ("Now that we know what you want, we will go through" \
"a speed round\n of all the totally nessesary information you" \
"need to tell us so we can sell you the flowers.\n")

#Asks the user for their information and checks to make sure it's not over or
#under or over the limit.
first_nam = input("Please tell us your first name.\n")
while len(first_nam) < (1):
    first_nam = input("\nSorry, but we need to know your first name.\n")

last_nam = input("\nPlease tell us your last name.\n")
while len(last_nam) < (1):
    last_nam = input("\nSorry, but we need to know your last name.\n")

address = input("\nPlease tell us your address.\n")
while len(address) < (1):
    address = input("\nSorry, but we need to know your address.\n")

email = input("\nPlease tell us your email.\n")
while len(email) < (5):
    email = input("\nSorry, but we need to know your email.\n")

phone = input("\nPlease tell us your phone number.\n")
while len(phone) < (10) or len(phone) > (10):
    phone = input("\nSorry, but we need to know your phone number.\n")

print("\nNow that we have your customer information, we need " \
"information regarding your delivery.\n")

#Asks the user for their information and checks to make sure it's not over or
#under or over the limit.
delivery_name = input("What is the name of your delivery?\n")
while len(delivery_name) < (1):
    delivery_name = input("\nSorry, but we need the name of the delivery.\n")

delivery_address = input("\nWhat is the address the delivery will be sent to?\n")
while len(delivery_address) < (1):
    delivery_address = input("\nSorry, but we need the address the" \
    "delivery will be sent to.\n")

delivery_date = input("\nWhen do you want the delivery sent?\n")
while len(delivery_date) < (1):
    delivery_date = input("\nSorry, but we need to know the date" \
    "the delivery will be sent.\n")

customer_name = [first_nam, last_nam]

#I know there is definitly a better way to print everything
#out in a vertical way, but I decided not to.
print("Your customer information is:")
print(*customer_name)
print(*address)
print(*email)
print(*phone)

print("Your order information is:")
print(*delivery_name)
print(*delivery_address)
print(*delivery_date)

tax_rate = 0.09
amount_tax = price * tax_rate
total_with_tax = price + amount_tax
print(f"${total_with_tax:.2f}")

#Compressing the variables into smaller "bits" for the program to use.
#Makes reading easier.
customer_info = [address, email, phone]
delivery_info = [delivery_name, delivery_address, delivery_date]

print("Order information: ", *customer_name, *customer_info, *delivery_info, f"${total_with_tax}")

#Creating the dictionary that will be turned into a csv file.
customer_data = {'Name' : customer_name,
            'Address' : address,
            'Email' : email,
            'Phone' : phone,
            'Delivery Name' : delivery_name,
            'Delivery Address' : delivery_address,
            'Delivery Date' : delivery_date,
            'Total With Tax' : total_with_tax}

#Turns the dictionary into a DataFrame.
customer_df = pd.DataFrame([customer_data])

#Makes the file name the customers name and the date.
filename = f"{customer_name}_{formatted_date}.csv"

#Adds the DataFrame to the csv file.
customer_df.to_csv(filename, index=False)

print(customer_df.head())