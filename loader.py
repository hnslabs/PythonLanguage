#!/user/bin/env python3 -tt
"""
Module documentation.
"""


"""
#*****************************************************
#    https: // www.python - course.eu / python3_sequential_data_types.php
#    https: // www.sqlitetutorial.net
"""


# Imports
import sys
#import os

# Global variables

# Class declarations

# Function declarations

def main():
    #args = sys.argv[1:]

    #if not args:
    #    print('usage: [--flags options] [inputs] ')
    #    sys.exit(1)

    # oggetti:
    # qualsiasi variabile ha una indirizzo di memoria associato. Se due variabili puntano allo stesso valore o una variabile
    # e' uguale all'altra, entrambe avranno lo stesso indirizzo di memoria

    a = 10
    b = a
    # 10914784 10914784
    print(id(a), id(b))
    b = 11
    # 10914784 10914816
    print(id(a), id(b))

    # numero
    # •Integer
    #     ∙Normal integers
    #     e.g., 4321
    #     ∙Octal literals (base 8)
    #     A number prefixed by 0o (zero and a lowercase "o" or uppercase "O") will be interpreted as an octal number
    #     example:
    a = 0o10
    print(a)    # 8
    # ∙Hexadecimal literals (base 16)
    #     Hexadecimal literals have to be prefixed either by "0x" or "0X".
    #     example:
    hex_number = 0xA0F
    #
    print(hex_number) # 2575

    # ∙Binary literals (base 2)
    #     Binary literals can easily be written as well. They have to be prefixed by a leading "0", followed by a "b" or "B":
    x = 0b101010
    print(x)
    # Output: :
    # 42

    # The functions hex, bin, oct can be used to convert an integer number into the corresponding string representation of the integer number:
    #
    x = hex(19)
    print(x) # '0x13'

    print(type(x))
    # Output: :
    # str

    x = bin(65)
    print(x)
    # Output: :
    # '0b1000001'

    x = oct(65)
    # x
    # Output: :
    # '0o101'
    print(oct(0b101101))
    #
    # Output: :
    # '0o55'

    # STRINGHE
    # Name	Description
    # UTF-32	It's a one to one encoding, i.e., it takes each Unicode character (a 4-byte number)
    #           and stores it in 4 bytes. One advantage of this encoding is that you can find the Nth character of a
    #           string in linear time, because the Nth character starts at the 4×Nth byte. A serious disadvantage of
    #           this approach is due to the fact that it needs four bytes for every character.
    # UTF-16	UTF-16 (16-bit Unicode Transformation Format) is a character encoding capable of encoding all
    #           1,112,064 valid code points of Unicode. The encoding is variable-length, as code points are encoded
    #           with one or two 16-bit code units.
    # UTF-8	UTF8 is a variable-length encoding system for Unicode, i.e., different characters take up a different
    #           number of bytes. ASCII characters use solely one byte per character. This means that the first 128
    #           characters UTF-8 are indistinguishable from ASCII. But the so-called "Extended Latin" characters like
    #           the Umlaute ä, ö and so on take up two bytes. Chinese characters need three bytes. Finally, the very
    #           seldom used characters of the "astral plane" need four bytes to be encoded in UTF-8.
    #           W3Techs (Web Technology Surveys) writes that "UTF-8 is used by 94.3% of all the websites whose
    #           character encoding we know."

    # All strings in Python 3 are sequences of "pure" Unicode characters, no specific encoding like UTF-8
    s = 'I am a string enclosed in single quotes.'
    s2 = "I am another string, but I am enclosed in double quotes."
    s3 = 'It doesn\'t matter!'
    s3 = "It doesn't matter!"
    txt = "He said: \"It doesn't matter, if you enclose a string in single or double quotes!\""
    print(txt) # He said: "It doesn't matter, if you enclose a string in single or double quotes!"
    txt = '''A string in triple quotes can extend
    over multiple lines like this one, and can contain
    'single' and "double" quotes.'''

    s = "Hello World"
    s[0]    # Output:: 'H'
    s[5]    # Output:: ' '
    s[len(s) - 1]   # Output::   'd'
    s[-1]   # Output::     'd'

    # Like strings in Java and unlike C or C++, Python strings cannot be changed.
    # Trying to change an indexed position will raise an error

    txt = "He lives in Berlin!"
    txt = "He lives in Hamburg!" # questo comando crea un oggetto exnovo

    #  "a is b" checks if they have the same identity, i.e., share the same memory location. If "a is b" is True,
    #  then it trivially follows that "a == b" has to be True as well. Yet, "a == b" True doesn't imply
    #  that "a is b" is True as well!
    a = "Linux"
    b = "Linux"
    a is b # True

    # Strings show a special effect, which we will illustrate in the following example. We will need the "is"-Operator.
    # If both a and b are strings, "a is b" checks if they have the same identity, i.e., share the same memory location.
    # If "a is b" is True, then it trivially follows that "a == b" has to be True as well. Yet, "a == b" True
    # doesn't imply that "a is b" is True as well!
    #
    # IDENTITY
    # Every object has an identity, a type and a value. An object’s identity never changes once it has been created;
    # you may think of it as the object’s address in memory. The ‘is‘ operator compares the identity of two objects;
    # the id() function returns an integer representing its identity (currently implemented as its address).
    #
    # Let's have a look at how strings are stored in Python:
    #
    # a = "Linux"
    # b = "Linux"
    # a is b
    # Output: :
    # True
    # Okay, but what happens, if the strings are longer? We use the longest village name in the world in the
    # following example. It's a small village with about 3000 inhabitants in the South of the island of Anglesey in the North-West of Wales:
    #
    # a = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
    # b = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
    # a is b
    # Output: :
    # True
    # Nothing has changed in our first "Linux" example. But what works for Wales doesn't work e.g., for Baden-Württemberg in Germany:
    #
    # a = "Baden-Württemberg"
    # b = "Baden-Württemberg"
    # a is b
    # Output: :
    # False
    # a == b
    # Output: :
    # True
    # You are right, it has nothing to do with geographical places. The special character, i.e., the hyphen, is to "blame".
    #
    # a = "Baden!"
    # b = "Baden!"
    # a is b
    # Output: :
    # False
    # a = "Baden1"
    # b = "Baden1"
    # a is b
    # Output: :
    # True

    #String Escape
    # Escape Sequence	Meaning
    # \newline	        Ignored
    # \\	            Backslash (\)
    # \'	            Single quote (')
    # \"	            Double quote (")
    # \a	            ASCII Bell (BEL)
    # \b	            ASCII Backspace(BS)
    # \f	            ASCII Formfeed (FF)
    # \n	            ASCII Linefeed (LF)
    # \N{name}	        Character named name in the Unicode database (Unicode only)
    # \r	            ASCII Carriage Return (CR)
    # \t	            ASCII Horizontal Tab (TAB)
    # \uxxxx	        Character with 16-bit hex value xxxx (Unicode only)
    # \Uxxxxxxxx	    Character with 32-bit hex value xxxxxxxx (Unicode only)
    # \v	            ASCII Vertical Tab (VT)
    # \ooo	            Character with octal value ooo
    # \xhh	            Character with hex value hh

    # BYTE STRING
    # Python 3.0 uses the concepts of text and (binary) data instead of Unicode strings and 8-bit strings. Every string or text in Python 3 is Unicode, but encoded Unicode is represented as binary data. The type used to hold text is str, the type used to hold data is bytes. It's not possible to mix text and data in Python 3; it will raise TypeError. While a string object holds a sequence of characters (in Unicode), a bytes object holds a sequence of bytes, out of the range 0 to 255, representing the ASCII values. Defining bytes objects and casting them into strings:
    #
    x = "Hallo"
    t = str(x)
    u = t.encode("UTF-8")
    print(u) # b'Hallo'



    # Operator	Description	Example
    # +, -	                                Addition, Subtraction	                    10 -3
    # *, %	                                Multiplication, Modulo	                    27 % 7
    #                                                                                   Result: 6
    # /	                                    Division
    #                                       This operation brings about different results for Python 2.x
    #                                       (like floor division) and Python 3.x	Python3:
    #                                                                                   10  / 3
    #                                                                                   3.3333333333333335
    #                                                                                   and in Python 2.x:
    #                                                                                   10  / 3
    #                                                                                   3
    # //	                                Truncation Division (also known as floordivision or floor division)
    #                                       The result of this division is the integral part of the result,
    #                                       i.e. the fractional part is truncated, if there is any.
    #                                       It works both for integers and floating-point numbers,
    #                                       but there is a difference between the type of the results:
    #                                       If both the dividend and the divisor are integers, the result will also be an integer.
    #                                       If either the divident or the divisor is a float, the result will be the truncated result as a float.
    #                                                                                   10 // 3
    #                                                                                   3
    #                                       If at least one of the operands is a float value, we get a truncated float value as the result.
    #                                                                                   10.0 // 3
    #                                                                                   3.0
    #                                                                                   >>>
    #                                       A note about efficiency:
    #                                       The results of int(10 / 3) and 10 // 3 are equal.
    #                                       But the "//" division is more than two times as fast! You can see this here:
    #                                                                                   %%timeit
    #                                                                                   for x in range(1, 100):
    #                                                                                       y = int(100 / x):
    #                                                                                   100000 loops, best of 3: 11.1 μs per loop
    #
    #                                                                                   %%timeit
    #                                                                                   for x in range(1, 100):
    #                                                                                       y = 100 // x
    #                                                                                       :
    #                                                                                   100000 loops, best of 3: 4.48 μs per loop
    #
    # +x, -x	                            Unary minus and Unary plus (Algebraic signs)	-3
    # ~x	                                Bitwise negation	                            ~3 - 4
    #                                                                                       Result: -8
    # **	                                Exponentiation	                                10 ** 3
    #                                                                                       Result: 1000
    # or, and, not	                        Boolean Or, Boolean And, Boolean Not	        (a or b) and c
    # in	                                "Element of"	                                1 in [3, 2, 1]
    # <, <=, >, >=, !=, ==	                The usual comparison operators	                2 <= 3
    # |, &, ^	                            Bitwise Or, Bitwise And, Bitwise XOR	        6 ^ 3
    # <<, >>	                            Shift Operators                             	6 << 3


    #The byte object is a sequence of small integers. The elements of a byte object are in the range 0 to 255,
    # corresponding to ASCII characters and they are printed as such.

    s = "Glückliche Fügung"
    s_bytes = s.encode('utf-8')
    print(s_bytes)
    #Output::
    #b'Gl\xc3\xbcckliche F\xc3\xbcgung'

    # LIST
    # Generally speaking a list is a collection of objects. To be more precise: A list in Python is an ordered group of
    # items or elements. It's important to notice that these list elements don't have to be of the same type. It can be
    # an arbitrary mixture of elements like numbers, strings, other lists and so on
    # The main properties of Python lists:
    # •They are ordered
    # •The contain arbitrary objects
    # •Elements of a list can be accessed by an index
    # •They are arbitrarily nestable, i.e. they can contain other lists as sublists
    # •Variable size
    # •They are mutable, i.e. the elements of a list can be changed
    #
    # List	                                                    Description
    # []	                                                    An empty list
    # [1,1,2,3,5,8]	                                            A list of integers
    # [42, "What's the question?", 3.1415]	                    A list of mixed data types
    # ["Stuttgart", "Freiburg", "München", "Nürnberg", "Würzburg", "Ulm","Friedrichshafen", Zürich", "Wien"]	A list of Strings
    # [["London","England", 7556900], ["Paris","France",2193031], ["Bern", "Switzerland", 123466]]	            A nested list
    # ["High up", ["further down", ["and down", ["deep down", "the answer", 42]]]]	                            A deeply nested list

    # SUBLIST
    # Lists can have sublists as elements
    person = [["Marc", "Mayer"], ["17, Oxford Str", "12345", "London"], "07876-7876"]
    name = person[0]
    print(name)             #    ['Marc', 'Mayer']

    first_name = person[0][0]
    print(first_name)       #     Marc

    languages = ["Python", "C", "C++", "Java", "Perl"]
    languages[4] = "Lisp"
    print(languages)
    # Output::
    #['Python', 'C', 'C++', 'Java', 'Lisp']

    languages.append("Haskell")
    print(languages)
    #Output:: ['Python', 'C', 'C++', 'Java', 'Lisp', 'Haskell']

    languages.insert(1, "Perl")
    print(languages)
    # Output:: ['Python', 'Perl', 'C', 'C++', 'Java', 'Lisp', 'Haskell']
    shopping_list = ['milk', 'yoghurt', 'egg', 'butter', 'bread', 'bananas']

    # We go to a virtual supermarket. Fetch a cart and start shopping:

    shopping_list = ['milk', 'yoghurt', 'egg', 'butter', 'bread', 'bananas']
    cart = []
    #  "pop()"" removes the last element of the list and returns it
    article = shopping_list.pop()
    print(article, shopping_list)
    cart.append(article)
    print(cart)

    # we go on like this:
    article = shopping_list.pop()
    print("shopping_list:", shopping_list)
    cart.append(article)
    print("cart: ", cart)
    # output:
    # bananas['milk', 'yoghurt', 'egg', 'butter', 'bread']
    #['bananas']
    #shopping_list: ['milk', 'yoghurt', 'egg', 'butter']
    #cart: ['bananas', 'bread']


    # TUPLE
    # A tuple is an immutable list, i.e. a tuple cannot be changed in any way, once it has been created.
    # A tuple is defined analogously to lists, except the set of elements is enclosed in parentheses instead of square brackets.
    # The rules for indices are the same as for lists. Once a tuple has been created, you can't add elements to a tuple or remove elements from a tuple.
    #
    # Where is the benefit of tuples?
    #
    # •Tuples are faster than lists.
    # •If you know that some data doesn't have to be changed, you should use tuples instead of lists, because this
    # protects your data against accidental changes.
    # •The main advantage of tuples is that tuples can be used as keys in dictionaries, while lists can't.

    # SLICE
    # In many programming languages it can be quite tough to slice a part of a string and even harder,
    # if you like to address a "subarray". Python makes it very easy with its slice operator.
    # Slicing is often implemented in other languages as functions with possible names like "substring", "gstr" or "substr".
    #
    # So every time you want to extract part of a string or a list in Python, you should use the slice operator.
    # The syntax is simple. Actually it looks a little bit like accessing a single element with an index, but instead
    # of just one number, we have more, separated with a colon ":". We have a start and an end index, one or both of
    # them may be missing. It's best to study the mode of operation of slice by having a look at examples:
    slogan = "Python is great"
    first_six = slogan[0:6]
    first_six # Output:: 'Python'

    starting_at_five = slogan[5:]
    starting_at_five # Output:: 'n is great'

    a_copy = slogan[:]
    without_last_five = slogan[0:-5]
    without_last_five # Output:: 'Python is '

    # Syntactically, there is no difference on lists. We will return to our previous example with European city names:
    cities = ["Vienna", "London", "Paris", "Berlin", "Zurich", "Hamburg"]
    first_three = cities[0:3]
    # or easier:
    ...
    first_three = cities[:3]
    print(first_three) # ['Vienna', 'London', 'Paris']

    all_but_last_two = cities[:-2]
    print(all_but_last_two) # ['Vienna', 'London', 'Paris', 'Berlin']

    # Slicing works with three arguments as well. If the third argument is for example 3,
    # only every third element of the list, string or tuple from the range of the first two arguments will be taken.
    #
    # If s is a sequential data type, it works like this:
    #
    #  s[begin: end: step]
    # The resulting sequence consists of the following elements:
    #
    #  s[begin], s[begin + 1 * step], ... s[begin + i * step] for all (begin + i * step) < end.

    slogan = "Python under Linux is great"
    slogan[::3] # Output:: 'Ph d n  e'

    # LENGTH
    txt = "Hello World"
    len(txt) # Output:: 11

    a = ["Swen", 45, 3.54, "Basel"]
    len(a) # Output::  4

    # Concatenation of Sequences
    firstname = "Homer"
    surname = "Simpson"
    name = firstname + " " + surname
    print(name) # Homer Simpson

    colours1 = ["red", "green", "blue"]
    colours2 = ["black", "white"]
    colours = colours1 + colours2
    print(colours) # ['red', 'green', 'blue', 'black', 'white']
    # The augmented assignment "+=" which is well known for arithmetic assignments work for sequences as well.
    #
    # s += t
    #
    # is syntactically the same as:
    #
    # s = s + t
    #
    # But it is only syntactically the same. The implementation is different:
    # In the first case the left side has to be evaluated only once.
    # Augment assignments may be applied for mutable objects as an optimization.


    # Checking if an Element is Contained in List
    abc = ["a", "b", "c", "d", "e"]
    "a" in abc # True

    "a" not in abc # False
    "e" not in abc # False
    "f" not in abc # true

    #Repetitions
    # str * 4
    #
    # is the same as
    #
    # str + str + str + str
    3 * "xyz-" # 'xyz-xyz-xyz-'
    3 * ["a", "b", "c"] # ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']

    # ATTENZIONE
    x = ["a", "b", "c"]
    y = [x] * 4     # [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]

    # !!!!!! OKKIO
    y[0][0] = "p" # [['p', 'b', 'c'], ['p', 'b', 'c'], ['p', 'b', 'c'], ['p', 'b', 'c']]
    # questo perche' [x] * 4 crea una reference alla locazione di memoria di x
    # cambiando quindi il valore a y[0][0] si modifica in automatico su tutti gli x referenziati con lo stesso indirizzo
    # di memoria














    # Main body
if __name__ == '__main__':
    main()