""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
    * customer_id (string): id from the crm
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
    elif option == "7":
        id = ui.get_inputs(['Please enter the specified id: '], '')
        get_title_by_id(id[0])
    elif option == "8":
        id = ui.get_inputs(['Please enter the specified id: '], '')
        get_title_by_id_from_table(table, id[0])
    elif option == "9":
        get_item_id_sold_last()
    elif option == "10":
        get_item_id_sold_last_from_table(table)
    elif option == "11":
        get_item_title_sold_last_from_table(table)
    elif option == "12":
        item_ids_no = ui.get_inputs(['How many IDs do you want to enter? '], '')
        item_ids = ui.get_inputs(['Enter ID ' + str(index + 1) + ': ' for index in range(int(item_ids_no[0]))], '')
        get_the_sum_of_prices(item_ids)
    elif option == "13":
        item_ids_no = ui.get_inputs(['How many IDs do you want to enter? '], '')
        item_ids = ui.get_inputs(['Enter ID ' + str(index + 1) + ': ' for index in range(int(item_ids_no[0]))], '')
        get_the_sum_of_prices_from_table(table, item_ids)
    elif option == "14":
        sale_id = ui.get_inputs(['Please enter the sale id: '], '')
        get_customer_id_by_sale_id(sale_id[0])
    elif option == "15":
        sale_id = ui.get_inputs(['Please enter the sale id: '], '')
        get_customer_id_by_sale_id_from_table(table, sale_id[0])
    elif option == "16":
        get_all_customer_ids()
    elif option == "17":
        get_all_customer_ids_from_table(table)
    elif option == "18":
        get_all_sales_ids_for_customer_ids()
    elif option == "19":
        get_all_sales_ids_for_customer_ids_form_table(table)
    elif option == "20":
        get_num_of_sales_per_customer_ids()
    elif option == "21":
        get_num_of_sales_per_customer_ids_from_table(table)
    elif option == "0":
        return 0
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Show table",
               "Add item",
               "Remove item",
               "Update item",
               "Lowest price item",
               "Items sold between",
               "Get title by id",
               "Get title by id from table",
               "Get item id sold last",
               "Get item id sold last from table",
               "Get item title sold last from table",
               "Get the sum of prices",
               "Get the sum of prices from table",
               "Get customer id by sale id",
               "Get customer id by sale id from table",
               "Get all customer ids",
               "Get all customer ids from table",
               "Get all sales ids for customer ids",
               "Get all sales ids for customer ids form table",
               "Get num of sales per customer ids",
               "Get num of sales per customer ids from table"]

    ui.print_menu("Sales", options, "Back to main menu")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    ui.print_table(table, ['id', 'title', 'price', 'month', 'day', 'year', 'sale id'])


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

    # 5
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
    # 6
    
    filtered_table = []
    from_date = (int(year_from), int(month_from), int(day_from))
    to_date = (int(year_to), int(month_to), int(day_to))
    for row in table:
        if from_date < (int(row[5]), int(row[3]), int(row[4])) < to_date:
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
        row[5], row[4], row[3], row[2] = int(
            row[5]), int(row[4]), int(row[3]), int(row[2])
    return filtered_table


# functions supports data abalyser
# --------------------------------


def get_title_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # 7

    result = ''
    table = data_manager.get_table_from_file('sales/sales.csv')
    for row in table:
        if row[0] == id:
            result += row[1]
    return result


def get_title_by_id_from_table(table, id):

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """
    
    # 8

    result = ''
    for row in table:
        if row[0] == id:
            result += row[1]
    ui.print_result(result, 'The title of the given ID is')
    return result


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # 9
    table = data_manager.get_table_from_file('sales/sales.csv')
    date = (1970, 1, 1)
    item_id = ''
    for row in table:
        if date < (int(row[5]), int(row[3]), int(row[4])):
            date = (int(row[5]), int(row[3]), int(row[4]))
            item_id = row[0]
    return item_id


def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # 10
    date = (1970, 1, 1)
    item_id = ''
    for row in table:
        if date < (int(row[5]), int(row[3]), int(row[4])):
            date = (int(row[5]), int(row[3]), int(row[4]))
            item_id = row[0]
    ui.print_result(item_id, 'The last sold item is')
    return item_id


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _title_ of the item that was sold most recently.
    """

    # 11
    date = (1970, 1, 1)
    title = ''
    for row in table:
        if date < (int(row[5]), int(row[3]), int(row[4])):
            date = (int(row[5]), int(row[3]), int(row[4]))
            title = row[1]
    ui.print_result(title, 'The last sold item is')
    return title


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # 12
    table = data_manager.get_table_from_file('sales/sales.csv')
    sum_of_items = 0
    for row in table:
        if row[0] in item_ids:
            sum_of_items += int(row[2])
    return sum_of_items


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # 13
    sum_of_items = 0
    for row in table:
        if row[0] in item_ids:
            sum_of_items += int(row[2])
    ui.print_result(sum_of_items, 'The sum in USD')
    return sum_of_items


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
         sale_id (str): sale id to search for
    Returns:
         str: customer_id that belongs to the given sale id
    """

    # 14
    table = data_manager.get_table_from_file('sales/sales.csv')
    cust_id = ''
    for row in table:
        if row[0] == sale_id:
            cust_id = row[6]
    if cust_id == '':
        return None
    return cust_id


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """

    # 15
    cust_id = ''
    for row in table:
        if row[0] == sale_id:
            cust_id = row[6]
    if cust_id == '':
        cust_id = 'None'
    ui.print_result(cust_id, 'Customer ID')
    return cust_id


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.

    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # 16

    table = data_manager.get_table_from_file('sales/sales.csv')
    result = {i[6] for i in table}
    return result


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # 17

    result = {i[6] for i in table}
    ui.print_result([[i] for i in result], 'All customer IDs from table')
    return result


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
            all the sales id belong to the given customer_id
    """

    # 18
    table = data_manager.get_table_from_file('sales/sales.csv')
    ids = {}
    for row in table:
        ids[row[6]] = ids.get(row[6], []) + [row[0]]
    return ids


def get_all_sales_ids_for_customer_ids_form_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # 19
    ids = {}
    for row in table:
        ids[row[6]] = ids.get(row[6], []) + [row[0]]
    #ui.print_result(ids, 'Sales IDs per customer')
    return ids


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    table = data_manager.get_table_from_file('sales/sales.csv')
    ids = {}
    for row in table:
        ids[row[6]] = ids.get(row[6], 0) + 1
    ui.print_result(ids, 'Number of sales per customer IDs')
    return ids
    # 20


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # 21
    ids = {}
    for row in table:
        ids[row[6]] = ids.get(row[6], 0) + 1
    return ids
