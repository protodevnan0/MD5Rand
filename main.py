import hashlib
import random

print ("  MD5 Rand 1.0a");
print ("  Made by Jay");


word_try = ""; # Stores Your generated letters as a word
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
# For now numbers are removed because they slow everything down
attempts = 0; # Number of generated words

usrinp = input(" What hash are You trying to process?: "); # What hash You want to "decrypt"


while True: # Loops generating new words until they match word
 word_try = random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters); # Each random.choice(letters) generated one letter. So for 20 letters You'd want to use 20 of those
 hash_object = hashlib.md5(word_try.encode())
 attempts += 1;
 print (" Current hash: " + str(hash_object.hexdigest()) + " For word: " + str(word_try) + " | Amount of retries: " + str(attempts));
 if (hash_object.hexdigest() == usrinp): # Check generated hash if it matches Your input hash. 
  print (" Found hash: " + str(hash_object.hexdigest()) + " For word: " + str(word_try));
  break;


# Notes

# It's just a for fun project, if You're lucky, it might decrypt some hashes pretty quickly. 

# For real/faster decrypting purposes, You will find a lot better scripts on Github/Internet, just search for them. 
