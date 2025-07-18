import math
import random

# 9. Prime Number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 10. Sum of Digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

# 11. LCM and GCD
def lcm_and_gcd(a, b):
    gcd = math.gcd(a, b)
    lcm = abs(a * b) // gcd if a and b else 0
    return lcm, gcd

# 12. List Reversal
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

# 13. Sort a List (Bubble Sort)
def sort_list(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# 14. Remove Duplicates
def remove_duplicates(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

# 15. String Length without len()
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

# 16. Count Vowels and Consonants
def count_vowels_and_consonants(s):
    vowels = set("aeiouAEIOU")
    v = c = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v += 1
            else:
                c += 1
    return v, c

# 2. Maze Generator and Solver using DFS
def generate_maze(rows, cols):
    maze = [[1 for _ in range(cols)] for _ in range(rows)]
    def carve(x, y):
        dirs = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 < nx < rows and 0 < ny < cols and maze[nx][ny] == 1:
                maze[nx][ny] = 0
                maze[x + dx // 2][y + dy // 2] = 0
                carve(nx, ny)
    maze[1][1] = 0
    carve(1, 1)
    return maze

def solve_maze(maze, x=1, y=1, path=[]):
    if not (0 <= x < len(maze) and 0 <= y < len(maze[0])) or maze[x][y] != 0:
        return False
    if (x, y) == (len(maze) - 2, len(maze[0]) - 2):
        path.append((x, y))
        return True
    maze[x][y] = 2
    for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
        if solve_maze(maze, x+dx, y+dy, path):
            path.append((x, y))
            return True
    return False

def display_maze(maze):
    for row in maze:
        print(''.join(['#' if cell == 1 else ' ' if cell == 0 else '.' for cell in row]))

# Demo Execution (you can comment/uncomment below to test)
if __name__ == "__main__":
    print("Prime Check (7):", is_prime(7))
    print("Sum of Digits (123):", sum_of_digits(123))
    print("LCM and GCD (12, 18):", lcm_and_gcd(12, 18))
    print("Reversed List [1,2,3]:", reverse_list([1,2,3]))
    print("Sorted List [3,1,2]:", sort_list([3,1,2]))
    print("Remove Duplicates [1,1,2,2,3]:", remove_duplicates([1,1,2,2,3]))
    print("String Length ('hello'):", string_length("hello"))
    print("Vowels & Consonants ('hello'):", count_vowels_and_consonants("hello"))
    
    print("\nGenerated Maze and Solution Path:")
    maze = generate_maze(15, 15)
    path = []
    if solve_maze(maze, 1, 1, path):
        for x, y in path:
            maze[x][y] = 2
    display_maze(maze)
