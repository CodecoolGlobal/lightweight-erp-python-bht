""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
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
    hr_menu_options = inputs[0]
    table = data_manager.get_table_from_file('hr/persons.csv')
    if hr_menu_options == '1':
        show_table(table)
    elif hr_menu_options == '2':
        add(table)
    elif hr_menu_options == '3':
        remove(
            table,
            ui.get_inputs(
                ['id'],
                'Which id you want removed? \n')[0])
    elif hr_menu_options == '4':
        update(
            table,
            ui.get_inputs(
                ['id'],
                'Which id you want updated? \n')[0])
    elif hr_menu_options == '5':
        get_oldest_person(table)
    elif hr_menu_options == '6':
        get_persons_closest_to_average(table)
    elif hr_menu_options == '0':
        return 0


def handle_menu():
    store_menu = [
        'Show table',
        'Add item',
        'Remove item',
        'Update item',
        'Oldest person',
        'People closest to average']
    ui.print_menu('HR', store_menu, 'Back to main menu')


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code
    ui.print_table(table, ['id', 'name', 'birth_year'])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code
    id = common.generate_random(table)
    addnew = ui.get_inputs(
        ['name: ', 'birth_year: '],
        'Adding entry to hr')
    addnew.insert(0, id)
    table.append(addnew)
    data_manager.write_table_to_file('hr/persons.csv', table)
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
        data_manager.write_table_to_file('hr/persons.csv', table)
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

    # your code
    for index in range(len(table)):
        if table[index][0] == id_:
            addnew = ui.get_inputs(
                ['name: ', 'birth_year: '],
                'Updating list of hr')
            addnew.insert(0, id_)
            table[index] = addnew
            data_manager.write_table_to_file('hr/persons.csv', table)
    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code
    oldest_name = []
    oldest = 2000
    for line in table:
        if line[2] < str(oldest):
            oldest_name.clear()
            oldest = line[2]
            oldest_name.append(line[1])
        elif line[2] == str(oldest):
            oldest = line[2]
            oldest_name.append(line[1])
    ui.print_result(oldest_name, "The oldest is/are: \n")
    return oldest_name


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
    total = 0
    dividor = 0
    for line in table:
        total += int(line[2])
        dividor += 1
    avg = total / dividor
    diff = 1000
    closest = []
    for line in table:
        if abs(int(line[2]) - avg) < diff:
            closest.clear()
            diff = abs(int(line[2]) - avg)
            closest.append(line[1])
        elif abs(int(line[2]) - avg) == diff:
            closest.append(line[1])
    ui.print_result(closest, '\nClosest PEOPLE to average: ')
    return closest
