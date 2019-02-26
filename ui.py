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
    title_lenght = []
    for elements in title_list:
        title_lenght.append(len(elements))
    for row in table:
        for index in range(len(row)):
            if len(row[index]) > title_lenght[index]:
                title_lenght[index] = len(row[index])
    table_width = (len(title_list) + 1) + (len(title_list) * 2) - 2
    for row in title_lenght:
        table_width += row
    top_bottom_line = '-' * table_width
    print(f'\n\t/{top_bottom_line}\\')
    string_title = ''
    string_tabulator = ''
    for index in range(len(title_list)):
        string_title += '| {0:^{1}} '.format(
            title_list[index], title_lenght[index])
        string_tabulator += '|{0:^{1}}'.format('-' *
                                               ((title_lenght[index]) +
                                                2), title_lenght[index])
    print('\t' + string_title + '|')
    print('\t' + string_tabulator + '|')
    for row in table:
        string_table = ''
        for index in range(len(row)):
            string_table += '| {0:^{1}} '.format(
                row[index], title_lenght[index])
        print(f'\t{string_table}|')
        if row != table[-1]:
            print(f'\t{string_tabulator}|')
    print(f'\t\\{top_bottom_line}/\n')


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
    if isinstance(result, str):
        print(result)
        label_lenght = len(str(label))
        result_lenght = len(result)
        string_title = ''
        string_result = ''
        print('\n\t/' + '-' * (label_lenght+2) + '\\')
        string_title += '| {0:^{1}} |'.format(label, label_lenght)
        print('\t' + string_title)
        print('\t|' + '-' * (label_lenght+2) + '|')
        string_result += '| {0:^{1}} |'.format(result, label_lenght)
        print('\t' + string_result)
        print('\t\\' + '-' * (label_lenght+2) + '/')

    elif isinstance(result, int):
        label_lenght = len(str(label))
        result_lenght = len(str(result))
        string_title = ''
        string_result = ''
        print('\n\t/' + '-' * (label_lenght+2) + '\\')
        string_title += '| {0:^{1}} |'.format(label, label_lenght)
        print('\t' + string_title)
        print('\t|' + '-' * (label_lenght+2) + '|')
        string_result += '| {0:^{1}} |'.format(result, label_lenght)
        print('\t' + string_result)
        print('\t\\' + '-' * (label_lenght+2) + '/')

    elif isinstance(result, float):
        label_lenght = len(str(label))
        result_lenght = len(str(result))
        string_title = ''
        string_result = ''
        print('\n\t/' + '-' * (label_lenght+2) + '\\')
        string_title += '| {0:^{1}} |'.format(label, label_lenght)
        print('\t' + string_title)
        print('\t|' + '-' * (label_lenght+2) + '|')
        string_result += '| {0:^{1}} |'.format(result, label_lenght)
        print('\t' + string_result)
        print('\t\\' + '-' * (label_lenght+2) + '/')

    elif isinstance(result, list):
        label_lenght = len(str(label))
        result_lenght = []
        total_result_lenght = 0
        string_label = ''
        if len(result) == 1:
            result_lenght.append(1)
        else:
            for elements in result[0]:
                result_lenght.append(len(elements))
        for row in result:
            for index in range(len(row)):
                if len(result) != 1 and len(row[index]) > result_lenght[index]:
                    result_lenght[index] = len(row[index])
        for items in result_lenght:
            total_result_lenght += items + 2
        total_result_lenght += len(result_lenght) + 1 - 2
        if total_result_lenght > label_lenght:
            label_lenght = total_result_lenght
        print('\n\t/' + '-' * label_lenght + '\\')
        string_label += '|{0:^{1}}|'.format(label, label_lenght)
        print('\t' + string_label)
        print('\t' + '|' + '-' * label_lenght + '|')
        for row in result:
            string_result = ''
            string_tabulator = ''
            if len(result) == 1:
                string_result += '| {0:^{1}} '.format(
                    result[0], label_lenght - 2)
            else:
                for index in range(len(row)):
                    string_result += '| {0:^{1}} '.format(
                        row[index], result_lenght[index])
                    string_tabulator += '|{0:^{1}}'.format(
                        '-' * ((result_lenght[index]) + 2), result_lenght[index])
            print('\t' + string_result + '|')
            if row != result[-1]:
                print('\t' + string_tabulator + '|')
        print('\t\\' + '-' * label_lenght + '/')

    elif isinstance(result, dict):
        key_lenght = []
        value_lenght = []
        label_lenght = len(str(label))
#        for key, value in result.items():
#            print(f'\t{key, value}')
        for key, value in result.items():
            key_lenght.append(len(key))
            value_lenght.append(len(str(value)))
        longest_key = max(key_lenght)
        longest_value = max(value_lenght)
        if longest_key + longest_value + 7 > label_lenght:
            label_lenght = longest_key + longest_value + 7

        string_label = ''
        print('\n\t/' + '-' * (label_lenght+2) + '\\')
        string_label += '| {0:^{1}} |'.format(label, label_lenght)
        print('\t' + string_label)
        print('\t' + '|' + '-' * (label_lenght+2) + '|')
        string_result = ''
        string_tabulator = ''
        last_tabulator = 0
        for key, value in result.items():
            string_result = '|{0:^{1}}'.format(key, longest_key)
            string_result += '|{0:^{1}}'.format(value, label_lenght-longest_key+1)
            print('\t' + string_result + '|')
            string_tabulator = '|'+'-'*longest_key+'|'+'-'*(label_lenght-longest_key+1)+'|'
            last_tabulator += 1
            if last_tabulator < len(result):
                print('\t'+string_tabulator)
        print('\t\\'+'-'*(label_lenght+2)+'/')

    else:
        print('\n\t>>NOTstr/int/float/list/dictionary<<')


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
    print('\n' + title)
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
