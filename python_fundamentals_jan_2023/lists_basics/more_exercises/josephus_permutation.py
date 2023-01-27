numbers = input().split()
executed_person_sequence = int(input())

executions_list = []
counter = 0

while len(numbers) > 0:
    for num in range(len(numbers)):
        counter += 1
        end_point = num

        if counter == executed_person_sequence:
            executions_list.append(numbers.pop(end_point))
            counter = 0
            numbers = numbers[end_point:] + numbers[:end_point]
            break

result = ",".join(executions_list)
print(f"[{result}]")
