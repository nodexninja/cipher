alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if (not (direction == 'encode' or direction == 'decode')):
  direction = input("Invalid command. Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
try:
  shift = int(input("Type the shift number:\n"))
except:
  shift = int(input("Invalid Input. Type the shift number:\n"))
if (direction == 'encode'):
  crypt = ''
  for i, char in enumerate(text):
    if (char in alphabet):
      crypt = crypt + alphabet[(alphabet.index(char) + shift) % len(alphabet)]
    else:
      crypt = crypt + char
  print(f'Your encrypted code:\n{crypt}')
elif (direction == 'decode'):
  crypt = ''
  for i, char in enumerate(text):
    if (char in alphabet):
      crypt = crypt + alphabet[alphabet.index(char) - shift]
    else:
      crypt = crypt + char
  print(f'Your decrypted message:\n{crypt}')