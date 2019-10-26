# -----------------------------------------------------------------------------
#
# Copyright: Justin Scott Giboney, 2019
#
# This code is only to be used for testing the IT&C 366 encryption lab at
# Brigham Young University.
# 
# No permission is granted to redistribute, replicate, mimic, copy, or modify 
# this code.
#
# No warranty is given either. This may annihilate your computer, your files,
# your life, and/or humanity. Use at your own risk! 
#
# -----------------------------------------------------------------------------

import importlib, os


# Setup the student libraries to run.
studentModuleDirectory = 'studentLibrary/' # This should be in a config file
studentModules = {}

for module in os.listdir(os.path.dirname(studentModuleDirectory)):
    module_path = studentModuleDirectory[:-1]+'.'+module
    if module_path[-11:] != '__init__.py' and module_path[-3:] == '.py':
        studentModules[module] = importlib.import_module(module_path[:-3])
del module


# These should be in a config file
key = 'attacker'
message = 'thefighterswillstriketheenemybasesatnoona5'
transposeColumnarEncryptedMessage = 'teteeafwkmt iieyn hlhao gltbo tsesn hrrns5esiea '
transposeColumnarDecryptedMessage = 'thefighterswillstriketheenemybasesatnoona5      '
alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
rotation = 5
substitutionRotationEncryptedMessage = 'ymjknlmyjwx1nqqxywnpjymjjsjr3gfxjxfysttsfa'
runningKeyAlphabet = 'abcdefghijklmnopqrstuvwxyz'
runningKeyMessage = 'richardwill'
runningKeyKey = 'withmuchint'
runningKeyEncryptedMessage = 'nqvomlfdqye'


# Loop through the student libraries and run the encryption and decryption functions.
for module in studentModules.keys():

    try:
        encryptedString = studentModules[module].substitutionRotationEncrypt(alphabet,rotation,message)
        if encryptedString == substitutionRotationEncryptedMessage:
            print('substitution rotation encryption correct.')
        else:
            print('substitution rotation encryption NOT correct.')
    except:
        print('running substitutionRotationEncrypt failed.')

    try:
        decryptedString = studentModules[module].substitutionRotationDecrypt(alphabet,rotation,substitutionRotationEncryptedMessage)
        if decryptedString == message:
            print('substitution rotation decryption correct.')
        else:
            print('substitution rotation decryption NOT correct.')
    except:
        print('running substitutionRotationDecrypt failed.')

    try:
        encryptedString = studentModules[module].runningKeyCipherEncrypt(runningKeyAlphabet,runningKeyKey,runningKeyMessage)
        if encryptedString == runningKeyEncryptedMessage:
            print('running key encryption correct.')
        else:
            print('running key encryption NOT correct.')
    except:
        print('running runningKeyEncryption failed.')

    try:
        decryptedString = studentModules[module].runningKeyCipherDecrypt(runningKeyAlphabet,runningKeyKey,runningKeyEncryptedMessage)
        if decryptedString == runningKeyMessage:
            print('running key decryption correct.')
        else:
            print('running key decryption NOT correct.')
    except:
        print('running runningKeyDecrypt failed.')

    try:
        encryptedString = studentModules[module].transposeColumnarEncrypt(key,message)
        if encryptedString == transposeColumnarEncryptedMessage:
            print('transpose columnar encryption correct.')
        else:
            print('transpose columnar encryption NOT correct.')
    except:
        print('running transposeColumnarEncrypt failed.')

    try:
        decryptedMessage = studentModules[module].transposeColumnarDecrypt(key,transposeColumnarEncryptedMessage)
        if transposeColumnarDecryptedMessage == decryptedMessage:
            print('transpose columnar decryption correct.')
        else:
            print('transpose columnar decryption NOT correct.')
    except:
        print('running transposeColumnarDecrypt failed.')


    studentModules[module].desHexEncrypt('133457799BBCDFF1','0123456789ABCDEF')





