## Data Encryption Standard (DES)

The Data Encryption Standard was once a predominant symmetric-key algorithm for the encryption of electronic data. It was highly influential in the advancement of modern cryptography in the academic world. 

DES is now considered to be insecure for many applications. This is mainly due to the 56-bit key size being too small; in January, 1999, distributed.net and the Electronic Frontier Foundation collaborated to publicly break a DES key in 22 hours and 15 minutes.

DES is the archetypal block cipher — an algorithm that takes a fixed-length string of plaintext bits and transforms it through a series of complicated operations into another ciphertext bitstring of the same length

### Purpose

The purpose of this kata is to implement the standard, and then break DES. 

### Steps 

1. A block of 64 bits is permuted by an initial permutation called IP.
2. Resulting 64 bits are divided in two halves of 32 bits, left and right.
3. Right half goes through a function F(Feistel function)
4. Left half is XOR-ed with output from F function above.
5. Left and right are swapped(except last round).
6. If last round, apply an inverse permutation IP-1 on both halves and that’s the output else, goto step 3. 

### Notes

1. Feistel Structure: 

The Feistel structure has the advantage that encryption and decryption operations are very similar, even identical in some cases, requiring only a reversal of the key schedule. 

source1: https://en.wikipedia.org/wiki/Data_Encryption_Standard
<br>
source2: http://www.networksorcery.com/enp/rfc/rfc2419.txt
<br>
source3: http://csrc.nist.gov/publications/fips/fips46-3/fips46-3.pdf
<br>
source4: http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
