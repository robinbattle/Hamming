# Hamming
The key to the Hamming Code is the use of extra parity bits to allow the identification of a single error.
There are two ways of encoding: ASCII and Binary

# Usage
$ python hamming.py <type> <command> <arg1> <arg2>

## Type
Where <type> is one of: <br /> 
    asc - ASCII encoding <br />
    bin - Binary encoding <br />
  
## Commond
Where <command> is one of:<br />
    enc <infile> <outfile> <br />
      Encode
    dec  <infile> <outfile> <br />
      ecode
    chk <infil> <br />
      Check
    fix <infile> <outfile> <br />
      Fix
    err <pos> <infile> <outfile> <br />
      Create an error at bit postion <pos> <br />
    
 *
# Testing
$ python testing.py
