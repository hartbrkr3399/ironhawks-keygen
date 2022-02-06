# ironhawks-keygen
IronHawks KeyGen v0.1

Effortlessly generate random passwords of custom lengths.

Uses Alphabets(Upper and Lower cases), Digits(0-9) 
and Special Characters(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~) and  
the 'random' standard library for the random character picking.

The available Strategies are:
1. Generate using Alphabets only.
2. Generate using Digits only.
3. Generate using Alphabets and Digits only.
4. Generate using Alphabets and Special Characters only.
5. Generate using Digits and Special Characters only.
6. Generate using Alphabets, Digits and Special Characters.

The Constants used are:
1. ALPHABETS - String having all Lower and Upper cases alphabets.
2. DIGITS - Straing having digits from 0 to 9.
3. SPECIAL_CHARACTERS - String having a selection of punctuation 
                        characters that are present on standard US 
                        keyboard and frequently used in passwords.
4. STRING_POOL - A dictionary having the possible startegies, where the 
                 keys represent the Strategy Number and their values 
                 represent the respective Strategy String used for 
                 password generation.

The generate() function has two optional parameters which are:
1. strategy_number - The corresponding number key to the strategy 
                     specified in the STRING_POOL dictionary. Default 
                     value is 6 for its robustness.
2. password_length - The preferred length of the password string to be
                     generated. Minimum is 8 and Maximum is 128. 
                     Recommended is 12 to 15 characters.
and it returns the generated password string or None if either 
strategy_number or password_length do not fall in the ranges [1,6] and 
[8,128] respectively.

The get_doc() function returns this whole docstring, if wanted.

Created by Praveen K. Contact: hartbrkrlegacy@gmail.com