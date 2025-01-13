# transaction-records
Practice project for developing CURD operation-capable web application using flask and deploy on the flask server

## The functions
Three separate web pages make up the application.

### View the transaction records
The first one shows every transaction that has been logged. This page, titled Transaction Records, shows every transaction entry made in the system. The option to modify or delete the available entries is also provided on this page. On this page, you can also choose to add an entry. 

### Add new transaction record
The Add Transaction page is the second page that appears after the user decides to add the entry from the previous page. The Date and Amount values are added by the user for the new entry. 

### Edit transaction
After selecting the edit entry option, the user is taken to the third page, Edit Transaction. The date and the amount are also permitted as entries on this page, but they are compared to the ID that was being changed.

### Delete the record
User can click delete to remove the record from the list.

## What I Learned
- "Create" operation to add transaction entry
- "Read" operation to access the list of transaction entries
- "Update" operation to update the details of a given transaction entry
- "Delete" operation to delete a transaction entry
- Use additional functions from Flask library for advanced routing and request management
- Manage routing between multiple HTML files as per requirement
