from assignment11.invoice import  Invoice
from invoice_item import  InvoiceItem
from product import Product
from customer import Customer
#Write import statements for classes AverageCustomer and GoodCustomer


'''
LOOK AT THE TEST CASES FOR HINTS
Create an invoice object ASSIGNMENT10: Make sure to change invoice bill_to argument to an instance of a Customer class 

In the loop:
Create a user controlled loop to continue until y is not typed, in loop...
    Prompt user for description, quantity, and cost.
    ASSIGNMENT10: Create a product object and add description and cost as parameter arguments.  Quantity remains same.
    Create a new InvoiceItem, use the newly created product as a parameter argument 
    Add values to the InvoiceItem.
    Add the InvoiceItem to the invoice object.
    Once user types a letter other than y display the Invoice to screen
'''


invoice1 = Invoice(Customer('Customer', 'Smith', '5121234567'), '03012018')
#see invoice creation above to complete next two statements
#ASSIGNMENT 11: Create an invoice instance named invoice2, with parameter instance of an Average Customer
#ASSIGNMENT 11: Create an invoice instance named invoice3, with parameter instance of an Good Customer

keep_going = 'y'

while keep_going == 'y':

    description = input("Enter description: ")
    quantity = int(input("Enter quantity: "))
    cost = float(input("Enter cost: "))

    invoice1.add_invoice_item(InvoiceItem(Product(1, description, cost), quantity))
    #see statement above to complete next two statements
    #ASSIGNMENT 11: add an invoice item to invoice 2 object with exact same Invoice item as invoice2 above
    #ASSIGNMENT 11: add an invoice item to invoice 3 object with exact same Invoice item as invoice3 above

    keep_going = input("Enter another type y: ")


print(invoice1.get_invoice_total())
print()
#ASSIGNMENT11: call get invoice total method of invoice2 object
print()
#ASSIGNMENT11: call get invoice total method of invoice3 object
print()

invoice1.print_invoice()
#ASSIGNMENT 11: call print invoice method of invoice 2 object
#ASSIGNMENT 11: call print invoice method of invoice 3 object




