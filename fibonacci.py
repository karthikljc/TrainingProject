


def fiblist(n):
    #creates a list of Fibonacci numbers up to the n-th generation 
    fib = [0,1]
    print("fib series 12345")
    for i in range(1,n):
        fib += [fib[-1]+fib[-2]]
    return fib

if __name__ == "__main__":
    if fib(0) == 0 and fib(10) == 55 and fib(50) == 12586269025:
        print(" fib function was successful!")
    else:
        print("The fib function is returning wrong values!")
