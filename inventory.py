
#======== Classes & methods ==========
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        value = int(self.quantity) * int(self.cost)

        return f"${value}"
        
    def get_quantity(self):
        return int(self.quantity)

    # prints out a well spaced description of each object
    def __str__(self):
        output = f"\nProduct name: \t {self.product}\n"
        output += f"Product code: \t {self.code}\n"
        output += f"Made in: \t {self.country}\n"
        output += f"Price: \t\t${self.cost}\n"
        output += f"Quanity: \t {self.quantity}\n"
        
        return str(output)
    

#============= Shoe list ===========

# list will be used to store a list of objects of shoes.
shoe_list: list[Shoe] = []


#========== Functions ==============
def spacer():
    # this func help separate all the items in the printout
    print("\n======================================================\n")


def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    try:
        # opening the file as "r" read only
        with open("inventory.txt", "r") as inventory_file:
            # initializing the var that will hold the content
            inventory_content = inventory_file.readlines()

            print("\nHere is the inventory:")
            spacer()

            # looping through each line, and skipping the first one, to assign each part of the line to a specific variable
            for line in inventory_content[1:]:
                line = line.strip().split(",")
                
                country = line[0]
                code = line[1]
                product = line[2]
                cost = line[3]
                quantity = line[4]

                # creating a Shoe object with the data passed in from the inventory file 
                # and appending the shoes to the list
                shoes = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoes)
                
                # printing the output
                print(shoes)
                spacer()

    # error handling in case something goes wrong.
    except ValueError:
        spacer()
        print("ERROR: Something went wrong. Please try again.")
        spacer()


