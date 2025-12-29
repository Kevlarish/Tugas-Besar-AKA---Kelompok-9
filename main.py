import time
import random
import sys

print("=== PROGRAM PERBANDINGAN ===")
n = int(input("Masukkan jumlah data: "))

sys.setrecursionlimit(n + 5000)

arr = []
for i in range(n):
    arr.append(random.randint(1, 100))

def sum_iterative(arr):
    total = 0
    for i in range(len(arr)):
        total = total + arr[i]
    return total

start_iter = time.time()
hasil_iter = sum_iterative(arr)
end_iter = time.time()
waktu_iter = end_iter - start_iter

def sum_recursive(arr, n):
    if n == 0:
        return 0
    return arr[n-1] + sum_recursive(arr, n-1)

start_rec = time.time()
try:
    hasil_rec = sum_recursive(arr, n)
    end_rec = time.time()
    waktu_rec = end_rec - start_rec
except:
    waktu_rec = -1

print("-" * 30)
print(f"Total Penjumlahan: {hasil_iter}")
print("-" * 30)
print(f"Waktu Iteratif : {waktu_iter:.6f} detik")

if waktu_rec != -1:
    print(f"Waktu Rekursif : {waktu_rec:.6f} detik")
else:
    print("Waktu Rekursif : Gagal")
print("-" * 30)