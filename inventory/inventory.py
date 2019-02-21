""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    while True:
        handle_menu()
        try:
            if choose() == 0:
                break
        except KeyError as err:
            ui.print_error_message(str(err))


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    table = data_manager.get_table_from_file('inventory/inventory.csv')
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        id_ = ui.get_inputs(['Please enter an id: '], '')
        remove(table, id_[0])
    elif option == "4":
        id_ = ui.get_inputs(['Please enter an id: '], '')
        update(table, id_[0])
    elif option == "5":
        get_available_items(table)
    elif option == "6":
        get_average_durability_by_manufacturers(table)
    elif option == "0":
        return 0
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Show table",
               "Add item",
               "Remove item",
               "Update item",
               "Get aviable items",
               "Average durability"]

    ui.print_menu("Inventory", options, "Back to main menu")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    ui.print_table(table, ['id', 'name', 'manufacturer',
                           'purchase_year', 'durability'])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    id = common.generate_random(table)
    addnew = ui.get_inputs(
        ['name of item: ',
         'manufacturer of item: ',
         'purchase_year of item: ',
         'durability of item: '],
        'Adding item to Inventory')
    addnew.insert(0, id)
    table.append(addnew)
    data_manager.write_table_to_file('inventory/inventory.csv', table)

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    for index in range(len(table)):
        if table[index][0] == id_:
            table.pop(index)
        data_manager.write_table_to_file('inventory/inventory.csv', table)

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    for index in range(len(table)):
        if table[index][0] == id_:
            addnew = ui.get_inputs(
                ['name of item: ',
                 'manufacturer of item: ',
                 'purchase_year of item: ',
                 'durability of item: '],
                'Updating item of Inventory')
            addnew.insert(0, id_)
            table[index] = addnew
            data_manager.write_table_to_file('inventory/inventory.csv', table)

    return table


# special functions:
# ------------------

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    rtable = []
    for lines in table:
        lines[-2] = int(lines[-2])
        lines[-1] = int(lines[-1])
        if lines[-2] + lines[-1] >= 2017:
            rtable.append(lines)
    ui.print_result(rtable, '\nAviable items:')
    return rtable


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """
    manufacturer_list = list(set(i[2] for i in table))
    manufacturer_dict = {i: 0 for i in manufacturer_list}
    for key in manufacturer_list:
        counter = 0
        years_total = 0
        for lines in table:
            if lines[2] == key:
                manufacturer_dict[key] += int(lines[4])
                years_total += int(lines[4])
                counter += 1
        manufacturer_dict[key] = years_total / counter

    ui.print_result(manufacturer_dict, '\nAverage durability by manufacturer:')
    return manufacturer_dict
