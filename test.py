import hill_cipher

# first setting message
message = "noWhiteSpaceAllowed"

# creating encrypter object
encrypter = hill_cipher.HillCipherEncrypter()
# encrypt object and store in ecrypt_message
ecrypt_message = encrypter.encrypt(message)

# decrypter created with encrypter key (keys should be same)
decrypter = hill_cipher.HillCipherDecrypter(key=encrypter._key)
# store decrypted message in decrypt_msg
decrypt_msg = decrypter.decrypt(ecrypt_message)