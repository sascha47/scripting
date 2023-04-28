#!/usr/bin/python3
#20230427
# Find associated MAC address with an IP for DHCP REQUEST
# Return in .csv the top two highest IP + MAC address


# imported variables
import csv  
import sys
import re #imports regex

# BEGING WRITE TO FILE
writeToFile = sys.argv[1] #take in input for write file
with open(writeToFile,"w",newline='') as file: 
    writer = csv.writer(file)
    
    # read from file.log
    with open("dhcpdsmall.log","r") as file:
        my_dict = {} # my dictionary # create a dictionary empty
        for line in file: # enumerates through the line by line
            line.rstrip() # removes additional syntax and spaces
            m = re.search("((?:\d{1,3}\.){3}\d{1,3}).*(..:..:..:..:..:..)",line,re.DOTALL) # ip pattern for regex
            if m: # if pattern is found
                ip = m.group(1) # put group1 in var
                mac = m.group(2) # put group2 in var
                key = ip + ' + ' + mac # put both group1 and group2 into a var to define a key
                if key in my_dict:# looks for a key in the dictionary
                    my_dict[key] += 1 # if a key, it will have a value, add 1 to it
                else:
                    my_dict[key] = 1 # no key, add 1 value
                
        high_keys = sorted(my_dict, key=my_dict.get, reverse=True)[:2] # reverse sort dictionary higest to lowest
      
        for key in high_keys:# loops over dictionary and prints value [0] then [1] which is key ip + mac

            writer.writerow([key,my_dict[key]]) # write the result to file
                #writer.writerow([key,my_dict[key]])
        

        


