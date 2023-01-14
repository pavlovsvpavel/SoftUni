start_letter = input()
end_letter = input()
except_letter = input()

start_letter_num = ord(start_letter)
end_letter_num = ord(end_letter)
except_letter_num = ord(except_letter)

counter = 0
for i in range(start_letter_num, end_letter_num + 1):
    i = chr(i)
    for j in range(start_letter_num, end_letter_num + 1):
        j = chr(j)
        for k in range(start_letter_num, end_letter_num + 1):
            k = chr(k)
            if i != except_letter and j != except_letter and k != except_letter:
                counter += 1
                print(f"{i}{j}{k}", end=" ")

print(counter)



