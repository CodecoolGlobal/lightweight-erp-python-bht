'''
    User Interface (UI) module
    Prints table with data.
    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/
    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers
    Returns:
    None: This function doesn't return anything it only prints to console.
'''


def print_table(table, title_list):
    ltitle = []
    for i in title_list:
        ltitle.append(len(i))
    for lines in table:
        for index in range(len(lines)):
            if len(lines[index]) > ltitle[index]:
                ltitle[index] = len(lines[index])
    tw = len(table)+4
    for i in ltitle:
        tw += i
    print(ltitle)
    print(tw)       
    print('\n\t/'+'-'*tw+'\\')
    print('\t| {:^8} | {:^20} | {:^12} | {:^13} | {:^10} | '.format(title_list[0], title_list[1], title_list[2], title_list[3], title_list[4]))
    for item in table:
        print('\t|'+'-'*tw+'|')
        print('\t' + '| ' + ' | '.join(item) + ' |')
    print('\t\\'+'-'*tw+'/\n')


'''
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.

     your code
'''


def print_result(result, label):
    pass


'''
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    your code
'''


def print_menu(title, list_options, exit_message):
    print(title)
    for item_no, item in enumerate(list_options):
        print('\t(' + str(item_no + 1) + ') ' + item)
    print('\t(0) ' + exit_message)


'''
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>
'''


def get_inputs(list_labels, title):
    inputs = []
    print(title)
    for labels in list_labels:
        item = input(labels + ' ')
        inputs.append(item)

    return inputs


'''
    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"
    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.

     your code
'''


def print_error_message(message):
    print('Error: ' + message)
