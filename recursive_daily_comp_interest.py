#This recursive python function calculates daily compounding interest.

starting_funds = 10000
day_one = 0

def func(total, count):
  print("{:,}".format(int(total * 1.014) - total))
  total = total * 1.014
  count = count + 1
  print(str(count) + " :: " + "{:,}".format(int(total)))
  if count < 365:
    func(total, count)

func(starting_funds, day_one)
