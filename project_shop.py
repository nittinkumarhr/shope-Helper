#NOTE -  Shop is a class that has a list of items.
import sqlite3
from tabulate import tabulate
import pywhatkit

class Shop:
    def __init__(self,input_user):
        self.input_user = input_user
        self.con=sqlite3.connect(database="shop_db.db")
        self.curser=self.con.cursor()
        print("Choice :",self.input_user)
        if self.input_user == 1:
            self.create_customer()
        elif self.input_user == 2:
            self.view_customer()
        elif self.input_user == 3:
            self.add_customer_loan()
        else:
            print(" Invalid choice...!")
    def create_customer(self):
        print("++++++++++++++++++++Create Customer+++++++++++++++++++++++++++++")
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
        
        self.curser.execute("insert into shope_data (name,phone,address,total_loan,deposit_loan,remaining_Amount)values(?,?,?,?,?,?) ",(self.c_dictionary["name"],self.c_dictionary["phone"],self.c_dictionary["address"],0,0,0))
        self.con.commit()
        print("\n :) Customer Add Suscefully.....")
        
    def view_customer(self):
        show_data=int(input("""\nview all Customer Details (Enter...1)\nview Customer Details by Name (Enter...2)"""))
        
        if self.con is not None:

            if show_data == 1:
                
                self.curser.execute("select * from shope_data")
            elif show_data == 2:
                show_name=input("Enter the Name You want to Check :")
                self.curser.execute("select * from shope_data where name=?",(show_name,))
                
            rows=self.curser.fetchall()
            if rows:    
                headers = ['Customer id', 'Name', 'Phone','Address','Total Loan','Deposit Loan','Remaining Amount']  # Modify this list to include desired columns
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            else:
                print(f"\t Error! => No data found for  {show_name}")

        else:
            print("\t Error! => Can not create the database connection.")
    def add_customer_loan(self):

        add_loan=int(input("\n \t  If you want to add the loan customer account... \n Add by Id (Enter 1...) \n Add by Name (Enter 2...)"))
        
        loan_ammount=input("\n Enter the Loan Rs :")
        if add_loan ==1:
            id_intput=int(input("\n Enter the Customer Id :"))
            d=self. get_number(name,id_intput)
            print("+++++++++++++++++++++get Number ++++++++++++++++",d)
            self.curser.execute(f"UPDATE shope_data SET total_loan = {loan_ammount} WHERE Cid  = {id_intput}")
            print("\n :) Loan Add Suscefully.....")
            self.con.commit()
        elif add_loan ==2:
            name_input=input("\n Enter the Customer Name :")
            self.curser.execute(f"""UPDATE shope_data SET total_loan = {loan_ammount} WHERE name ={name_input} """)
            print("\n :) Loan Add Suscefully.....")
            
            self.con.commit()
        else:
            print("\n Error! => Invalid choice...!")
    def get_number (self, choice='',id=0):
        
        self.curser.execute("select phone from shope_data where name=? or Cid=?",(choice,id))
        rows=self.curser.fetchall()
        return rows
        
    def send_whatsapp_message(self,phone_number,context):
        pass
    self.__display = Xlib.display.Display()
        
            


        
while True:
    if __name__ == "__main__":
        
        print("""Welcome to Customer Tracker App
            \n
            A. Create Customer (Enter... 1)
            B. View Customer Details AND Loan (Enter... 2)  
            C. Add Customer loan  (Enter... 3) 
            D. Exit (Enter... 5)\n
            """)
        input_user= int(input("Enter your choice :"))
        
        if input_user == 5:
            break
            
        obj=Shop(input_user)
        print("\n \t Press any key to continue...")
        input()
        # con.close()
