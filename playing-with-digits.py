def dig_pow(n, p):
  total = 0
  for i, count in enumerate(str(n)):
      total += pow(int(count), p+i)
  return total/n if total%n == 0 else -1