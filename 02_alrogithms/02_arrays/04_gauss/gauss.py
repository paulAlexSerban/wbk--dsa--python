import time

def sum(n: int) ->int:
  result = 0
  for i in range(n + 1):
    result += i
  return result

def sum_optimized(n: int) -> int:
  return n * (n + 1) / 2

def measure_sum(ranges):
  print("\nMeasuring sum")
  for n in ranges:
    start = time.process_time_ns()
    sum(n)
    end = time.process_time_ns()
    exec_time = end - start
    print(f"sum {n} execution time {exec_time} ns")

def measure_sum_optimized(ranges):
  print("\nMeasuring sum_optimized")
  for n in ranges:
    start = time.process_time_ns()
    sum_optimized(n)
    end = time.process_time_ns()
    exec_time = end - start
    print(f"sum_optimized {n} execution time {exec_time} ns")
    
"""
Measuring sum
sum 10 execution time 100000 ns
sum 100 execution time 100000 ns
"""