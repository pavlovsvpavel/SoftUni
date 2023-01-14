walk_minutes = int(input())
walks_count = int(input())
calories_per_day = int(input())

calories_per_all_walks = walk_minutes * 5 * walks_count

if (calories_per_all_walks / calories_per_day) >= 0.5:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_per_all_walks}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_per_all_walks}.")

