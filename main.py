#Andrew DeMarco

import randStr
import random
# when i add the random seed, every time i run the code
# it gives the same result. if i don't have it, it gives
# different results every time.

print("randWord Outcomes:")
print(randStr.randWord("Python is fun"))
print(randStr.randWord("It's way better than java"))
print(randStr.randWord("My name is Andrew"))
random.seed(2)
print(randStr.randWord("My name is Andrew"))
random.seed(2)
print(randStr.randWord("My name is Andrew"))
print("\n")

print("strMixer Outcomes: ")
print(randStr.strMixer("I love to travel"))
print(randStr.strMixer("I really want to go to"))
print(randStr.strMixer("Thailand"))
random.seed(0)
print(randStr.strMixer("and Australia"))
print(randStr.strMixer("Australia"))
print("\n")

print("randIntForWord Outcomes: ")
print(randStr.randIntForWord("Andrew"))
print(randStr.randIntForWord("is"))
print(randStr.randIntForWord("My"))
print(randStr.randIntForWord("Name"))
print(randStr.randIntForWord("Andrew"))
print("\n")
