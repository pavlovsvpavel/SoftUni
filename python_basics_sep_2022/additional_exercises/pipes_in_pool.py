pool_area = int(input())
first_pipe_flow = int(input())
second_pipe_flow = int(input())
hours_without_worker = float(input())

first_pipe_lt = first_pipe_flow * hours_without_worker
second_pipe_lt = second_pipe_flow * hours_without_worker
total_lt = first_pipe_lt + second_pipe_lt

pipe_1_pool_percentage = first_pipe_lt / total_lt * 100
pipe_2_pool_percentage = second_pipe_lt / total_lt * 100
total_pool_percentage = total_lt / pool_area * 100

diff = abs(total_lt - pool_area)

if total_lt <= pool_area:
    print(f"The pool is {total_pool_percentage:.2f}% full. Pipe 1: {pipe_1_pool_percentage:.2f}%. "
          f"Pipe 2: {pipe_2_pool_percentage:.2f}%.")
else:
    print(f"For {hours_without_worker:.2f} hours the pool overflows with {diff:.2f} liters.")
