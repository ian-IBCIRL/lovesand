# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

print("Hello World")
print("Hello World2")
print("Hello World3")

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# open the google sheet
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# access the sales tab of the google sheet
sales = SHEET.worksheet('sales')

# get the google sheet data from the sales tab/worksheet
salesdata = sales.get_all_values()

# access the surplus sheet
surplussheet = SHEET.worksheet('surplus')

# get the data from the surplus sheet/tab
surplusdata = surplussheet.get_all_values()

# print the sales data obtained from the sales sheet of the workbook
print(salesdata)
print("--------------------")

# print the surplus data obtained from the surplus sheet of the workbook
print(surplusdata)


#function to get sales figures from the users
def get_sales_data():
    """
    Get sales figures input from the user, until valid data received
    """

    while (True):
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: \n")
        print(f"\nThe data provided is {data_str}")
        sales_data = data_str.split(",")
        if (validate_data(sales_data)):
            print("Data is valid!")
            break
    return sales_data


# function to validate data input to check it meets specification
def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        check_values = [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required. \nYou provided {len(values)} values as follows: "
                f"{check_values}"
            )
        return True
    except ValueError as errorv:
        print(f"\nInvalid data: {errorv}.\nPlease try again.\n")
        return (False)


# call the get sales data function defined above
input_sales_data = get_sales_data()
print(f"Sales data is {input_sales_data}")
