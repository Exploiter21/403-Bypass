#!/bin/env python3
from core.engine import *
import argparse
import os

if __name__=="__main__":
    
    banner = """
  ____                            _  _    ___ ____  
 |  _ \                          | || |  / _ \___ \ 
 | |_) |_   _ _ __   __ _ ___ ___| || |_| | | |__) |
 |  _ <| | | | '_ \ / _` / __/ __|__   _| | | |__ < 
 | |_) | |_| | |_) | (_| \__ \__ \  | | | |_| |__) |
 |____/ \__, | .__/ \__,_|___/___/  |_|  \___/____/ 
         __/ | |                                    
        |___/|_|                                    

Created with <3 by Sarthak Joshi
"""
    
    parse = argparse.ArgumentParser(description="Tools for testing 403 response code")
    parse.add_argument('--domain', '-d', help='domain name')
    parse.add_argument('--dfile', '-df', help='domain file')
    parser = parse.parse_args()

    domain = parser.domain
    domainFile = parser.dfile
    print(f"{CYAN}{banner}{RESET}")
    if domain and domainFile:
        parse.error("only supply one option, either --domain or --dfile")
    
    elif domain:
        bypassme = Bypass(domain)
        bypassme.scan()

    elif domainFile:
        bypassme = Bypass(domainFile)
        bypassme.scan()
      
    else:
        parse.error("atleast provide domain or file of domains")            
