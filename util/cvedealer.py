import csv
from packaging import version
import re
import sys

def printCVE(v):

    with open("cvedetails.tsv") as file:
        
        tsv_file = csv.reader(file, delimiter="\t")
        
        for line in tsv_file:
            linha = str(line[15])
            
            # Looking for version numbers
            #versions = re.findall(r'(\d+[.]\d+[.]\d+)', linha)
            #versions = re.findall(r'([\d.]+[\d.]+)', linha)
            
            # testing versions with .x
            versionsX = re.findall(r'([\d.]+[x.]+[x.]+)\s*through\s*([\d.]+[\d.]+)', linha)
            if len(versionsX) >= 1:
                
                
                for i in versionsX:
                    #print(i)
                    i_replaced = i[0].replace('x','0')
                    #print(i_replaced)
                    if version.parse(v) >= version.parse(i_replaced) and version.parse(v) <= version.parse(i[1]):
                        print(" [+] {} - {}".format(line[1], line[4]))
                        print("          {}\n".format(line[15]))
                        
            # testing versions through more than 1
            versionsThrough = re.findall(r'([\d.]+[\d.]+)\s*through\s*([\d.]+[\d.]+)', linha)
            if len(versionsThrough) >= 1:
            
                for i in versionsThrough:
                    if version.parse(v) >= version.parse(i[0]) and version.parse(v) <= version.parse(i[1]):
                        print(" [+] {} - {}".format(line[1], line[4]))
                        print("          {}\n".format(line[15]))
            
            versionsDash = re.findall(r'([\d.]+[\dx.]+)\s*-\s*([\d.]+[\d.]+)', linha)
            if len(versionsDash) >= 1:
                #print(versionsDash)
                for i in versionsDash:
                    if version.parse(v) >= version.parse(i[0]) and version.parse(v) <= version.parse(i[1]):
                        print(" [+] {} - {}".format(line[1], line[4]))
                        print("          {}\n".format(line[15]))


            versionCMSThrough = re.findall(r'^Plone\s*through\s*([\d.]+[\d.]+)', linha)
            if len(versionCMSThrough) >= 1:
                #print(versionCMSThrough)
                for i in versionCMSThrough:
                    if version.parse(v) >= version.parse('0') and version.parse(v) <= version.parse(i):
                        print(" [+] {} - {}".format(line[1], line[4]))
                        print("          {}\n".format(line[15]))

            versionCMSBefore = re.findall(r'^Plone\s*before\s*([\d.]+[\d.]+)', linha)
            if len(versionCMSBefore) >= 1:
                #print(versionCMSThrough)
                for i in versionCMSBefore:
                    if version.parse(v) >= version.parse('0') and version.parse(v) <= version.parse(i):
                        print(" [+] {} - {}".format(line[1], line[4]))
                        print("          {}\n".format(line[15]))

            versionUntilThroughBefore = re.findall(r'^Plone\s*CMS\s*until\s*version\s*([\d.]+[\d.]+)', linha)
            if len(versionUntilThroughBefore) >= 1:
                for i in versionUntilThroughBefore:
                    if version.parse(v) >= version.parse('0') and version.parse(v) <= version.parse(i):
                        print(" [+] {} - {}".format(line[1], line[4]))
                        print("          {}\n".format(line[15]))
                        
            '''
            # counting versions
            lengthVersions = len(versionsThrough) 
            # looking for through
            if line[15].lower().count('through') > 0:
                exists = line[15].lower().count('through')
                if version.parse(v) >= version.parse(versions[0]) and version.parse(v) <= version.parse(versions[1]):
                    print("{} - {} - {}".format(lengthVersions, versions, exists))
            else:
                exists = False
            '''

            


'''def main():
    plone_version = sys.argv[1]

    #version.parse("2.3.1") < version.parse("10.1.2")
    printCVE(plone_version)

if __name__ == "__main__":
    try:
        main()
    except NameError:
        print("Variable x is not defined")
    except:
        print("Something else went wrong") '''