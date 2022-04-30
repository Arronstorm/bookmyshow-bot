import re

def StringCleaner(stringList, iterationValue):
    regex = "[A-Z/]"
    temp1 = stringList[iterationValue].replace('/cinemas/', '')
    temp2 = re.sub(regex, "", temp1)
    temp3 = temp2.replace('-', ' ')
    temp = temp3.title()

    return temp