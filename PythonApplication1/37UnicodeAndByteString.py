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
bytes_=b'prova di byte'
stringfrombyte = bytes_.decode()           #.decode() str from bytes
backtobyte = stringfrombyte.encode()      #.encode() bytes from str
print(b'prova di byte: ',bytes_)
'''
all the current string literal forms 'xxx', "xxx", and triplequoted blocks generate a str; adding a 
b or B just before any of them creates a bytes instead
'''
print("bytes object is a sequence of short integer")
for x in bytes_:
    print("byte %s corrisponde al carattere %s" % (x, chr(x)))
print('---------------------------------------------------------------------')
x='XYZ'         #an Unicode string of ASCII text
for c in x:
    print("byte %s corrisponde al carattere %s" % (ord(c), c))  #ord to get a character cardinal
print('---------------------------------------------------------------------')
print('Coding non ASCII text')
ab = [chr(0xc4),chr(0xe8)]             # 0x Unicode escape, usable only on a character 
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
print('latin-1: ',h)
print("len(h): ",len(h))           #two byte for 2 characters
print("len(h.decode('latin-1')): ",len(h.decode('latin-1')))    
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
print("Working with bytes type we can use a lot of the standar string command")
print('But remember, bytes operation take bytes by imput and return bytes')
B = b'spam'
print("B: ",B)  #print as ASCII character
print("B.find(b'am'):", B.find(b'am'))
print("B.replace(b'pa',b'UU'):", B.replace(b'pa',b'UU'))
print("B[1:3]:", B[1:3])
'''
bytes really is a sequence of 8-bit integers, but for convenience prints as a string of 
ASCII coded characters where possible when displayed as a whole.
'''
print("list(B): ",list(B))
print("B[0]: ",B[0])
print("chr(B[0]): ",chr(B[0]))
print("B + b' LUNA': ",B + b' LUNA')
print('---------------------------------------------------------------------')
print("We can also create a byte using the bytes(..) costructor")
B = bytes('abc',"ascii")    #constructor with string and encoding
print("B: ",B) 
B = bytes([101,97,113])
print("B: ",B) 
print('---------------------------------------------------------------------')
print("Using bytarray (mutable bytes) :-)")
ba = bytearray('viva la pappa',"latin1")
print(ba)
ba[1] = ord('u')
print(ba)
ba.extend(b' al pomodoro')
print(ba)
print("ba[4:12]: %s" % ba[4:12])
print('---------------------------------------------------------------------')
print("     A SAMPLE RECAP")
print('Use str for textual data.')
print('Use bytes for binary data.')
print('Use bytearray for binary data you wish to change in place.')
print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')