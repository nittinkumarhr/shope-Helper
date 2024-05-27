#NOTE -  Shop is a class that has a list of items.
from email import message
import sqlite3
from tabulate import tabulate
import pywhatkit as pwk
from datetime import datetime

class Shop:
    def __init__(self,input_user):
        self.input_user = input_user
        self.con=sqlite3.connect(database="shop_db.db")
        self.cursor=self.con.cursor()
        print("Choice :",self.input_user)
        if self.input_user == 1:
            self.create_customer()
        elif self.input_user == 2:
            self.view_customer()
        elif self.input_user == 3:
            self.add_customer_loan()
        elif self.input_user == 4:
            self.add_customer_loan_Deposit()
        elif self.input_user == 5:
            self.delete_custmoer()
        else:
            print(" Invalid choice...!")
            
    def create_customer(self):
        print("++++++++++++++++++++Create Customer+++++++++++++++++++++++++++++\n")
        name =input("Customer Name :")
        phone =input("Customer Phone Number :")
        address=input("Customer Address :")
        self.c_dictionary={
            "name":name,
            "phone":phone,
            "address":address
        }
        self.createCustomer()


    def createCustomer(self):
        
        self.cursor.execute("insert into shope_data (name,phone,address,total_loan,deposit_loan,remaining_Amount)values(?,?,?,?,?,?) ",(self.c_dictionary["name"],self.c_dictionary["phone"],self.c_dictionary["address"],0,0,0))
        self.con.commit()
        print("\n :) Customer Add Suscefully.....")
        message=f"Dear *{self.c_dictionary['name']}*  \n\n Your Account is created successfully \n\n Your ID is :{self.cursor.lastrowid} \n\n  Your Phone Number is : {self.c_dictionary['phone'] } \n\n Your Address is : {self.c_dictionary['address']} \n\n Thank You For Using Our Services \n\n Regards \n\n *Shope*"
        self.send_whatsapp_message(self.c_dictionary["phone"],message)
        
        
        
        
    def view_customer(self):
        print("++++++++++++++++++++View Customer+++++++++++++++++++++++++++++\n")
        show_data=int(input("""\nview all Customer Details (Enter...1)\nview Customer Details by Name (Enter...2)"""))
        
        if self.con is not None:

            if show_data == 1:
                
                self.cursor.execute("select * from shope_data")
                
            elif show_data == 2:
                
                show_name=input("Enter the Name You want to Check :")
                self.cursor.execute("select * from shope_data where name=?",(show_name,))
                
            rows=self.cursor.fetchall()
            
            
            if rows:    
                
                headers = ['Customer id', 'Name', 'Phone','Address','Total Loan','Deposit Loan','Remaining Amount','created_at','updated_at']  # Modify this list to include desired columns
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            else:
                
                print(f"\t Error! => No data found for  {show_name}")

        else:
            
            print("\t Error! => Can not create the database connection.")
            
            
    def add_customer_loan(self):
        
        print("++++++++++++++++++++Add Customer Loan+++++++++++++++++++++++++++++\n")
        try: 

            add_loan=int(input("\n \t  If you want to add the loan customer account... Add by Id (Enter 1...)  "))
            
            loan_amount=input("\n Enter the Loan Rs :")
            id_input=int(input("\n Enter the Customer Id :"))
            total_lon=self.fetch_data(id_input,column_name='total_loan')
            if total_lon >=500:
                print("Dear Customer \n Your Total Loan is above  500. Please Deposit the loan") 
            else:
                if add_loan ==1:
                    
                    
                    number=self.get_phone_number(id_input)
                    name_input=self.fetch_data(id_input,column_name='name')
                    print("+++++++++++get Number ++++++++++++++++",number,name_input)

                    
                    self.cursor.execute(f"UPDATE shope_data SET total_loan = {loan_amount} WHERE Cid  = {id_input}")
                    
                    print("\n :) Loan Add Suscefully.....")
                    
                    self.con.commit()
                    message=f"Dear *{name_input}* \n Your Loan Rs *{loan_amount}* is added successfully \n Thanks for using our services \n Regards \n *Shope*"
                
                    self.send_whatsapp_message(number, message)
                    
            
                else:
                    
                    
                    print("\n Error! => Invalid choice...!")
                    
                    
        except Exception as e:
            print(f"\nError! => {e}")
        
      
        
        
    def get_phone_number(self, id):
    
        
        try:
            
            self.cursor.execute("SELECT phone FROM shope_data WHERE Cid = ?", (id,))
            row = self.cursor.fetchone()
            return row[0] if row else None
        
        
        except sqlite3.Error as e:
            
            
            print(f"An error occurred while fetching phone number: {e}")
            return None
        
        
    

        
    def send_whatsapp_message(self, phone_number, context):
        
            now = datetime.now()
            current_hour = now.hour
            current_minute = now.minute + 1
            print(current_hour, current_minute)
            # Using Exception Handling to avoid unexpected errors
            
       
            try:
                # Sending message in Whatsapp in India so using Indian dial code (+91)
                pwk.sendwhatmsg(f"+91{phone_number}", context, current_hour, current_minute, wait_time=30, tab_close=True, close_time=30)
                print("Message Sent!")

            except Exception as e:
                print(f"Error in sending the message: {e}")
                
    def  add_customer_loan_Deposit(self):
        
        print("++++++++++++++++++++Deposit Customer Loan +++++++++++++++++++++++++++++\n")
        
        deposit_id=int(input("\n Enter Customer ID : \n"))
        deposit_amount=int(input("\n Enter the Deposit Amount : \n"))
        total_lon=self.fetch_data(deposit_id,column_name='total_loan')
        
        
        if total_lon>=deposit_amount:
            
            self.cursor.execute(f"UPDATE shope_data SET deposit_loan = {deposit_amount}, remaining_Amount = {total_lon-deposit_amount}  WHERE Cid  = {deposit_id}")
        
            self.con.commit()
            print("\n :) Deposit Loan Suscefully.....")
            number=self.get_phone_number(deposit_id)
            name_input=self.fetch_data(deposit_id,column_name='name')
            message=f"Dear *{name_input}* \n Your Loan Rs *{deposit_amount}* is added successfully  Your remaining Loan is *{total_lon-deposit_amount}* \n Thanks for using our services \n Regards \n *Shope*"
            self.send_whatsapp_message(number, message) 
        else:     
            print("\n :( Sorry You can't Deposit Loan.....")                
        
        
        
    def fetch_data(self,data,column_name):
        
        self.cursor.execute(f"SELECT {column_name} FROM shope_data WHERE Cid = ?", (data,))
        row = self.cursor.fetchone()
        return row[0] if row else None
    def delete_custmoer(self):
        
        print("++++++++++++++++++++Delete Customer Account +++++++++++++++++++++++++++++\n")
        delete_id=int(input("\n Enter Customer ID : \n"))
        check=self.fetch_data(delete_id,delete_id)
        if check is None:
            print("\n :( Sorry! Customer is not exit ")
        else:
            self.cursor.execute(f"DELETE FROM shope_data WHERE Cid  = {delete_id}")
            self.con.commit()
            print("\n :) Customer Delete Suscefully.....")
            number=self.get_phone_number(delete_id)
            name_input=self.fetch_data(delete_id,column_name='name')
            message=f"Dear *{name_input}* \n Your Account is deleted successfully \n Thanks for using our services \n Regards \n *Shope*"
            self.send_whatsapp_message(number, message)
        
        

        

while True:
    if __name__ == "__main__":
        
        print("""Welcome to Customer Tracker App
            \n
            A. Create Customer (Enter... 1)
            B. View Customer Details AND Loan (Enter... 2)  
            C. Add Customer loan  (Enter... 3) 
            D. Deposit Loan  Customer Loan (Enter... 4)
            E. Delete the Customer Account (Enter... 5)
            f. Exit (Enter... 9)\n
            """)
        input_user= int(input("Enter your choice :"))
        
        if input_user == 9:
            break
            
        obj=Shop(input_user)
        print("\n \t Press any key to continue...")
        input()
        # con.close()
