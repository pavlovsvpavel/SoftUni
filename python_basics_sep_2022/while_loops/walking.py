daily_goal_steps = 10000
steps_per_walk = input()

total_steps = 0
while steps_per_walk != "Going home":
    steps_per_walk = int(steps_per_walk)
    total_steps += steps_per_walk

    if total_steps >= daily_goal_steps:
        break
    steps_per_walk = input()

if steps_per_walk == "Going home":
    steps_per_walk = input()
    steps_per_walk = int(steps_per_walk)
    total_steps += steps_per_walk

diff = abs(daily_goal_steps - total_steps)

if total_steps >= daily_goal_steps:
    print(f"Goal reached! Good job!\n{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
