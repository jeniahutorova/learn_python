import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# Option 1
# print(random.choice(friends))

# Option 2
# who_will_pay = random.randint(0,4)
# if who_will_pay == 0:
#     print("Alice")
# elif who_will_pay == 1:
#     print("Bob")
# elif who_will_pay == 2:
#     print("Charlie")
# elif who_will_pay == 3:
#     print("David")
# elif who_will_pay == 4:
#     print("Emanuel")

# Option 3
who_will_pay = random.randint(0,4)
print(friends[who_will_pay])

