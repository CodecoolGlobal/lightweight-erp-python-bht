"""
This module creates reports for the marketing department.
This module can run independently from other modules.
Has no own data structure but uses other modules.
Avoud using the database (ie. .csv files) of other modules directly.
Use the functions of the modules instead.
"""

# todo: importing everything you need

# importing everything you need
import ui
import common
from sales import sales
from crm import crm


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
    option = inputs[0]
    if option == "1":
        get_the_last_buyer_name()
    elif option == "2":
        get_the_last_buyer_id()
    elif option == "3":
        get_the_buyer_name_spent_most_and_the_money_spent()
    elif option == "4":
        get_the_buyer_id_spent_most_and_the_money_spent()
    elif option == "5":
        get_the_most_frequent_buyers_names()
    elif option == "6":
        get_the_most_frequent_buyers_ids()
    elif option == "0":
        return 0
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Last buyer name",
               "Last buyer id",
               "Most spent buyer name",
               "Most spent buyer id",
               "Most ferquent buyer name",
               "Most frequent buyer id"]

    ui.print_menu("Data analyser", options, "Back to main menu")


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """

    # 1
    sale_id = sales.get_item_id_sold_last()
    buyer_id = sales.get_customer_id_by_sale_id(sale_id)
    buyer_name = crm.get_name_by_id(buyer_id)
    return buyer_name


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """

    # 2
    sale_id = sales.get_item_id_sold_last()
    buyer_id = sales.get_customer_id_by_sale_id(sale_id)
    return buyer_id


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """

    # 3
    most_sales = sales.get_num_of_sales_per_customer_ids()
    id_ = ''
    for key, value in most_sales.items():
        if value == max(most_sales.values()):
            id_ = key
    name = crm.get_name_by_id(id_)
    all_sale_ids = sales.get_all_sales_ids_for_customer_ids()
    sum_sales = sales.get_the_sum_of_prices(all_sale_ids[id_])
    return (name, sum_sales)


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """

    # 4
    most_sales = sales.get_num_of_sales_per_customer_ids()
    id_ = ''
    for key, value in most_sales.items():
        if value == max(most_sales.values()):
            id_ = key
    all_sale_ids = sales.get_all_sales_ids_for_customer_ids()
    sum_sales = sales.get_the_sum_of_prices(all_sale_ids[id_])
    return (id_, sum_sales)


def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """

    # 5
    most_sales = sales.get_num_of_sales_per_customer_ids()
    most_frequent = []
    for number in range(num):
        id_ = ''
        for key, value in most_sales.items():
            if value == max(most_sales.values()):
                id_ = key
        name = crm.get_name_by_id(id_)
        most_frequent.append((name, max(most_sales.values())))
        most_sales.pop(id_)
    return most_frequent


def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]
    """

    # 6
    most_sales = sales.get_num_of_sales_per_customer_ids()
    most_frequent = []
    for number in range(num):
        id_ = ''
        for key, value in most_sales.items():
            if value == max(most_sales.values()):
                id_ = key
        most_frequent.append((id_, max(most_sales.values())))
        most_sales.pop(id_)
    return most_frequent
