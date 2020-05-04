from mpmath import mp, mpf, ceil, sqrt

def PI(precision):
    
    num_iterations = int(ceil(precision / 14)) + 10 #Every iteration in Chudnovsky Algorithm produces approximately 14.18 digits, added 10 more digits for precision
    mp.dps = precision + 10 # Added 10 more for more precision
    
    K, M, X, L, S = 6, 1, 1, 13591409, 13591409

    for k in range(1, num_iterations + 1):
        M = (K ** 3 - 16 * K) * M / k ** 3
        K += 12
        L += 545140134
        X *= -262537412640768000
        S += mpf(M * L) / X
        
    C = 426880 * sqrt(10005)
    pi = C / mpf(S)
    
    print(str(pi)[:precision+2])

if __name__ == "__main__":
    n = input("Enter the number of digits of PI to be calculated")
    PI(int(n))
