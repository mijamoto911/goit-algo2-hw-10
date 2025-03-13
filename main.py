import random
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def randomized_quick_sort(arr):
    # Рандомізований QuickSort
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


# Детермінований QuickSort
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


# Функція для вимірювання часу виконання
def measure_time(sort_function, arr, runs=5):
    times = []
    for _ in range(runs):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_function(arr_copy)
        times.append(time.time() - start_time)
    return np.mean(times)


# Розміри тестових масивів
sizes = [10_000, 50_000, 100_000, 500_000]
randomized_times = []
deterministic_times = []

# Вимірювання часу виконання
for size in sizes:
    test_array = [random.randint(0, 10**6) for _ in range(size)]
    randomized_times.append(measure_time(randomized_quick_sort, test_array))
    deterministic_times.append(measure_time(deterministic_quick_sort, test_array))

# Виведення таблиці результатів
data = pd.DataFrame(
    {
        "Розмір масиву": sizes,
        "Час randomized QuickSort (сек)": randomized_times,
        "Час deterministic QuickSort (сек)": deterministic_times,
    }
)


print(data.to_string(index=False))

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(sizes, randomized_times, marker="o", label="Randomized QuickSort")
plt.plot(sizes, deterministic_times, marker="s", label="Deterministic QuickSort")
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (сек)")
plt.title("Порівняння Randomized та Deterministic QuickSort")
plt.legend()
plt.grid(True)
plt.show()
