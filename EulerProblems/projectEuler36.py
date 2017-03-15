print(sum(filter(lambda i: i%2==1 and str(i) == str(i)[::-1] and bin(i)[2:].lstrip('0') == bin(i)[2:].lstrip('0')[::-1], range(0,1000000) )))

        

