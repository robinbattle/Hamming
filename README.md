# Hamming
The key to the Hamming Code is the use of extra parity bits to allow the identification of a single error.
There are two ways of encoding: ASCII and Binary

# Usage
$ python hamming.py <type> <command> <arg1> <arg2>

## Type
Where <type> is one of:
  asc - ASCII encoding
  bin - Binary encoding
  
## Commond
Where <command> is one of:
    enc <infile> <outfile>
      Encode
    dec  <infile> <outfile>
      Decode
    chk <infile>
      Check
    fix <infile> <outfile>
      Fix
    err <pos> <infile> <outfile>
      Create an error at bit postion <pos>
    
 *
# Testing
$ python testing.py
