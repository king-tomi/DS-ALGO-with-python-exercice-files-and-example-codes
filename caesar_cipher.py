class CaesarCipher:
    """
        A class for performing the caesar cipher encrypton and decryption for the English Language
        This is an example code for which i have added extra code as solutions to exercices

        Author: Ayodabo Tomisin Kolawole

        E-mail: ayodabooluwatomisin@gmail.com

        github: https://github.com/king-tomi
    """

    def __init__(self,shift: int):
        self._forward = "".join([chr((k + shift) % 26 + ord("A"))for k in range(26)])
        self._backward = "".join([chr((k - shift) % 26 + ord("A")) for k in range(26)])

    def encrypt(self,message: str) -> str:
        """encrypts a given message and returns a string containing the encrypted message"""
        return self._transform(message,self._forward)

    def decrypt(self,coded: str) -> str:
        """decrypts the coded message and returns a string containng the orginal message"""
        return self._transform(coded,self._backward)

    def _transform(self,message: str,code: str) -> str:
        """Utilitiy function for performing encryption and decryption"""
        msg = list(message)
        for i,v in enumerate(msg):
            if v.isupper():
                j = ord(v) - ord("A")
                msg[i] = code[j]
            elif v.islower():
                v = v.upper()
                j = ord(v) - ord("A")
                msg[i] = code[j]
        return "".join(msg)


if __name__ == "__main__":
    caesar = CaesarCipher(3)
    print(caesar.encrypt("HeLLo boy"))