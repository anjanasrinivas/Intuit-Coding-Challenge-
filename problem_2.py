import time

def prime_sieve(cap):

    n = cap + 1
    nprime = set()
    prime = []

    for i in range(2, n):
        print("Sieve Operation Completion: " + str((i/n) * 100))
        if i in nprime:
            continue
        for f in range(i*2, n, i):
            nprime.add(f)

        prime.append(i)

    return prime

def find_primes(array):
	start_time = time.time()

	maximum = max(array)
	n = 2
	
	while len(prime_sieve(n)) < maximum:
		n += 100000

	primeArray = prime_sieve(n)

	result = []
	
	for i in array:
		result.append(primeArray[i-1])

	print(result)
	print("--- Sieve Operation Completed in: %s seconds ---" % (time.time() - start_time))
	print (find_primes([3,58,10001]))
 




