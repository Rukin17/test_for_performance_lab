import sys


def get_min_moves(nums: list) -> int:
    n = len(nums)
    if n == 0:
        return 0
    
    median = sorted(nums)[n // 2]
    moves = (sum(abs(num - median) for num in nums))

    return moves


if __name__ == '__main__':
    file_path = sys.argv[1]
    with open(file_path, 'r') as f:
        nums = [int(num) for num in f.read().split()]
        print(get_min_moves(nums))