def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    try:
        print()
        # initilizing user input to add a new shoes in the inventory file
        shoes_name = input("Enter the name of the shoes: ").capitalize()
        shoes_code = input("Enter the code of the shoes: ").upper()
        shoes_country = input("Enter the production country: ").capitalize()
        shoes_price = int(input("Enter the price of the shoes: "))
        shoes_quantity = int(input("Enter the available quantity: "))
        
        # if any of the first three input is empty - throw an error
        if len(shoes_name) <= 0 or len(shoes_code) <= 0 or len(shoes_country) <= 0:
            spacer()
            print("ERROR: You cannot leave any of these spaces blank.")
            spacer()
            return
        
        #if the price or the quantity == 0 - throw an error
        if shoes_price <= 0:
            spacer()
            print("ERROR: Price cannot be 0 or lower. Try again.")
            spacer()
            return
        
        if shoes_quantity < 0:
            spacer()
            print("ERROR: Items quantity cannot go below 0. Try again.")
            spacer()
            return
        
        # creating and appending new shoe object
        user_captured_shoes = Shoe(shoes_country, shoes_code, shoes_name, shoes_price, shoes_quantity)
        shoe_list.append(user_captured_shoes)

        # writing it on the inventory file
        with open("inventory.txt", "a") as inventory_file:
            new_shoes = f"{shoes_country},{shoes_code},{shoes_name},{shoes_price},{shoes_quantity}\n"
            inventory_file.write(str(new_shoes))

        # print out a confirmation message
        spacer()
        print("Shoe succesfully added to the inventory.")
        spacer()
        
    # in case of weird input - throw an error
    except ValueError:
        spacer()
        print("ERROR: Shoes price and quantity should be full numbers")
        spacer()
        return


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python's tabulate module.
    '''
    # checking if the shoe_list is empty and printing out all the inventory
    if not shoe_list:
        print()
        print("Loading the inventory...")
        spacer()

        read_shoes_data()

    else:
        print("Here's the inventory:")

        for shoe in shoe_list:
            print(shoe.__str__())
            spacer()



def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # checking if the shoe_list is empty and printing out all the inventory
    if not shoe_list:
        print()
        print("Loading the inventory...")
        spacer()

        read_shoes_data()

    #initializing the var that will hold the shoe with the lowest stock
    low_stock_shoe = shoe_list[0]

    # checking each shoe and comparing the stock to then assign the lowest to the declared variable
    for shoe in shoe_list:
        if shoe.get_quantity() < low_stock_shoe.get_quantity():
            low_stock_shoe = shoe

    # printing out the final result
    print("Item with the lowest stock:")
    spacer()
    print(low_stock_shoe.__str__())
    spacer()

    # promprting the user with a new menu to restock the items in the inventory
    restock_menu = "This is the item with the lowest stock.\n"
    restock_menu += "Would you like to order more? (Yes/No)\n\n"
    restock_menu += ": ".lower()

    user_selection = input(restock_menu).lower()

    while True:
        #if the user wants to restock the items
        if user_selection[0] == "y":
            restock_order = "\n\nHow many items would you like to order?\n\n"
            restock_order += ": "

            user_order = int(input(restock_order))

            # updating the quantity of the shoes with low stock
            restocked_shoe = int(low_stock_shoe.quantity) + user_order

            # updating the stock of the shoe inside shoe_liist
            for shoe in shoe_list:
                if shoe == low_stock_shoe:
                    shoe.quantity = restocked_shoe

            # writing the whole shoe_list back to the inventory file
            with open("inventory.txt", "w") as inventory_file:
                for shoe in shoe_list:
                    new_inventory = f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
                    inventory_file.writelines(str(new_inventory))

            # printing out a successful print
            spacer()
            print("Stock successfully done!\n")
            print(f"You have now {restocked_shoe} pairs of {low_stock_shoe.product} in stock.")
            spacer()

            break
        # break the program if the userr doesn't want to stock any shoe
        # it goes back to main menu
        elif user_selection[0] == "n":
            break
        
        # handling wrong inputs
        else:
            spacer()
            print("ERROR: input not valid. Try again.")
            spacer()
            break


def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    # checking if the shoe_list is empty and printing out all the inventory
    if not shoe_list:
        print()
        print("Loading the inventory...")
        spacer()

        read_shoes_data()

    # asking user which item they are looking for 
    search_menu = input("\nPlease enter the code of the shoe model\n\n: ").upper()
    
    spacer()
    searched_code = search_menu

    # going through the list of shoes to match the item with the code given
    for shoe in shoe_list:
        if searched_code == shoe.code:
            print()
            print("Here is the item you are looking for:")
            spacer()
            print(shoe.__str__())
            spacer()
    
    # if there is not such code, go back to the main menu.
    # works with item found as confirmation too.
    print("Going back to the main menu.")
    spacer()
    
            

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    # printing out each item and its cost
    print("\nHere is a list of each item with its cost:")
    spacer()

    # fetching data for shoe_list
    if not shoe_list:
        read_shoes_data()

    else:
        for shoe in shoe_list:
            print(shoe.__str__())
            print(f"Total value: \t {shoe.get_cost()}")
            spacer()


def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    # checking if the shoe_list is empty and printing out all the inventory
    if not shoe_list:
        print()
        print("Loading the inventory...")
        spacer()

        read_shoes_data()

    #initializing the var that will hold the shoe with the highest stock
    highest_stock_shoe = shoe_list[0]

    # checking each shoe and comparing the stock to then assign the highest to the declared variable
    for shoe in shoe_list:
        if shoe.get_quantity() > highest_stock_shoe.get_quantity():
            highest_stock_shoe = shoe

    # printing out the final result
    print("Item with the highest stock:")
    spacer()
    print(highest_stock_shoe.__str__())
    print("Sale: \t\t 50 %\n\n")
    print(f"This shoe is on sale at: ${int(highest_stock_shoe.cost) / 2}")

    spacer()



#==========Main Menu=============
main_menu = """
Welcome to the Nike Storage!

Please select one of the following options:

======================================================

si  - See Inventory
as  - Add shoes
va  - View All Shoes
rs  - Restock Shoes
s   - Search Shoes
vpi - Value Per Item
hq  - Highest Quantity
e   - Exit

======================================================

: """

while True:
    user_selection = input(main_menu).lower()

    if user_selection == "si":
        read_shoes_data()

    elif user_selection == "as":
        capture_shoes()

    elif user_selection == "va":
        view_all()

    elif user_selection == "rs":
        re_stock()

    elif user_selection == "s":
        search_shoe()

    elif user_selection == "vpi":
        value_per_item()

    elif user_selection == "hq":
        highest_qty()

    elif user_selection == "e":
        spacer()
        print("Thank you! Good bye!")
        spacer()

        break

    else:
        spacer()
        print("ERROR: Input not recognized. Please, try again.")
        spacer()

        continue