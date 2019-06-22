
starting_funds = 10000
day_one = 0
interest = .014

def func(total, count, interest):
  inc_profit = (total * (interest + 1)) - total
  total = total * (interest + 1)
  count = count + 1
  print("Day :: " + str(count) + " :: " + "{:,}".format(int(total)))
  print("Incremental Profit :: " + "{:,}".format(int(inc_profit)))
  if count < 365:
    func(total, count, interest)

func(starting_funds, day_one, interest)
