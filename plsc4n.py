from queue import Empty
import requests
from util import cvedealer
from util import headerdealer as rheader
import shodan
import argparse
from colorama import Fore, Back, Style
import hashlib
import os

_SHODAN_API_KEY_ = "YOUR API KEY HERE"
_SHODAN_API_ = shodan.Shodan(_SHODAN_API_KEY_)

def md5Tester(file_to_test):
    md5_hash = hashlib.md5()

    a_file = open(file_to_test, "rb")
    content = a_file.read()
    md5_hash.update(content)

    digest = md5_hash.hexdigest()
    return digest

def urlTester(url, header):
    r = requests.get(url, headers=header)
    #print(type(r.headers))
    pl_version = r.headers['Server'][r.headers['Server'].find('Plone'):].strip('Plone/')
    
    if r.headers['Server'].find('Plone') > 0 and pl_version.lower() != "unknow":
        print("[+] Plone version found TEST: {} \n".format(pl_version)) 
        return pl_version
    else:
        return None

def versionTester(url, header):
    # Normalize url
    if url[:-1] == "/":
        urlTest1 = url+"xlsx.png"
        urlTest2 = url+"docx.png"
        urlTest3 = url+"pptx.png"
    else:
        urlTest1 = url+"/xlsx.png"
        urlTest2 = url+"docx.png"
        urlTest3 = url+"pptx.png"

    r1 = requests.get(urlTest1, headers=header)
    r2 = requests.get(urlTest2, headers=header)
    r3 = requests.get(urlTest3, headers=header)
    if r1.status_code == "200" and r2.status_code == "200" and r3.status_code == "200":
        ploneVersion = "5.x"
        return ploneVersion
    else:
        print("[-] Plone 5.x not detected")
        print("[+] Testing for Plone 3.x or 4.x") 
        if url[:-1] == "/":
            rdoc = requests.get(url+"doc.png",headers=header)
            open('doc.png', 'wb').write(rdoc.content)
            #print(rdoc.status_code)
            md5TestResult = md5Tester('doc.png')
            if md5TestResult == "9aaf340ffade6855773d77e5337f2e99":
                print("[+] Hash found for Plone 3.x")
                ploneVersion = "3.x"
                return ploneVersion
            elif md5TestResult == "0cdccf92dd1983b092d6937d4b098aa2":
                print("[+] Hash found for Plone 4.x")
                ploneVersion = "4.x"
                return ploneVersion
        else:
            rdoc = requests.get(url+"/doc.png",headers=header)
            open('doc.png', 'wb').write(rdoc.content)
            #print(rdoc.status_code)
            md5TestResult = md5Tester('doc.png')
            if md5TestResult == "9aaf340ffade6855773d77e5337f2e99":
                print("[+] Hash found for Plone 3.x")
                ploneVersion = "3.x"
                return ploneVersion
            elif md5TestResult == "0cdccf92dd1983b092d6937d4b098aa2":
                print("[+] Hash found for Plone 4.x")
                ploneVersion = "4.x"
                return ploneVersion
        
def main():

    parser = argparse.ArgumentParser(prog='PLsc4n', formatter_class=argparse.RawDescriptionHelpFormatter, \
    description='''\n      :::::::::  :::        ::::::::   ::::::::     :::     ::::    ::: 
     :+:    :+: :+:       :+:    :+: :+:    :+:   :+:      :+:+:   :+:  
    +:+    +:+ +:+       +:+        +:+         +:+ +:+   :+:+:+  +:+   
   +#++:++#+  +#+       +#++:++#++ +#+        +#+  +:+   +#+ +:+ +#+    
  +#+        +#+              +#+ +#+       +#+#+#+#+#+ +#+  +#+#+#     
 #+#        #+#       #+#    #+# #+#    #+#      #+#   #+#   #+#+#      
###        ########## ########   ########       ###   ###    ####       

Plone Scanner Version 0.01\nBy bt0 - github.com/halencarjunior
==============================================================''')


    parser.add_argument('-u', '--url', type=str, help='url e.g: https://192.168.0.1/plone')
    parser.add_argument('-s', '--shodan' , action="store_true", help='Search for hosts in Shodan (Needs api key)')	
    parser.add_argument('-r', '--random-agent' , action="store_true", help='Use a random user-agent')	
    parser.add_argument('-c', '--cve' , action="store_true", help='Search and Print CVEs')	
    parser.add_argument('--version', action='version', version='%(prog)s 0.01')
    args = parser.parse_args()

    if args.random_agent:
        defaultHeader = {'user-agent': rheader.randomHeader()}
        
        headermsg = "Using Random user-agent: " + defaultHeader['user-agent']
    else:
        defaultHeader = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'}
        headermsg = "Using Default user-agent: " + defaultHeader['user-agent']
    
    if args.url == None:
        print(parser.print_help())
    elif args.url:
        print(parser.description)
        print("Testing URL {} ".format(args.url))
        print(headermsg+"\n")
        testing = urlTester(args.url, defaultHeader)
        if testing is not None:
            if args.cve:
                print("    Describing CVEs\n")
                cvedealer.printCVE(testing)
        else:
            print("[-] Plone version not exposed. Trying to guess the version")
            versionGuessed = versionTester(args.url, defaultHeader)
            print("[+] Plone version would be: {} \n".format(versionGuessed))
            os.remove("./doc.png")
            if args.cve:
                if versionGuessed == "3.x":
                    print("CVEs found for 3.x version\n")
                    cvedealer.printCVE("3.2")
                if versionGuessed == "4.x":
                    print("CVEs found for 4.x version\n")
                    cvedealer.printCVE("4.1")
                if versionGuessed == "5.x":
                    print("CVEs found for 5.x version\n")
                    cvedealer.printCVE("5.1")

if __name__ == "__main__":
    main()
