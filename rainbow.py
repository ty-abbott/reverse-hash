#Import required modules
import sys
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from signal import signal,SIGINT

# terminates the program gracefully
def handler(signal_received, frame):
    #print("exiting program")
    print(f'Number of cards tested {cards}')
    exit(0)

def usage():
    print(f'usage: python3 {sys.argv[0]} [first6] [last4]')

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0

# Main routing of program
#print("starting program")
signal(SIGINT, handler)
# confirm that the right number of arguments was provided
if len(sys.argv) < 3:
    usage()
    sys.exit(1)

#Define variables necessary for operation
first6 = int(sys.argv[1])
last4 = int(sys.argv[2])
targetHash = str(sys.argv[3])
customerName = str(sys.argv[4])
cardnum = first6 * pow(10,10) + last4
#print(cardnum)
cardtext = str(cardnum)
endnumber = cardnum + 9999990000

# debug code just to confirm that the values are correct
#print(endnumber)
#print(f'first6 = {first6}')
#print(f'last4 = {last4}')

cards = 0

#cryptography.hazmat.backends.default_backend()
while (cardnum <=  endnumber):
    cardtext = str(cardnum)
    if is_luhn_valid(cardnum):
        digest = hashes.Hash(hashes.SHA256())
        digest.update(cardtext.encode('latin1'))
        myHash = digest.finalize()
        yourHex = myHash.hex()
        if targetHash == yourHex:
            print(f'Here is the card number for {customerName}:')
            print(f'{cardnum}')
            print(f'Hash value: {targetHash}, First six: {first6}, last four:{last4}')
            break
        #print (f'{cardnum},{yourHex}')
    cardnum += 10000
    cards += 1
handler(0,0)