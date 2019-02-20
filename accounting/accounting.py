""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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

    # you code
    list_options = ['show_table','add', 'remove','update','which_year_max','avg']
    print_menu("Accounting", list_options, 'Back to Main Menu')
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
    table = data_manager.get_table_from_file('accounting/accounting.csv')
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
        year_max = ui.get_inputs(['Please enter a year: '], '')
        which_year_max(table)
    elif option == "6":
        avg(table)
    elif option == "0":
        return 0
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Show table",
               "Add item",
               "Remove item",
               "Update item",
               "Year of highest profit",
               "Average profit per item for a given year"]

    ui.print_menu("Accounting", options, "Back to main menu")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    ui.print_table(table, ['id', 'month', 'day',
                           'year', 'type', 'amount'])


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
        ['month: ', 'day: ', 'year: ', 'type (in=income, out= outflow): ', 'amount (of transaction in USD): '], 
        'Adding item to Accounting table')
    addnew.insert(0, id)
    table.append(addnew)
    data_manager.write_table_to_file('accounting/accounting.csv', table)

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
        data_manager.write_table_to_file('accouting/accounting.csv', table)

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
                ['month: ', 'day: ', 'year: ', 'type (in=income, out= outflow): ', 'amount (of transaction in USD): '], 
                'Updating item in Accounting table')
            addnew.insert(0, id_)
            table[index] = addnew
            data_manager.write_table_to_file('accounting/accounting.csv', table)

    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
