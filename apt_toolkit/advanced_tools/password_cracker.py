import hashlib
import sys

def crack_password(hash_to_crack, wordlist):
    with open(wordlist, "r") as f:
        for line in f:
            word = line.strip()
            hashed_word = hashlib.sha256(word.encode()).hexdigest()
            if hashed_word == hash_to_crack:
                print(f"Password found: {word}")
                return
    print("Password not found.")

def main():
    hash_to_crack = input("Enter hash to crack: ")
    wordlist = input("Enter wordlist path: ")
    crack_password(hash_to_crack, wordlist)

if __name__ == "__main__":
    main()
