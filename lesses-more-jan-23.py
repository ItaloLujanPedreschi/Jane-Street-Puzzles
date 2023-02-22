# Goal
# Find f(a,b,c,d) in which M is maximized and the sum of a,b,c,d are minimized
# Steps
# 1. Find max value of M
# 2. Find min sum of a,b,c,d that result in value M

class Solution:
  def __init__(self):
    self.memo = dict()

  def find_m_recursive(self, nums):
    print(nums)
    if nums in self.memo:
      return self.memo[nums]
    a, b, c, d = nums
    if a == b == c == d == 0:
      return 1

    new_nums = (abs(a - b), abs(b - c), abs(c - d), abs(d - a))
    m = self.find_m_recursive(new_nums) + 1
    self.store_nums_in_memo(nums, m)
    return m

  def store_nums_in_memo(self, nums, m):
    a, b, c, d = nums
    self.memo[(a, b, c, d)] = m
    self.memo[(b, c, d, a)] = m
    self.memo[(c, d, a, b)] = m
    self.memo[(d, a, b, c)] = m
    self.memo[(d, c, b, a)] = m
    self.memo[(a, d, c, b)] = m
    self.memo[(b, a, d, c)] = m
    self.memo[(c, b, a, d)] = m


soln = Solution()
# print(soln.find_m_recursive((1389537, 2555757, 4700770, 8646064)))
print(soln.find_m_recursive((0, 1389537, 3945294, 8646064)))


# (0, 1, 2, 4) - Top
# (1, 1, 2, 4) + 1, 0, 0, 1
# (0, 1, 2, 3)
# (1, 1, 1, 3)
# (0, 0, 2, 2)
# (0, 2, 0, 2)
# (2, 2, 2, 2)
# (0, 0, 0, 0)

# (0, 2, 6, 13) - Top
# (2, 4, 7, 13) + 0, 1, 1, 2
# (2, 3, 6, 11) + 1, 0, 1, 2
# (1, 3, 5, 9)
# (2, 2, 4, 8)
# (0, 2, 4, 6)
# (2, 2, 2, 6)
# (0, 0, 4, 4)
# (0, 4, 0, 4)
# (4, 4, 4, 4)
# (0, 0, 0, 0)

# (0, 7, 20, 44) - Top
# (7, 13, 24, 44) + 1, 2, 4, 7
# (6, 11, 20, 37) + 1, 2, 3, 6
# (5, 9, 17, 31) + 1, 1, 3, 5
# (4, 8, 14, 26) + 0, 2, 2, 4
# (4, 6, 12, 22) + 2, 0, 2, 4
# (2, 6, 10, 18)
# (4, 4, 8, 16)
# (0, 4, 8, 12)
# (4, 4, 4, 12)
# (0, 0, 8, 8)
# (0, 8, 0, 8)
# (8, 8, 8, 8)
# (0, 0, 0, 0)

# 15 + 3x = 24 + x
# 2x = 22
# x = 11

# (0,  24, 68,149) - Top
# (24, 44, 81,149) + 4, 7, 13, 24
# (20, 37, 68,125) + 3, 6, 11, 20
# (17, 31, 57,105) + 3, 5, 9, 17
# (14, 26, 48, 88) + 2, 4, 8, 14
# (12, 22, 40, 74) + 2, 4, 6, 8
# (10, 18, 34, 62) + 2, 2, 6, 10
# (8,  16, 28, 52)
# (8,  12, 24, 44)
# (4,  12, 20, 36)
# (8,   8, 16, 32)
# (0,   8, 16, 24)
# (8,   8,  8, 24)
# (0,   0, 16, 16)
# (0,  16,  0, 16)
# (16, 16, 16, 16)
# (0, 0, 0, 0)

# 35 + 3x = 57 + x
# 2x = 22
# x = 11

# (0, 1389537, 3945294, 8646064)
# (1389537, 2555757, 4700770, 8646064)

# (68,125,230,423) + 11, 20, 37, 68
# (57,105,193,355) + 9, 17, 31, 57
# (48, 88,162,298) + 8, 14, 26, 48
# (40, 74,136,250) + 6, 12, 32, 40
# (34, 62,104,210) + 6, 10, 8, 34
# (28, 52, 96,176)
# (24, 44, 80,148)
# (20, 36, 68,124)
# (16, 32, 56,104)
# (16, 24, 48, 88)
# (8,  24, 40, 72)
# (16, 16, 32, 64)
# (0,  16, 32, 48)
# (16, 16, 16, 48)
# (0,   0, 32, 32)
# (0,  32,  0, 32)
# (32, 32, 32, 32)
# (0, 0, 0, 0)

# 1, 5, 17


def bubble_up(nums):
  m = 7
  while nums[-1] < 10000000:
    if can_bubble(nums):
      nums = bubble(nums)
      m += 1
    else:
      nums = [num * 2 for num in nums]
    print(nums)
  print(m)
  return nums

def bubble(nums):
  a, b, c, d = nums
  new_a = a
  new_b = new_a + a
  new_c = new_b + b
  new_d = new_c + c
  left = (new_b - b) + (new_c - c)
  right = new_d - d
  factor = (right - left) // 2
  return [num + factor for num in [new_a, new_b, new_c, new_d]]


def can_bubble(nums):
  a, b, c, d = nums
  new_a = a
  new_b = new_a + a
  new_c = new_b + b
  new_d = new_c + c
  left = (new_b - b) + (new_c - c)
  right = new_d - d
  return (right - left) % 2 == 0


# print(bubble_up([1, 1, 2, 4]))
print(can_bubble((1389537, 2555757, 4700770, 8646064)))
print(can_bubble((0, 1389537, 3945294, 8646064)))
print(bubble((0, 1389537, 3945294, 8646064)))

# 0;1389537;3945294;8646064
