# Case 2 - Mapper using standard input and output
# Easy to test locally with Bash


import sys
with open("purchases.txt", "r") as input:
    with open("departmentmapper.txt", "w") as output:

        # iterate through each line provided via standard input
      for line in sys.stdin:
        datalist = line.strip().split("    ")
        if (len(datalist) == 6):
          date, time, store, department, cost, paymentType = datalist

        # print intermediate key-value pairs to standard output
          print(store + "\t" + cost + "\n")
