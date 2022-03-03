# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudocode to start assignment 8
# RLupinski,2.26.2022,Begin assignment
# RLupinski,2.27.2022,Updated and tested Product class
# RLupinski,3.1.2022, menu options, save/load to file, formatting fixes
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = "products.txt"
lstOfProductObjects = []


class Product(object):
    """Stores data about a product:
    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        RLupinski,02.26.2022,Modified code to complete assignment 8
        RLupinski,02.27.2022, setter/getter clean up
    """

    # -- Fields --
    # -- Constructor -- (special method that auto runs on instantiation)
    def __init__(self, product_name, product_price):
        # -- Attributes --
        self.__product_name = product_name  # sets product obj name
        self.__product_price = product_price  # sets product obj price

    # -- Properties -- (functions used to manage field attributes. setter/getter)
    # product_name
    @property
    def product_name(self):  # (getter or accessor)
        return str(self.__product_name).title()  # returns uppercase product name

    @product_name.setter  # (setter or mutator) checks if product name entered is numeric
    def product_name(self, value):
        if not str(value).isnumeric():  # if not numeric, set product name as value
            self.__product_name = value
        else:  # if numeric, raise exception
            raise Exception("Names cannot be numbers")

    # product_price
    @property
    def product_price(self):  # (getter or accessor)
        return self.__product_price  # returns float value

    @product_price.setter  # (setter or mutator) checks if product price entered is numeric
    def product_price(self, value):
        if str(value).isnumeric():  # if numeric, set price as value
            self.__product_price = value
        else:  # else raise exception
            raise Exception("Price must be a float")
    # -- Methods -- (Functions in a class)
    # --End of class--


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor(object):
    """Processes data to and from a file and a list of product objects:
    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        RLupinski,2.27.2022,Modified code to complete assignment 8
    """

    # -- Fields --
    # -- Constructor --
    # 	   -- Attributes --
    # -- Properties --
    # -- Methods --
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):  # save data to file
        file = open(file_name, "w+")  # open connection to file in write mode +
        for row in list_of_product_objects:  # for each row in list of objects
            file.write(str(row.product_name) + "," + str(row.product_price))  # write object to file
        file.close()  # close connection

    @staticmethod
    def read_data_from_file(file_name):  # read data from file
        lstOfProductObjects.clear()  # clear list of all data
        try:  # check to make sure the file exists
            with open(file_name, 'r') as file:  # open file in read mode
                for line in file:  # for each line in file
                    product_name, product_price = line.split(",")  # split each line and save to vars
                    product = Product(product_name=product_name, product_price=product_price)  # make product list
                    lstOfProductObjects.append(product)  # append each product to list of product objects
                return lstOfProductObjects  # return the list of product objects
        except:  # if the file doesn't exist
            print("File \'product.txt\' not found")
            print("Creating a new file")
            with open(file_name, 'w') as file:  # create a new file
                file.write("Product,Price\n")  # write header to file


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    # TODO: Add code to show menu to user
    @staticmethod
    def print_menu_of_options():  # print a menu of options
        """  Display a menu of options to the user
        :return: nothing
        """
        print('''
    Menu of Options
    1) Add a new Product
    2) Save Data to File        
    3) Reload Data from File
    4) Exit Program
            ''')

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():  # get menu choice from user
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice  # strip newline from choice var and return value

    @staticmethod
    def print_current_list(list_of_products):  # list all products in current list
        print("***************************")
        print("Current Products List:")
        for product in list_of_products:  # for each product in list of product objects
            print(product.product_name + "," + product.product_price, sep="", end="")  # print the name and price
        print("***************************")
        return

    # TODO: Add code to get product data from user
    @staticmethod
    def add_product_to_list(new_product, list_of_products):  # add product to list
        list_of_products.append(new_product)  # append list of product w/ new product
        return list_of_products  # return list of products

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing
        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')


# Presentation (Input/Output)  -------------------------------------------- #

# Custom Exception Class  --------------------------------------------------- #
class ProductNameError(Exception):
    """Can not have numeric entry for product name"""

    @staticmethod
    def __int__(self):  # custom error handling example for when a non-alphanumeric name is tried
        return 'Can not have numeric entry for product name'


class ProductPriceError(Exception):
    """Can not have alphanumeric entry for product price"""

    @staticmethod
    def __int__(self):  # custom error handling example for when a non-alphanumeric name is tried
        return 'Can not have alphanumeric entry for product price'


# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

while True:
    IO.print_current_list(lstOfProductObjects)  # show the current list of products
    IO.print_menu_of_options()  # Show user a menu of options
    strChoice = IO.input_menu_choice()  # Gets user's menu option choice

    if strChoice.strip() == '1':  # Let user add data to the list of product objects
        try:
            strNewProduct = str(input("Add a Product: "))  # prompt user to add a Product
            if strNewProduct.isnumeric():  # if name is numeric
                raise ProductNameError()  # raise custom error
            strNewPrice = str(input("Add Price: ") + "\n")  # prompt user to define Price
            if strNewPrice.strip().isalpha():  # if price is alphanumeric
                raise ProductPriceError()  # raise custom error
            objNewProduct = Product(product_name=strNewProduct, product_price=strNewPrice)  # create new object
            IO.add_product_to_list(objNewProduct, lstOfProductObjects)  # add product to current list
            IO.input_press_to_continue()  # hold for user
        except ValueError as e:
            print("Price must be a number")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')  # return python error docs
        except Exception as e:  # generic catch-all error exception
            print("There was a non-specific error!")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')  # return python error docs

    elif strChoice == '2':  # let user save current data to file and exit program
        strChoice = input("Do you want to save the product list to the file?\n"
                          "Continue: (y/n)")  # option to abort saving to file
        if strChoice == 'y':
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)  # save data to file
            print(f"Data saved to {strFileName}!")
        else:
            print("Save aborted")
        IO.input_press_to_continue()  # hold for user

    elif strChoice == '3':
        strChoice = input("WARNING: THIS WILL OVERWRITE UNSAVED DATA\n"
                          "Continue: (y/n)")  # option to abort loading from file
        if strChoice == 'y':
            lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)  # load data from file
            print(f"Data from {strFileName} loaded!")
            IO.input_press_to_continue()  # hold for user
        else:
            print("Data load aborted")
            IO.input_press_to_continue()  # hold for user
    elif strChoice == '4':
        strChoice = input("WARNING: EXITING PROGRAM. UNSAVED DATA WILL BE LOST\n"
                          "Continue: (y/n)")  # option to abort exiting program
        if strChoice == 'y':
            print("Goodbye")
            break
        else:
            print("Exit program aborted")
            IO.input_press_to_continue()  # hold for user
    else:
        print("Must choose options 1 - 4")
        IO.input_press_to_continue()  # hold for user

# Main Body of Script  ---------------------------------------------------- #
