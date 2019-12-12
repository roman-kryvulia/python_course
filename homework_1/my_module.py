
def my_sort(a):

  my_sort = list(filter(None,a.keys()))
  my_sort.sort()

  for i in my_sort:
      if a[i] == 1: print(i, a[i], 'time')
      else: print(i, a[i], 'times')
