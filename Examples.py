greek_island = "Santorini"
print(greek_island)
# Example 1b Assignment operator w/ integer & tuple (+=)
earth_age_bln = 4.4
universe_age_bln = 14
earth_age_bln += 0.1

print(earth_age_bln)
# Example 1c: Assignment operator w/ list (=)
asia_wishlist = ["Bhutan", "Ha Long", "Laos", "Danxia", "Seoul", "Khao Sok", "Cebu", "Chiang Mai", "Ho Chi Minh"]
# Example 2a: Relational (comparison) operator (==)
msg = "life is beautiful"
if msg == "I love you":
    print("propose")
else:
    print("wait xP")
# Example 2b: Relational (comparison) operator (>=)
net_earnings = 10000.000
if net_earnings >= 100000.000:
    print("Large Cap")
else:
    print("Small Cap")
# Example 3a: Membership operator (in)
lst = ["soccer", "swimming", "running", "skiing"]
if "rock climbing" not in lst:
    print("boo")
# Example 3b: Membership operator (not in)
web_data = ["tech research and computer vision"]
if "@" in web_data:
    print("e-mail address")
elif "0123456789" in web_data:
    print("phone number")
else:
    print(not "e-mail nor phone number")

# Example 4: Arithmetic operator (+, -, *, /, //, **, %)
# a = 10+20
# b = 100 - 1
# c = 50 / 7
# d = 50 // 7
# e = 10 % 8
# f = 5 ** 2
#
# print(a, b, c, d, e, f, sep="\n")

number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

helloworld = "hello" + " " + "world"
print(helloworld)

even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1, 2, 3] * 3)

x = object()
y = object()


x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

lst = ["yellow", "white", "blue"]
print(lst)

a = 10
b = 3

result = a/b
print(result)

vertical_speed = 750

vertical_speed += 100

print(vertical_speed)
remainder = 1000 % 400

print(remainder)

p_result = 11111 ** 2

print(p_result)

lst = ["Mango", "Kiwi", "Melon", "Cherry"]
if lst[0] == "strawberry":
    answer_1 = "Yes"

else:
    answer_1 = "No"
print(answer_1)
