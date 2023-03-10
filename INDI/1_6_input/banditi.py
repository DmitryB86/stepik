# g, l = map(int, input().split())
# total_cans = g + l - 1
# gg = total_cans - g
# ll = total_cans - l
# print(gg, ll)
#

# r,g,b = map(int, input().split())
# print(r,g,b)

def fibonacci(n):
    print('He we start our generator')
    fib1, fib2 = 0, 1
    print('Init is ready, starting loop with n =', n)
    for i in range(n):
        if i == 0:
            print('It is our first iteration')
        fib1, fib2 = fib2, fib1 + fib2
        print('Going to yield value', fib1, 'while i =', i)
        yield fib1
        print('We are back again! i is still', i, 'and fib1 =', fib1, 'fib2 =', fib2)
    print("It's the last line of our generator... Buy!")
list(fibonacci(5))