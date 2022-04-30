from miscfunctions import StringCleaner


def Theater_finder(list, theatername):
    listoftheaternames = []

    str_match = [s for s in list if theatername in s]

    if len(str_match) == 0:
        return "Theater name incorrect or not found"

    else:

        if len(str_match) > 1:
            for iteration_value in range(len(str_match)):
                cleanedString = StringCleaner(str_match, iteration_value)
                listoftheaternames.append(
                    str_match[iteration_value] + "_" + cleanedString)

        else:
            cleanedString = StringCleaner(str_match, 0)
            listoftheaternames.append(str_match[0] + "_" + cleanedString)

    return listoftheaternames
