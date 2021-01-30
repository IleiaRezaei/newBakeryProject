import pyfiglet

bread = {
  "sangak" : 20,
  "barbari" : 15,
  "lavash" : 13,
  "taftoon" : 25
}


print("we have sangak, barbari, lavash, and taftoon.")
sum = 0

answer = "yes"
while answer != "no":
  buy = input("what do you want? ")

  price = bread[buy]
  print("That will be", price, "each")
  count = input("How many do you want? ")
  finalprice = int(count) * price
  print("That will be", finalprice)
  sum = sum + finalprice

  answer = input("Do you want anything else? ")

print("--------")

print("Your total sum is:")
print(pyfiglet.figlet_format(str(sum)))
