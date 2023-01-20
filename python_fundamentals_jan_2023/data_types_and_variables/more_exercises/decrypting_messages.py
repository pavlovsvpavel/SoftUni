key = int(input())
count_letters = int(input())

message = []

for _ in range(count_letters):
    letter = input()
    decrypted_letter = ord(letter) + key
    message.append(chr(decrypted_letter))

print("".join(message))
