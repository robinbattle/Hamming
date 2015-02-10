__author__ = 'blu2'
import hamming

counter = 0

"""
    1. encode (file 1) as ascii (file 2),
    2. then decode to text (file 3),
    3. compare (file 1) and (file 3)
"""
def enc_asc_then_decode_then_verify():
    #encode
    encoder = hamming.HammingFile("asc", "hello.txt", "hello.asc")
    encoder.encode_file()
    #decode
    decoder = hamming.HammingFile("asc", "hello.asc", "hello_new.txt")
    decoder.decode_file()

    old_file = open("hello.txt")
    text1 = old_file.read()

    new_file = open("hello_new.txt")
    text2 = new_file.read()

    if text1 == text2:
        return True
    else:
        return False

"""
    1. encode (file 1) as binary (file 2),
    2. then decode to text (file 3),
    3. compare (file 1) and (file 3)
"""
def enc_bin_then_decode_then_verify():
    #encode
    encoder = hamming.HammingFile("bin", "hello.txt", "hello.bin")
    encoder.encode_file()
    #decode
    decoder = hamming.HammingFile("bin", "hello.bin", "hello_new.txt")
    decoder.decode_file()

    old_file = open("hello.txt")
    text1 = old_file.read()

    new_file = open("hello_new.txt")
    text2 = new_file.read()

    if text1 == text2:
        return True
    else:
        return False


"""
    Check the Parity of the Ascii File
    If no errors, return True
    Otherwise, return False
"""
def chk_asc_parity():
    #check
    checker = hamming.HammingFile("asc", "hello.asc", None)
    positions = checker.check_file()
    if len(positions) == 0:
        return True
    else:
        return False

"""
    Check the Parity of the Binary File
    If no errors, return True
    Otherwise, return False
"""
def chk_bin_parity():
    #check
    checker = hamming.HammingFile("bin", "hello.bin", None)
    positions = checker.check_file()
    if len(positions) == 0:
        return True
    else:
        return False


"""
    1. Flip some ascii positions of (file 1) into (file 2)
    2. Check Error Position
"""
def error_asc_parity():
    #first error
    errorer = hamming.HammingFile("asc", "hello.asc", "hello_error.asc")
    errorer.error_file(7)
    #second error
    errorer = hamming.HammingFile("asc", "hello_error.asc", "hello_error.asc")
    errorer.error_file(15)

    checker = hamming.HammingFile("asc", "hello_error.asc", None)
    positions = checker.check_file()
    if positions == [7, 15]:
        return True
    else:
        return False

"""
    1. Flip some binary positions of (file 1) into (file 2)
    2. Check Error Position
"""
def error_bin_parity():
    #first error
    errorer = hamming.HammingFile("bin", "hello.bin", "hello_error.bin")
    errorer.error_file(7)
    #second error
    errorer = hamming.HammingFile("bin", "hello_error.bin", "hello_error.bin")
    errorer.error_file(15)

    checker = hamming.HammingFile("bin", "hello_error.bin", None)
    positions = checker.check_file()
    if positions == [7, 15]:
        return True
    else:
        return False

"""
    1. Fix ascii error positions of (file 1) into (file 2)
    2. Check if Pass Parity test
"""
def fix_asc_parity():
    fixer = hamming.HammingFile("asc", "hello_error.asc", "hello_fix.asc")
    fixer.fix_file()

    checker = hamming.HammingFile("asc", "hello_fix.asc", None)
    positions = checker.check_file()
    if len(positions) == 0:
        return True
    else:
        return False

"""
    1. Fix binary error positions of (file 1) into (file 2)
    2. Check if Pass Parity test
"""
def fix_bin_parity():
    fixer = hamming.HammingFile("bin", "hello_error.bin", "hello_fix.bin")
    fixer.fix_file()

    checker = hamming.HammingFile("bin", "hello_fix.bin", None)
    positions = checker.check_file()
    if len(positions) == 0:
        return True
    else:
        return False

"""
    1. decode fixed ascii (file 1) into text (file 2)
    2. Check if it is the same as origin one
"""
def dec_fix_asc():
    decoder = hamming.HammingFile("asc", "hello_fix.asc", "hello_fix.txt")
    decoder.decode_file()

    old_file = open("hello.txt")
    text1 = old_file.read()

    new_file = open("hello_fix.txt")
    text2 = new_file.read()

    if text1 == text2:
        return True
    else:
        return False


"""
    1. decode fixed binary (file 1) into text (file 2)
    2. Check if it is the same as origin one
"""
def dec_fix_bin():
    decoder = hamming.HammingFile("bin", "hello_fix.bin", "hello_fix.txt")
    decoder.decode_file()

    old_file = open("hello.txt")
    text1 = old_file.read()

    new_file = open("hello_fix.txt")
    text2 = new_file.read()

    if text1 == text2:
        return True
    else:
        return False



if __name__ == '__main__':

    """ascii"""
    if enc_asc_then_decode_then_verify():
        counter += 1
        print "enc_asc_then_decode_then_verify() Pass"
    else:
        print "enc_asc_then_decode_then_verify() Fail"

    if chk_asc_parity():
        counter += 1
        print "chk_asc_parity() Pass"
    else:
        print "chk_asc_parity() Fail"

    if error_asc_parity():
        counter += 1
        print "error_asc_parity() Pass"
    else:
        print "error_asc_parity() Fail"

    if fix_asc_parity():
        counter += 1
        print "fix_asc_parity() Pass"
    else:
        print "fix_asc_parity() Fail"

    if dec_fix_asc():
        counter += 1
        print "dec_fix_asc() Pass"
    else:
        print "dec_fix_asc() Fail"




    """binary"""
    if enc_bin_then_decode_then_verify():
        counter += 1
        print "enc_bin_then_decode_then_verify() Pass"
    else:
        print "enc_bin_then_decode_then_verify() Fail"

    if chk_bin_parity():
        counter += 1
        print "chk_bin_parity() Pass"
    else:
        print "chk_bin_parity() Fail"

    if error_bin_parity():
        counter += 1
        print "error_bin_parity() Pass"
    else:
        print "error_bin_parity() Fail"

    if fix_bin_parity():
        counter += 1
        print "fix_bin_parity() Pass"
    else:
        print "fix_bin_parity() Fail"

    if dec_fix_bin():
        counter += 1
        print "dec_fix_bin() Pass"
    else:
        print "dec_fix_bin() Fail"

    if counter == 10:
        print "\nAll 10 Tests Pass"




