


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

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')












