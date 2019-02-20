""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
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

    # your code
    while True:
        handle_menu()
        try:
            if choose() == 0:
                break
        except KeyError as err:
            ui.print_error_message(str(err))


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    store_menu_options = inputs[0]
    table = data_manager.get_table_from_file('store/games.csv')
    if store_menu_options == '1':
        show_table(table)
    elif store_menu_options == '2':
        add(table)
    elif store_menu_options == '3':
        remove(
            table,
            ui.get_inputs(
                ['id'],
                'Which id you want removed? \n')[0])
    elif store_menu_options == '4':
        update(
            table,
            ui.get_inputs(
                ['id'],
                'Which id you want updated? \n')[0])
    elif store_menu_options == '5':
        get_counts_by_manufacturers(table)
    elif store_menu_options == '6':
        get_average_by_manufacturer(
            table,
            ui.get_inputs(
                ['manufacturer'],
                'Which manufacturer are you interested in? \n')[0])
    elif store_menu_options == '0':
        return 0


def handle_menu():
    store_menu = ['Show Table', 'Add', 'Remove', 'Update', 'Count', 'Avg']
    ui.print_menu('Store Menu', store_menu, 'Back to Main Menu')


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    # your code

    games_title_list = ['id', 'title', 'manufacturer', 'price', 'in_stock']
    ui.print_table(table, games_title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code a \n mehetne a get_inputsba, és egy : is a dupla space helyett
    gen_id = common.generate_random(table)
    input_parameters = ['title', 'manufacturer', 'price', 'in_stock']
    add_line = []
    add_line.append(gen_id)
    add_line.extend(
        ui.get_inputs(
            input_parameters,
            'Please enter the following: \n'))
    table.append(add_line)
    data_manager.write_table_to_file('store/games.csv', table)
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

    # your code
    for index in range(len(table)):
        if table[index][0] == id_:
            table.pop(index)
        data_manager.write_table_to_file('store/games.csv', table)

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    for index in range(len(table)):
        if table[index][0] == id_:
            addnew = ui.get_inputs(
                ['title', 'manufacturer', 'price', 'in_stock'],
                'Updating item of store')
            addnew.insert(0, id_)
            table[index] = addnew
        data_manager.write_table_to_file('store/games.csv', table)
    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code
    dict1 = {}
    for line in table:
        if line[2] in dict1.keys():
            dict1[line[2]] += 1
        else:
            dict1[line[2]] = 1

    return ui.print_result(
        dict1, '\nManufacturers have the following amount of games: \n')


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
    count = 0
    divider = 0
    for line in table:
        if line[2] == manufacturer:
            count = count + int(line[4])
            divider += 1
    result = count / divider
    return ui.print_result(result, '\nAverage amt of games in stock: ')
