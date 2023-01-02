def mode(list):
    y = {}
    for a in list:
      if not a in y:
        y[a] = 1
      else:
        y[a] += 1

    return [g for g,l in y.items() if l == max(y.values())]

print(mode([33,89,45,6,89,7,89]))
