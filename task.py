import sys
from statistics import mean
from prettytable import PrettyTable

# check if the values are numeric
def check_value(argu, value_list):
    for i in range(3, len(argu)):
        value_list.append(argu[i])
        try:
            float(sys.argv[i])
        except:
            help_message()
            value_list = []
            break
    return value_list

# write values into specific file
def write_file(value_list, argu):
    for i in value_list:
        with open(argu[2], "a+") as output_file:
            output_file.write(i + "\n")

# record action: save one or more values into a specified file
def record(argu):
    value_list = []
    if len(argu) > 3:
        # check if the file is a text file
        if argu[2].endswith('.txt'):
            value_list = check_value(argu, value_list)
        else:
            help_message()
    else:
        help_message()

    if value_list != []:
        write_file(value_list, argu)

# summary action: summarise the values
def summary(argu):
    if len(argu) == 3:
        txt_file = argu[2]
        if txt_file.endswith('.txt'):
            with open(txt_file, "r") as input_file:
                read_list = input_file.read().split('\n')
            # filter none value
            read_list = list(filter(None, read_list))
            # convert string to float
            read_list = list(map(float, read_list))
            create_texttable(read_list)
        else:
            help_message()
    else:
        help_message()

# print a text table
def create_texttable(read_list):
    x = PrettyTable()
    x.header = False
    x.add_row(["# of Entries", len(read_list)])
    x.add_row(["Min. value", min(read_list)])
    x.add_row(["Max. value", max(read_list)])
    x.add_row(["Avg. value", mean(read_list)])
    print(x)

# help action: print informative message
def help_message():
    print("Usage Guide: ")
    print("1. record action : python task.py record filepath value [value 2..value n]")
    print("2. summary action : python task.py summarise/summary filepath")
    print("3. help action : python task.py help" + "\n")
    print("Note: ")
    print("* value : Only accept numeric values")
    print("* filename : Only accept text file (.txt)")
    print("* summary action is only available after record action")

# main function
if __name__ == "__main__":
    try:
        # record
        if sys.argv[1].lower() == "record":
            record(sys.argv)

        # summary
        elif sys.argv[1].lower() == "summarise" or sys.argv[1].lower() == "summary":
            summary(sys.argv)

        # help
        elif sys.argv[1].lower() == "help":
            help_message()
    except:
        help_message()
