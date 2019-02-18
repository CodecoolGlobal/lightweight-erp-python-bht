def print_table(table, title_list):
    print('/-----------------------------------\\')
    for item in title_list:
        for j in item:
            print('|',{item[j]},' '*(20-len(item[j])),'|')
        print('\n')
        print('\\-----------------------------------/')


def print_result(result, label):
    pass


def print_menu(title, list_options, exit_message):
    print(title)
    for item_no, item in enumerate(list_options):
        print('\t(' + str(item_no) + ') ' + item)
    print('\t(0) ' + exit_message)


def get_inputs(list_labels, title):
    inputs = []
    print(title)
    for labels in list_labels:
        item = input(labels+' ')
        inputs.append(item)

    return inputs


def print_error_message(message):
    print('Error: ' + message)
