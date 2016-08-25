print('---------------------------------------------------------------------')
print('Different unicode type important when riding from external source')
S = 'ni'
print("S.encode('ascii'): %s" % S.encode('ascii'))
print("S.encode('latin1'): %s" % S.encode('latin1'))
print("S.encode('utf8'): %s" % S.encode('utf8'))
print("S.encode('utf16'): %s" % S.encode('utf16'))
print("S.encode('utf32'): %s" % S.encode('utf32'))
print('---------------------------------------------------------------------')
"""
In memory, Python always stores decoded text strings in an encoding-neutral format, which may 
or may not use multiple bytes for each character. Text is translated to and from an 
encoding-specific format only when it is transferred to or from external text files, byte strings, 
or APIs with specific encoding requirements. Once in memory, though, strings have no encoding.
"""

print('---------------------------------------------------------------------')
print ("Bytes as array of bites")
bytes=b'prova di byte'
stringfrombyte=bytes.decode()           #str from bytes
backtobyte=stringfrombyte.encode()      #bytes from str
print(b'prova di byte: ',bytes)
'''
all the current string literal forms 'xxx', "xxx", and triplequoted blocks generate a str; adding a 
b or B just before any of them creates a bytes instead
'''
print("bytes object is a sequence of short integer")
for x in bytes:
    print("byte %s corrisponde al carattere %s" % (x, chr(x)))
print('---------------------------------------------------------------------')
x='XYZ'         #an Unicode string of ASCII text
for c in x:
    print("byte %s corrisponde al carattere %s" % (ord(c), c))
print('---------------------------------------------------------------------')
print('Coding non ASCII text')
ab = [chr(0xc4),chr(0xe8)]       # 0x Unicode escape, usable only on a character 
print (ab)

s = 'primo: \xc4 - secondo: \xe8'      # \x 8-bit hex escape can be use on more than a single value
print(s)
z="\u00c4\u00e8"                       # \u00 -bit hex escape 
print(z)
print('---------------------------------------------------------------------')
print("Encodind and decoding non Asci")
s = '\xc4\xe8'
#h = s.encode('ascii')   #'ascii' codec can't encode character '\xc4' in position 7: ordinal not in range(128)
print("'\xc4\xe8' latin-1")
h = s.encode('latin-1')
print("len(h): ",len(h))           #two byte for 2 characters
print('latin-1: ',h)
print("len(h.decode('latin-1')): ",len(h.decode('latin-1')))    #
for x in h:
    print("byte %s corrisponde al carattere %s" % (x, chr(x)))
print('---------------------------------------------------------------------')
print("Encodind and decoding non Asci - 2")
print("'\xc4\xe8' utf-8")
h = s.encode('utf-8')
print("len(h): ",len(h))           #4: two couples of two byte, for a total of 2 characters
print('utf-8: ',h)
print("len(h.decode('utf-8')): ",len(h.decode('utf-8')))
print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')
