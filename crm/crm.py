""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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
    table = data_manager.get_table_from_file('crm/customers.csv')
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
        get_longest_name_id(table)
    elif option == "6":
        get_subscribed_emails(table)
    elif option == "7":
        id_ = ui.get_inputs(['Please enter an id: '], '')
        get_name_by_id(id_[0])
    elif option == "8":
        id_ = ui.get_inputs(['Please enter an id: '], '')
        get_name_by_id_from_table(table, id_[0])
    elif option == "0":
        return 0
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Show table",
               "Add item",
               "Remove item",
               "Update item",
               "ID of the longest name",
               "List of customers who subscribed",
               "Customer's name for a given ID with Data Manager",
               "Customer's name for a given ID"]

    ui.print_menu("CRM", options, "Back to main menu")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    ui.print_table(table, ['id', 'name', 'email',
                           'subscribed'])


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
        ['Customer name: ', 'E-mail address: ',
            'Subscribed (Please enter 1 if yes, 0 if not yet): '],
        'Adding customer to CRM database')
    addnew.insert(0, id)
    table.append(addnew)
    data_manager.write_table_to_file('crm/customers.csv', table)

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
        data_manager.write_table_to_file('crm/customers.csv', table)

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
                ['Name of customer: ', 'E-mail address: ', 'Subscribed: '],
                'Updating customer in CRM database')
            addnew.insert(0, id_)
            table[index] = addnew
            data_manager.write_table_to_file('crm/customers.csv', table)

    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    len_of_names = []
    maxi_names = []
    for lines in table:
        len_of_names.append(len(lines[1]))
    max_len = max(len_of_names)
    for lines in table:
        if len(lines[1]) == max_len:
            maxi_names.append(lines[1])
    for lines in table:
        if lines[1] == max(maxi_names):
            ui.print_result(
                lines[0],
                "The ID of the customer with the longest name")
            return lines[0]


def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    subs = []
    printable_list = []
    for line in table:
        if line[-1] == "1":
            subs.append(line[2] + ";" + line[1])
    printable_list = [[item] for item in subs]
    ui.print_result(printable_list, "Subscribers' email addresses and their names")

    return subs
    # your code


# functions supports data analyser
# --------------------------------


def get_name_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """
    table = data_manager.get_table_from_file('crm/customers.csv')
    for lines in table:
        if lines[0] == id:
            return lines[1]
    # your code


def get_name_by_id_from_table(table, id):
    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """
    for lines in table:
        if lines[0] == id:
            ui.print_result(lines[1], 'Name of customer with given ID: ')
            return lines[1]
    # your code