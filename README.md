# ironhawks-keygen
IronHawks KeyGen v0.2.1

Effortlessly generate random passwords of custom lengths.

Uses Alphabets(Upper and Lower cases), Digits(0-9) and Special 
Characters/Punctuations(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~) of the 
'string' standard library and the 'random' standard library for the 
random character picking.

The available Strategies are:
1. Generate using Alphabets only.
2. Generate using Digits only.
3. Generate using Alphabets and Digits only.
4. Generate using Alphabets and Special Characters only.
5. Generate using Digits and Special Characters only.
6. Generate using Alphabets, Digits and Special Characters.

The Constants used are:
1. ALPHABETS - String having all Lower and Upper cases alphabets.
2. DIGITS - String having digits from 0 to 9.
3. SPECIAL_CHARACTERS - String having a selection of punctuation 
                        characters that are present on standard US 
                        keyboard and frequently used in passwords.
4. STRING_POOL - A dictionary having the possible startegies, where the 
                 keys represent the Strategy Number and their values 
                 represent the respective Strategy String used for 
                 password generation.

The generate() function has three optional parameters which are,
1. strategy_number - The corresponding number key to the strategy 
                     specified in the STRING_POOL dictionary. Default 
                     value is 6 for its robustness.
2. password_length - The preferred length of the password string to be
                     generated. Minimum is 8 and Maximum is 128. 
                     Recommended is 12 to 15 characters.
3. strict - Takes boolean(True/False). Enables Strict mode for 
Strategies 3 to 6, as Strategies 1 and 2 are always strict. Strict mode 
refers to the condition by which the randomness in generation always 
happens as preferred. For example, Strategy 3 may produce only digits or
 alphabets as it is randomly generated and thus, strict mode ensures 
there is atleast one digit or one alphabet in the generated password.

The generate() returns the generated password string or None if either 
strategy_number or password_length do not fall in the ranges [1,6] and 
[8,128] respectively.

The get_doc() function returns this whole docstring, if wanted.

Check out the included Example file(example.py).

Created by Praveen K. Contact: hartbrkrlegacy@gmail.com