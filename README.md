# DNSniff
The Subdomain Sniffer

## Warning
This program requires the ``host`` program in order to function. it has only been tested on Linux(Debian/Kali).

## Disclaimer
This tool is meant for educational purposes only, any misuse of this application falls in responsibility of the user.

## How to use
+ ``-h`` or ``--help`` for the manual.
+ ``-w`` or ``--wordlist`` for specifying the wordlist that is going to be used.
``python3 dnsniff.py [Host] -w [WORDLIST]``
#### example:
``python3 dnsniff.py www.bancocn.com -w /usr/share/wordlists/dirb/common.txt``
### Attention
+ it is required that the wordlist is in .txt format
+ the host can be ``http[s]://www.whatever.[extension]`` or ``whatever.[extension]``
+ **NOT** ``http[s]://whatever.[Extension]``
