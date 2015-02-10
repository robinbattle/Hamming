# Hamming
The key to the Hamming Code is the use of extra parity bits to allow the identification of a single error.
There are two ways of encoding: ASCII and Binary

# Usage
$ python hamming.py <type> <command> <arg1> <arg2>

Where <type> is one of:
  1. asc - ASCII encoding
  2. bin - Binary encoding
Where <command> is one of:
  1. enc <infile> <outfile>
    Encode
  2. dec  <infile> <outfile>
    Decode
  3. chk <infile>
    Check
  4. fix <infile> <outfile>
    Fix
  5. err <pos> <infile> <outfile>
    Create an error at bit postion <pos>
    
 *
# Testing
$ python testing.py
