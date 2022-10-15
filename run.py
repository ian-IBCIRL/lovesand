# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pprint import pprint
import gspread
from google.oauth2.service_account import Credentials

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


def test_sheet_access():
    """
    Test sheet access
    python -c "from run import test_sheet_access;test_sheet_access()"
    """

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


# function to get sales figures from the users
# python -c "from run import get_sales_data  ; get_sales_data()"
def get_sales_data():
    """
    Get sales figures input from the user, until valid data received
    """

    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: \n")
        print(f"\nThe data provided is {data_str}")
        inp_sales_data = data_str.split(",")
        if validate_data(inp_sales_data):
            print("Data is valid!")
            break
    return inp_sales_data


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
                f"Exactly 6 values required. \n"
                f"You provided {len(values)} values as follows: "
                f"{check_values}"
            )
        return True
    except ValueError as errorv:
        print(f"\nInvalid data: {errorv}.\nPlease try again.\n")
        return False


def update_sales_worksheet(data):
    """
    update sales worksheet
    """
    print("Updating Sales Data\n")
    sales_worksheet = SHEET.worksheet("sales")
    try:
        if sales_worksheet.append_row(data):
            print("Sales data updated successfully")
    except gspread.exceptions.APIError as errorv:
        print(f"problem occured updating data.\n{errorv}")
        return False


def update_surplus_worksheet(data):
    """
    update surplus worksheet
    """
    print("Updating Surplus Data\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    try:
        if surplus_worksheet.append_row(data):
            print("Surplus data appended successfully")
    except gspread.exceptions.APIError as errorv:
        print(f"problem occured appending data.\n{errorv}")
        return False


def update_worksheet(data, worksheet):
    """
    update specified worksheet with specified data parameters
    """
    print(F"Updating {worksheet} Data\n")
    surplus_worksheet = SHEET.worksheet(worksheet)
    try:
        if surplus_worksheet.append_row(data):
            print(f"{worksheet} data appended successfully")
    except gspread.exceptions.APIError as errorv:
        print(f"problem occured appending data.\n{errorv}")
        return False


def calculate_surplus_stock(sales_row):
    """Calculate surplus stock

    Args:
        sales_row (_type_): sales data
    """
    print("Calculating Surplus Data\n")
    pprint(sales_row)
    stock_sheet = SHEET.worksheet("stock").get_all_values()
    pprint(stock_sheet)

    stock_str_data = stock_sheet[-1]
    print("stock row is: ", stock_str_data)

    # convert stock string data list to integer list
    # stock_row = [int(num) for num in stock_str_data]

    surplus_data = []
    for stock, sales in zip(stock_str_data, sales_row):
        print("stock: ", stock)
        print("sales: ", sales)
        surplus = int(stock) - sales
        print("surplus: ", surplus)
        surplus_data.append(surplus)
    print(surplus_data)
    return surplus_data


def main():
    """
    Main function to run all program functions
    """
    # call the get sales data function defined above
    input_data = get_sales_data()
    print(f"input string data is {input_data}")

    # convert sales string data list to integer list
    sales_data = [int(num) for num in input_data]

    # print integer list
    print(f"Sales integer data is {sales_data}")

    update_worksheet(sales_data, "sales")
    calc_surplus = calculate_surplus_stock(sales_data)
    print(calc_surplus)
    update_worksheet(calc_surplus, "surplus")


# to run use this command line - python -c "from run import main  ; main()"
print("Welcome to our sandwich data automation")
# call main function
main()
