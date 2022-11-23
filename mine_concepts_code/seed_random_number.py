import random

# random.seed(1)
for i in range(1, 5):
    print(random.randint(1, 6))

# random.seed(1)
for i in range(1, 5):
    print(random.randint(1, 6))

# select unique elements
print(random.sample([1, 2, 3, 4, 5], 3))

# -----------

# get float val in range
f1 = random.uniform(1, 3)
print(f1)

# choice
l = [1,2,3,4,5]
c1 = random.choice(l)

# proportional sampling
l = [20, 30, 40, 10]
c2 = random.choices(l, weights=[2,3,4,1], k=10)
print(c2)


# Shuffle
cards = random.shuffle(list(range(1,20)))
sample = random.sample(cards, k=3)  # sample will pick unique vals