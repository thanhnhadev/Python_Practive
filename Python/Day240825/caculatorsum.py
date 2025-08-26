from multiprocessing  import Pool
import time
def caculator_sum(n):
    total = sum(range (1, n+1))
    return total

if __name__ == "__name__":
    number= [10000,20000,30000,40000]
    with Pool(processes=4) as pool:
        results = pool.map(caculator_sum, number)
    print(results)