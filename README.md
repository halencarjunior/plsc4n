# Plone Scanner Version 0.01
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

```bash
      :::::::::  :::        ::::::::   ::::::::     :::     ::::    ::: 
     :+:    :+: :+:       :+:    :+: :+:    :+:   :+:      :+:+:   :+:  
    +:+    +:+ +:+       +:+        +:+         +:+ +:+   :+:+:+  +:+   
   +#++:++#+  +#+       +#++:++#++ +#+        +#+  +:+   +#+ +:+ +#+    
  +#+        +#+              +#+ +#+       +#+#+#+#+#+ +#+  +#+#+#     
 #+#        #+#       #+#    #+# #+#    #+#      #+#   #+#   #+#+#      
###        ########## ########   ########       ###   ###    ####       
```
## Requirements

- python3+
- shodan
- colorama

```sh
$ python3 -m pip install -r requirements.txt
```

## Features

- Grab Plone version from exposed servers
- Try to guess the close version from specific tests
- Show the CVEs for the specific version or close one

## optional arguments:
```
  -h, --help          show this help message and exit
  -u URL, --url URL   url e.g: https://192.168.0.1/plone
  -s, --shodan        Search for hosts in Shodan (Needs api key)
  -r, --random-agent  Use a random user-agent
  -c, --cve           Search and Print CVEs
  --version           show program's version number and exit
```
## Usage example

```sh
$ python3 plsc4n.py -u http://example.com/ --random --cve
```

## Development

Want to contribute? Great! Please send your PR for us and we'll be greateful for your help.
Thanks for using and help to share please

**Free Software, Hell Yeah!**
