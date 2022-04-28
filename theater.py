import re


def Theater_finder(list, theatername):
    listoftheaternames = []
    str_match = [s for s in list if theatername in s]
    if len(str_match) == 0 :
        return "Theater name incorrect or not found"
    else: 
        if len(str_match) > 1:
            for iteration_value in range(len(str_match)):
                regex = "[A-Z/]"
                temp1 = str_match[iteration_value].replace('/cinemas/', '')
                temp2 = re.sub(regex, "", temp1)
                temp3 = temp2.replace('-', ' ')
                temp = temp3.title()
                listoftheaternames.append(temp)
        else:
            listoftheaternames.append(str_match[0])
            regex = "[A-Z/]"
            temp1 = str_match[0].replace('/cinemas/', '')
            temp2 = re.sub(regex, "", temp1)
            temp3 = temp2.replace('-', ' ')
            temp = temp3.title()
            listoftheaternames.append(temp)

    return listoftheaternames