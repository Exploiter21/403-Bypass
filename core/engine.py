#!/bin/env python3
import os
import requests

RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
CYAN   = "\033[36m"
RESET  = "\033[0m"

class Bypass:
    def __init__(self, target):

        self.target = target

    def rectifier(self, domain):
        if domain.startswith("https://") or domain.startswith("http://"):
            return(domain)
        else:
            return(f"https://{domain}")
 
    def scan(self):
        
        if not os.path.isfile(self.target):
            url = self.rectifier(self.target)
        
            try:
                response = requests.get(url, allow_redirects=True)
                if response.status_code == 403:
                    self.forbiddenBypass(url)
            except:
                try:
                    url = "http://" + self.target
                    response = requests.get(url, allow_redirects=True)
                
                    if response.status_code == 403:
                        self.forbiddenBypass(url)
                except:
                    pass 
        else:
            try:
                with open(self.target, 'r') as dfile:
                    for domain in dfile.readlines():
                        self.forbiddenBypass(self.rectifier(''.join(domain.strip())))
            except Exception as error:
                print(f"{RED}Got error while reading {self.target} file. {error}{RESET}")

    def forbiddenBypass(self, url):
        # url scan
        try:
            
            with open('core/url_payloads.txt', 'r') as urlPayloads:
                i = 0
                for payload in urlPayloads.readlines():
                    finalUrl = url +'/'+ ''.join(payload.strip()) 
                    response = requests.get(finalUrl, allow_redirects=True)
                    if response.status_code != 403:
                        if response.status_code == 302 or response.status_code == 301:
                            print(f"{YELLOW}[INFO]{RESET} ▶ {YELLOW}{response.status_code}{RESET}  {YELLOW}{finalUrl}{RESET}")
                        elif response.status_code == 200:
                            print(f"{GREEN}[Found]{RESET} ▶ {GREEN}{response.status_code}{RESET}  {YELLOW}{finalUrl}{RESET} {GREEN} ")
                            break
                    else:
                        print(f"{CYAN}[INFO]{RESET} ▶ {RED}{response.status_code}{RESET}  {finalUrl}")
            
            with open('core/header_payloads.txt', 'r') as headerPayload:
                for payload in headerPayload.readlines():
                    part1 = ''.join(payload.split(":")[0])
                    part2 = ''.join(payload.split(":")[1].strip("\n").strip(" "))
                    header = {part1:part2}
                    response = requests.get(url, headers=header, allow_redirects=True)
                    
                    if response.status_code != 403:
                        if response.status_code == 302 or response.status_code == 301:
                            print(f"{YELLOW}[INFO]{RESET} ▶ {YELLOW}{response.status_code}{RESET} ▶ {YELLOW}{url}{RESET} {YELLOW}{part1}':'{part2}{RESET} ")
                        elif response.status_code == 200:
                            print(f"{GREEN}[Found]{RESET} ▶ {GREEN}{response.status_code}{RESET} ▶ {GREEN}{url}{GREEN} {YELLOW}{part1}':'{part2}{RESET}")
                    else:
                        print(f"{CYAN}[INFO]{RESET} ▶ {RED}{response.status_code}{RESET}  {url}  {RED}{part1} : {part2}{RESET}")
        except Exception as error:
            print(f"{RED}Got error while reading payloads file. {error}{RESET}")