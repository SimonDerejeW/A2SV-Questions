def countSwaps(a):
    size = len(a)
    count = 0
    for i in range(size):
      for j in range(size-i-1):
        if a[j]>a[j+1]:
          a[j],a[j+1] = a[j+1],a[j]
          count+=1
    print("Array is sorted in " + str(count) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[len(a)-1]))
