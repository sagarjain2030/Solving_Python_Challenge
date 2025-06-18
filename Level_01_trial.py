# Now first level of the game is cipher challenge.
# Input give is image where it is written:
# K -> M
# O -> Q
# E -> G
# Hint given is : everybody thinks twice before solving this.
# And input string is :
# g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
# Now looking at K->M, we can say that 2nd character is chosen in alphabetical order.
# it can be that we are getting encrypted data and we can decrypt like K -> M or M -> K.So 2 possible results can be there.
# So I will generate both results and then we can check Both results.

def translateForward(input_string):
    output_string = ''
    for i in input_string:
        if i in ['.','(',')',' ']:
            output_string += i
        elif(i == 'y'):
            output_string += 'a'
        elif(i == 'z'):
            output_string += 'b'
        else:
            output_string += chr(ord(i) + 2)
    return output_string

def translateBackward(input_string):
    output_string = ''
    for i in input_string:
        if i in ['.','(',')',' ']:
            output_string += i
        elif(i == 'a'):
            output_string += 'y'
        elif(i == 'b'):
            output_string += 'z'
        else:
            output_string += chr(ord(i) - 2)
    return output_string

def main():
    input_string = '''
    g fmnc wms bgblr rpylqjyrc gr zw fylb. 
    rfyrq ufyr amknsrcpq ypc dmp. 
    bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
    sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. 
    lmu ynnjw ml rfc spj.
    '''
    print(translateForward(input_string))
    '''
    Output is :
    i hope you didnt translate it by hand.
    thats what computers are for.
    doing it in by hand is inefficient and that)s why this text is so long.
    using string.maketrans() is recommended.
    now apply on the url.
    '''
    print(translateBackward(input_string))
    '''
    output is:
    e dkla ukq zezjp pnwjohwpa ep xu dwjz.
    pdwpo sdwp ykilqpano wna bkn.
    zkejc ep ej xu dwjz eo ejabbeyeajp wjz pdwp%o sdu pdeo patp eo ok hkjc.
    qoejc opnejc.iwgapnwjo() eo naykiiajzaz.
    jks wllhu kj pda qnh
    '''
    # Now looking at output translate forward is correct and so we can try string.maketrans() on url as suggested
    # given url is : http://www.pythonchallenge.com/pc/def/map.html
    txt = "map"
    mytable = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
    print(txt.translate(mytable))
    # output : ocr
    # so new url is : http://www.pythonchallenge.com/pc/def/ocr.html
    # just checking if my function is correct
    print(translateForward(txt))
    # output : ocr

if __name__ == "__main__":
    main()


