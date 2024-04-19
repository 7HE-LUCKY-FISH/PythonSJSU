from collections import defaultdict

def count_frequency(arr):
    frequency = defaultdict(int)  # Default value of int is 0
    for item in arr:
        frequency[item] += 1
    return frequency

if __name__ == "__main__":
    arr = [1, 2, 2, 3,6,3,1,1,1, 3, 3, 4, 4, 4, 4]
    frequency = count_frequency(arr)
    
    for num, freq in frequency.items():
        print(f"Number {num} appears {freq} times.")
