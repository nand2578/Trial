#python week2

import re
filea = open('C:/Users/anand005/Desktop/Training Documents/Python/regex_sum_314689.txt', 'r')
sum = 0
content = filea.readlines()
for line in content:
    ghj = re.findall('[0-9]+',line)
    print ghj
    if ghj != []:
        for i in ghj:
            sum = sum + int(i)
    print sum