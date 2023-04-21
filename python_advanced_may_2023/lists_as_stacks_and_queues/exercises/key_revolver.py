from collections import deque


def barrel_check(usage, barrel, total):
    if total and usage % barrel == 0:
        print("Reloading!")
        return


price_per_bullet = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split(" ")]  # usage from back to front
locks = deque([int(x) for x in input().split(" ")])  # usage from front to back
intelligence_value = int(input())

# Unlocking a lock only if the lock is equal to or larger than the bullet
used_bullets = 0

while locks and bullets:
    lock = locks[0]
    for _ in range(len(bullets)):
        bullet = bullets.pop()
        used_bullets += 1
        if lock >= bullet:
            print("Bang!")
            locks.popleft()
            barrel_check(used_bullets, gun_barrel_size, bullets)
            break
        else:
            print("Ping!")
            barrel_check(used_bullets, gun_barrel_size, bullets)

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    money_earned = intelligence_value - (used_bullets * price_per_bullet)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")

