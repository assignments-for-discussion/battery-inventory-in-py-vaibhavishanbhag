
count_low =0
medium = 0
high = 0

def count_batteries_by_usage(cycles):
  count_low = 0
  medium = 0
  high = 0

  cycles=[100,200,400,600,900,1000]
  for i in cycles:
    if i<400:
      count_low =count_low+1
    elif i in range(400,920):
      medium=medium+1
    elif i >=920:
      high = high +1

    print(count_low)
    print(medium)
    print(high)


