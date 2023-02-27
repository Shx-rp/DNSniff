#!/bin/env/python3
import subprocess
import sys

domainlist = [".com", ".pt", ".us", ".net", ".ca", ".gov"]
def main():
    if len(sys.argv) >= 1:
        try:
            if (sys.argv[1] == "-h") or (sys.argv[1] == "--help"):
                print("Argument             Action")
                print()
                print("-w or --wordlist     Wordlists")
                print("-h or --help         Help Menu")
                print()
                print("Example:")
                print()
                print("dnsniff.py www.bancocn.com -w /usr/share/wordlists/WORDLIST.txt")
            elif any(domain in sys.argv[1] for domain in domainlist):
                if "www" in sys.argv[1]:
                    sys.argv[1] =  sys.argv[1].replace("www","")
                else:
                    sys.argv[1] = "." + sys.argv[1]
                if (sys.argv[2] == "-w") or (sys.argv[2] == "--wordlist"):
                    if ".txt" in sys.argv[3]:
                        with open(sys.argv[3], 'r') as words:
                            wordlist = [line.split('\n') for line in words.read().splitlines()]
                        print("______DNSNIFF_______")
                        for word in wordlist:
                            word = str(word)
                            word = word.replace("['","")
                            word = word.replace("']","")
                            command = word + sys.argv[1]
                            try:
                                sniff = subprocess.Popen(["host", command], stdout=subprocess.PIPE, encoding="UTF-8")
                                out, err = sniff.communicate()
                                if "has" in out:
                                    print("\n" + word + " Has been found:\n")
                                    print(out)
                            except KeyboardInterrupt:
                                print("Action Canceled!")
                    else:
                        print("Invalid Wordlist extention!")
            else:
                print(sys.argv[1] + " Is an invalid argument!")
        except IndexError:
            print("Additional Parameters are required! use -h or --help for help!")
if __name__ == "__main__":
    main()