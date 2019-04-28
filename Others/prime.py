# Question: Write a function that counts the number of primes in the range [1 - N]
def prime():
    input_range = input("Enter range: ")
    count = 0
    for num in range(2, input_range+1):
        if all(num%i!=0 for i in range(2, num)):
            print num
            count+= 1
    print "Number of primes = ",count        

prime()
