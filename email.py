# thei sis sf kde i yfe abce@gmail.com
# thei sis sf kde i yfe abce@gmail.com
# thei sis sf kde i yfe eee@yahoo.com
# thei sis sf kde i yfe dec@ymail.com

# For this given email in emailtext.txt find all of the email and
# sort them according to there occurrence and print them into output file
# and find the number of gmail among them consider duplicate email as one.


import re
from collections import Counter

if __name__ == "__main__":
    mailList = []
    sortedlist = []
    setofmail = []
    gmail = 0
    with open("emailtext.txt", 'r') as f:
        for line in f:
            for element in re.findall('\S+@\S+', line):
                mailList.append(element)

        sortedlist = sorted(mailList, key=Counter(mailList).get, reverse=True)

        outF = open("sortedMail.txt", 'w+')
        for mail in sortedlist:
            outF.write(mail)
            outF.write('\n')
        setofmail = set(sortedlist)

        for li in setofmail:
            if (re.search('^[\w.+\-]+@gmail\.com$', li)):
                gmail += 1
        print("Number of Gmail is {}".format(gmail))
