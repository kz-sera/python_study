
import random as rand

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(num_list)

# print(num_list[8])
# print(num_list[4])

rand_int = rand.randint(0, 8)
# print('rand_int:', rand_int)
# print(num_list[rand_int])

trump_rand =rand.randint(0, 12)
trump_card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
print(trump_card[trump_rand])