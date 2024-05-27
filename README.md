# Customer Tracker App
This application is designed to manage customer data for a shop. It provides functionalities to create, view, update, and delete customer records, as well as handle customer loans. It also integrates with WhatsApp to send notifications to customers.


## Customer Tracker App
This application is designed to manage customer data for a shop. It provides functionalities to create, view, update, and delete customer records, as well as handle customer loans. It also integrates with WhatsApp to send notifications to customers.

Prerequisites
Make sure you have the following Python packages installed:

sqlite3 (comes pre-installed with Python)
tabulate
pywhatkit
You can install tabulate and pywhatkit using pip:

pip install tabulate
pip install pywhatkit


### 1. Create a Customer

To create a new customer, use the `create_customer` function. This function takes the following parameters:

`name`: The name of the customer.

`phone_number`: The phone number of the customer.

`address`: The address of the customer.

`email`: The email address of the customer.

`loan_amount`: The amount of the loan (optional).

For example:

```
create_customer("John Doe", "+1234567890", "123 Main St", "johndoe@example.com", 1000)

```

## Features

* Create Customer: Adds a new customer to the database.
* View Customer: Displays all customers or a specific customer by name.
* Add Customer Loan: Adds a loan amount to the customer's account.
* Deposit Customer Loan: Allows a customer to deposit a loan amount.
* Delete Customer: Removes a customer from the database.
* WhatsApp Notification: Sends a notification to the customer for each operation using WhatsApp.


### 2. View Customer Details

To view customer details, use the `view_customer` function. This function takes the following parameters:

`customer_id`: The ID of the customer.

For example:

```
view_customer(1)

```

### 3. Add Customer Loan

To add a loan amount to a customer's account, use the `add_loan` function. This function takes the following parameters:

`customer_id`: The ID of the customer.

`loan_amount`: The amount of the loan.

For example:

```
add_loan(1, 500)

```

### 4. Deposit Customer Loan

To deposit a loan amount to a customer's account, use the `deposit_loan` function. This function takes the following parameters:

`customer_id`: The ID of the customer.

`loan_amount`: The amount of the loan.

For example:

```
deposit_loan(1, 200)

```

### 5. Delete Customer

To delete a customer from the database, use the `delete_customer` function. This function takes the following parameters:

`customer_id`: The ID of the customer.

For example:

```
delete_customer(1)

```

### 6. WhatsApp Notification

To send a notification to a customer using WhatsApp, use the `send_whatsapp_notification` function. This function takes the following parameters:

`customer_id`: The ID of the customer.

`message`: The message to be sent.

For example:

```
    send_whatsapp_notification(1, "Your loan amount has been added successfully.")

```

## 7. View Customer Loans

To view all loans for a customer, use the `view_customer_loans` function. This function takes the following parameters:

`customer_id`: The ID of the customer.

For example:

```
    view_customer_loans(1)

```

### 8. View Customer Deposits

To view all deposits for a customer, use the `view_customer_deposits` function. This function takes the following parameters:

`customer_id`: The ID of the customer.

For example:

```
    view_customer_deposits(1)

```

### 9. View Customer Notifications

To view all notifications for a customer, use the `view_customer_notifications` function. This function takes the following parameters:

        
# CUI Based Application with Python

This is a CUI based application that allows users to interact with a customer database using a command-line interface. The application supports the following functions:

- View all customers
- View a specific customer
- Add a new customer
- Add a loan amount to a customer's account
- Deposit a loan amount to a customer's account
- Delete a customer from the database
- Send a WhatsApp notification to a customer
- View all loans for a customer
- View all deposits for a customer
- View all notifications for a customer
