import hill_cipher

message = "noWhiteSpaceAllowed"

encrypter = hill_cipher.HillCipherEncrypter()
ecrypt_message = encrypter.encrypt(message)

decrypter = hill_cipher.HillCipherDecrypter(key=encrypter._key)
decrypt_msg = decrypter.decrypt(ecrypt_message)