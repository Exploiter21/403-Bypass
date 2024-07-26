**403-Bypass** is a tool to bypass 403 forbidden status web sites. It is not perfect, it uses some basic and publicly available payloads. I have made this tools according to what I've learned in my bug bounty experience. It will get better and if you think that you have some thing better to contribute then you are welcome to issue a pull request or to fork this repo.


## Help
```
$ python3 main.py --help                               
usage: main.py [-h] [--domain DOMAIN] [--dfile DFILE]
Tools for testing 403 response code

options:
-h, --help            show this help message and exit
--domain DOMAIN, -d DOMAIN
                    domain name
--dfile DFILE, -df DFILE
                  domain file
```

+ `--domain` - This options is to supply a domain name or a proper URL as input.
+ `--dfile` - This options is to supply a file containing multiple domains to test

## Usage

Testing a single domain/URL:
```
$ python3 main.py -d https://example.com/admin/
```
or 
```
$ python3 main.py -d example.com/admin
```
Testing multiple domains:
```
$ python3 main.py -df domains.txt
```

## Payloads
You can find payload files in the cor/ folder.
