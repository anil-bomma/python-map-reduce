with open("bonussortedoutput.txt","r") as sorted:
  with open("bonusreducedoutput.txt", "w") as output:

    thisKey = ""
    thisValue = 0.0

    for line in sorted:
      datalist = line.strip().split('\t')
      if (len(datalist) == 2) : 
        department, amount = datalist

        if amount != thisKey:
          if thisKey:
            # output the previous key-summaryvalue result
            output.write(str(thisValue)+ '\t' + thisKey +'\n')
            print(str(thisValue)+ '\t' + thisKey +'\n')

          # start over for each new key
          thisKey = amount 
          thisValue = 0.0
  
        # apply the aggregation function
        thisValue += float(department)

    # output the final key-summaryvalue result outside the loop
    output.write(str(thisValue)+ '\t' + thisKey +'\n')
    print(str(thisValue)+ '\t' + thisKey + '\n')