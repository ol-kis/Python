def f():
    while True:
        try:
            count = int(input("Enter number of count: "))
            num_filt = [x for x in range(
                20, count+1) if not x % 20 or not x % 21]
            break
        except ValueError:
            print("You entered not number. Try again! ")

    print("Resuit: " + (", ").join(map(str, num_filt)))


f()
