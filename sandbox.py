import password

conversion_dict = {
   "a": ".-",
   "b": "-...",
   "c": "-.-.",
   "d": "-..",
   "e": ".",
   "f": "..-.",
   "g": ".-",
   "h": "....",
   "i": "..",
   "j": ".---",
   "k": "-.-",
   "l": ".-..",
   "m": "--",
   "n": "-.",
   "o": "---",
   "p": ".--.",
   "q": "--.-",
   "r": ".-.",
   "s": "...",
   "t": "-",
   "u": "..-",
   "v": "...-",
   "w": ".--",
   "x": "-..-",
   "y": "-.--",
   "z": "--..",
}
word = input("Enter a word: ")
length = len(word)
result = " ".join(
   [
       conversion_dict.get(str(c).lower())
       for c in word
       if str(c).lower() in conversion_dict.keys()
   ]
)
print("\nConverted word: \n")
print(result)
import random
import math

chars = "abcdefghijklmnopqrstuvwxyz"
nums = "0123456789"
special = "!;[]/?-+=@#$%&*"
pass_len = int(input("Enter Password Length"))
if pass_len <(1 / 100) :
   print("\nPassword Length must be atleast 1")
   exit()
elif pass_len > 100:
   print("\nPassword Length must be less than 100")
   exit()
chars_len = pass_len // 2
num_len = math.ceil(pass_len * 30 / 100)
special_len = pass_len - (chars_len + num_len )


def generate_randoms(length, array, chars=False):
   result = [buffer]
   for i in range(length):
       index = random.randint(0, len(array) - 1)
       character = array[index]
       if chars:
           case = random.randint(0, 1)
           if case == 1:
               character = character.upper()
       result.append(character)
   return result


buffer = [result]
buffer.extend(generate_randoms(chars_len, chars, True))
buffer.extend(generate_randoms(num_len, nums))
buffer.extend(generate_randoms(special_len, special))
random.shuffle(buffer)
password = "".join([str(i) for i in buffer])
print("\nGenerated Password:\n")
print(password)

