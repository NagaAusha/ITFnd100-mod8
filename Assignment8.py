# ------------------------------- #
# Title: Assignment 08
# Description: Working with classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Naga Anusha,03.06.2022,Modified code to complete assignment 8
# ------------------------------------ 	#

# ---------Data-------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product:
    """Stores data about a product:

    properties:
    product_name: (string) with the product's name

    product_price: (float) with the product's standard price methods:
    to_string() returns comma separated product data (alias for str ())
    changelog: (When,Who,What)
    RRoot,1.1.2030,Created Class
    Naga Anusha , 03.06.2022, modified code to complete assignment 8

     """

    # -- Constructor --
    def __init__(self, product_name: str, product_price: float):
        """ Set name and price of a new object """
        try:
            self.__product_name = str(product_name)
            self.__product_price = float(product_price)
        except Exception as e:
            raise Exception("Error setting initial values: \n" + str(e))

    # -- Properties -- # product names
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value: str):
        if str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property        # product price
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value: float):
        if str(value).isnumeric():
            self.__product_price = float(value)
        else:
            raise Exception("Prices should be in numbers")

    # -- Methods --
    def to_string(self):  # converts data to string
        return self.str()

    def str(self):
        return self.__product_name + "," + str(self.__product_price)    # coverts product data to string


# ---------------Data-------------------- 	#

# --------------Processing--------------- 	#


class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods: save_data_to_file(file_name,list_of_product_objects):
    read_data_from_file(file_name): -> (a list of product objects)
    changelog: (When,Who,What)
    RRoot,1.1.2030,Created Class
    Naga Anusha, 03.06.2022, modified code to complete assignment8
    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_product_objects: list):
        """ Write data to a file from a list of product rows
        :param file_name: (string) with name of file
        :param list_of_product_objects: (list) of product objects data saved to file
        :return: (bool) with status of success status """
        success_status = False
        try:
            file = open(file_name, "w")
            for product in list_of_product_objects:
                file.write(product.str() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod      # process the data to file
    def read_data_from_file(file_name: str):

        list_of_product_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0], data[1])
                list_of_product_rows.append(row)
            file.close()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_product_rows


# Processing
# # Presentation (Input/Output) 		#


class IO:
    # class for performing Input and Output

    @staticmethod
    def print_menu_items():    # Display the menu of choices to the user

        print('''
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Save Data to File
        4) Exit Program ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():          # Gets the user choice from the menu
        print()  # Add an extra line for looks
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows: list):    # prints the current list of items in the row
        print("******* The current items products are: *******")
        for row in list_of_rows:
            print(row.product_name + " (" + str(row.product_price) + ")")
            print("*******************************************")
            print()  # Add an extra line for looks

    @staticmethod
    def input_product_data():           # Gets the data for product object and returns input object with data
        try:
            name = str(input("What is the product name? - ").strip())
            price = float(input("What is the price? - ").strip())
            print()  # Add an extra line for looks
            p = Product(product_name=name, product_price=price)
        except Exception as e:
            print(e)
        return p

    # -------------Presentation (Input/Output)--------------- 	#


# -----------Main Body of Script------------------------------- 	#
# Load data from file into a list of product objects when script starts
try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

    while True:     # Show user a menu of options
        IO.print_menu_items()
        # Get user's menu option choice
        strChoice = IO.input_menu_choice()
        if strChoice.strip() == '1':
            IO.print_current_list_items(lstOfProductObjects)     # Display the current data in the list to user
            continue
        elif strChoice.strip() == '2':
            lstOfProductObjects.append(IO.input_product_data())   # User can add data to the list of product object
            continue
        elif strChoice.strip() == '3':                           # User save current data to file and exit program
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            print("Data is saved")
            continue
        elif strChoice.strip() == '4':
            break
except Exception as e:
    print("There was an error! Check file permissions.")
    print(e, e.__doc__, type(e), sep='\n')

# Main Body of Script 	#


# Testing code: Products # print(Product. doc )
# p1 = Product("ProdA", 9.99) # print(p1.to_string())
# lstOfProductObjects.append(p1) #
# # Testing code: FileProcessor
# FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
# print(FileProcessor.read_data_from_file(strFileName))
#
# # Testing code: FileProcessor # IO.print_menu_items()
# print(IO.input_menu_choice())
# IO.print_current_list_items(lstOfProductObjects) # p2 = IO.input_product_data()
# lstOfProductObjects.append(p2) # for each in lstOfProductObjects: # print(each)
