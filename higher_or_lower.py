from turtle import clear
import art
from game_data import data
import random

# print(art.logo)
list = []
for n in range(len(data)):
    list.append(n)

a = random.choice(list)
game_over = False
score = 0

while not game_over:
    list.remove(a)
    b = random.choice(list)

    a_name = data[a]['name']
    a_description = data[a]['description']
    a_country = data[a]['country']
    b_name = data[b]['name']
    b_description = data[b]['description']
    b_country = data[b]['country']

    print(art.logo)
    print(f"Compare A:{a_name},a {a_description},from {a_country}")
    print(art.vs)
    print(f"Compare B:{b_name},a {b_description},from {b_country}")

    guess = input("Who has more followers? Type'A' or 'B': ")
    clear()

    if guess == 'A':
        v1 = data[a]['follower_count']
        v2 = data[b]['follower_count']
    elif guess == 'B':
        v1 = data[b]['follower_count']
        v2 = data[a]['follower_count']

    if v1 > v2:
        #global score
        score += 1
        print(f"You're right! Currenct score: {score}.")
        a = b
    else:
        # clear()
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_over = True
