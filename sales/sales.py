""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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
    table = data_manager.get_table_from_file('sales/sales.csv')
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
        get_lowest_price_item_id(table)
    elif option == "6":
        month_from = ui.get_inputs(['Please enter month_from: '], '')
        day_from = ui.get_inputs(['Please enter day_from: '], '')
        year_from = ui.get_inputs(['Please enter year_from: '], '')
        month_to = ui.get_inputs(['Please enter month_to: '], '')
        day_to = ui.get_inputs(['Please enter day_to: '], '')
        year_to = ui.get_inputs(['Please enter year_to: '], '')
        get_items_sold_between(
            table,
            month_from[0],
            day_from[0],
            year_from[0],
            month_to[0],
            day_to[0],
            year_to[0])
    elif option == "0":
        return 0
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Show table",
               "Add ithem",
               "Remove ithem",
               "Update ithem",
               "Lowest price item",
               "Items sold between"]

    ui.print_menu("Sales", options, "Back to main menu")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    ui.print_table(table, ['id', 'title', 'price', 'month', 'day', 'year'])


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
        ['title of item: ',
         'price of item: ',
         'month of item: ',
         'day of item: ',
         'year of item: '],
        'Adding item to Sales')
    addnew.insert(0, id)
    table.append(addnew)
    data_manager.write_table_to_file('sales/sales.csv', table)

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
        data_manager.write_table_to_file('sales/sales.csv', table)

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
                ['title of item: ',
                 'price of item: ',
                 'month of item: ',
                 'day of item: ',
                 'year of item: '],
                'Updating item of Sales')
            addnew.insert(0, id_)
            table[index] = addnew
            data_manager.write_table_to_file('sales/sales.csv', table)

    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code
    lowest_price = 100
    id_ = []
    title = []
    for line in table:
        if int(line[2]) < lowest_price:
            id_.clear()
            title.clear()
            lowest_price = int(line[2])
            id_.append(line[0])
            title.append(line[1])
        else:
            if int(line[2]) == lowest_price:
                id_.append(line[0])
                title.append(line[1])
    ui.print_result(sort_list(id_)[-1], 'The ID of lowest sold is')
    return sort_list(id_)[-1]


def sort_list(list1):
    for i in range(len(list1)):
        for j in range(len(list1) - 1):
            while list1[j] > list1[j + 1]:
                temp = list1.pop(j + 1)
                list1.insert(j, temp)
    return list1


def get_items_sold_between(table, month_from, day_from,
                           year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """
    filtered_table = []
    from_date = (int(year_from), int(month_from), int(day_from))
    to_date = (int(year_to), int(month_to), int(day_to))
    for row in table:
        if from_date < (int(row[-1]), int(row[-3]), int(row[-2])) < to_date:
            filtered_table.append(row)
    ui.print_result(
        filtered_table,
        'Items sold between ' +
        str(month_from) +
        '/' +
        str(day_from) +
        '/' +
        str(year_from) +
        '-' +
        str(month_to) +
        '/' +
        str(day_to) +
        '/' +
        str(year_to))
    for row in table:
        row[-1], row[-2], row[-3], row[-4] = int(
            row[-1]), int(row[-2]), int(row[-3]), int(row[-4])
    return filtered_table
