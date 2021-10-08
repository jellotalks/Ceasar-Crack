
import enchant
import re
import time

def encrypt(instr, n):
    outstr = ''
    for i in range(len(instr)):
        charord = 0
        if not instr[i].isalpha():
            outstr += instr[i]
            continue
        elif instr[i].isupper(): charord = ord('A')
        else: charord = ord('a')
        outstr += chr(((ord(instr[i]) - charord + n) % 26) + charord)
    return outstr

def decrypt(instr, n):
    outstr = ''
    for i in range(len(instr)):
        charord = 0
        if not instr[i].isalpha():
            outstr += instr[i]
            continue
        elif instr[i].isupper(): charord = ord('A')
        else: charord = ord('a')
        outstr += chr(((ord(instr[i]) - charord - n) % 26) + charord)
    return outstr

def hack(instr):
    d = enchant.Dict('en_US')
    for i in range(1,26):
        sentence = decrypt(instr,i)
        wordlist = re.split('[^a-zA-Z]+',sentence)
        validwords = []
        for j in wordlist:
            if j != '' and d.check(j):
                validwords.append(j)
        if len(validwords) >= int(len(wordlist)/2):
            print("Possible Decrypt Key {}: {} (Matching words: {})".format(i,sentence,validwords))

def main():
    while True:
        try:
            option = str(input("Do what? (e = encrypt, d = decrypt, h = hack, q = quit): ")).strip()
            if option != 'e' and option != 'd' and option != 'h':
                if option == 'q':
                    break
                print("Invalid response")
                continue
            if option != 'h': numspaces = int(input("How many spaces? : "))
            instr = str(input("Please enter string: "))
        except ValueError as e:
            print("Invalid response")
            continue

        if option == 'e':
            tic = time.perf_counter()
            print("Encrypted string: {}".format(encrypt(instr,numspaces)))
            toc = time.perf_counter()
            print("Encrypted in {:.2f} milliseconds.".format((toc-tic)*1000))
        elif option == 'd':
            tic = time.perf_counter()
            print("Decrypted string: {}".format(decrypt(instr,numspaces)))
            toc = time.perf_counter()
            print("Decrypted in {:.2f} milliseconds.".format((toc-tic)*1000))
        elif option == 'h':
            tic = time.perf_counter()
            hack(instr)
            toc = time.perf_counter()
            print("Hacked in {:.2f} milliseconds.".format((toc-tic)*1000))

if __name__ == "__main__":
    main()
