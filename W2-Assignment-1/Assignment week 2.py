#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 22:14:44 2021

@author: lucas
"""

# 要求一:函式與流程控制 完成以下函式，在函式中​使用迴圈​計算最小值到最大值之間，所有整數的總和。
def calculate(min_number, max_number):
    total_sum = 0
    for i in range(min_number,max_number+1):
        total_sum += i
    print(total_sum)

# # 你的程式要能夠計算 1+2+3，最後印出 6 
# calculate(1, 3)
# # 你的程式要能夠計算 4+5+6+7+8，最後印出 30
# calculate(4, 8)


# 要求二:Python 字典與列表、JavaScript 物件與陣列 
# 完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。

def avg(data):
    total_employee_num = data['count']
    total_salary = 0
    total_employees = data['employees']
    for employee in total_employees:
        total_salary += employee['salary']
    
    avg_salary = total_salary / total_employee_num
    print(avg_salary)

# # 呼叫 avg 函式
# avg({
#     "count":3, "employees":[
#         {
#             "name":"John",
#             "salary":30000 },
#         {
#             "name":"Bob",
#             "salary":60000 },
#         {
#             "name":"Jenny",
#             "salary":50000 }
#     ]
# })

# 要求三:演算法
# 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
def maxProduct(nums):
    #sort
    nums.sort()
    
    max_num = 0
    
    if nums[0] * nums[1] > nums[-1] * nums[-2]:
        max_num = nums[0] * nums[1]
    else:
        max_num = nums[-1] * nums[-2]
    print(max_num)
    

# # 得到 120 因為 20 和 6 相乘得到最大值 
# maxProduct([5, 20, 2, 6])
# # 得到 30 因為 10 和 3 相乘得到最大值
# maxProduct([10, -20, 0, 3])

# 要求四 ( 請閱讀英文 ):演算法
# Given an array of integers, show indices of the two numbers such that they add up to a specific target. 
# You can assume that each input would have exactly one solution, and you can not use the same element twice.

def twoSum(nums, target):
# your code here
    # Solution 1 : N X N nesting
    # for i in nums:
    #     if target - i in nums and nums.index(i) != nums.index(target - i):
    #         return [nums.index(i),nums.index(target - i)]
    
    # Solution 2 : hash table
    hash_table = {}
    for i in range(len(nums)):
        hash_table[nums[i]] = i
    for num in nums:
        if target - num in hash_table and hash_table[num] != hash_table[target - num]:
            return [hash_table[num],hash_table[target - num]]

    
# result=twoSum([2, 11, 7, 15], 9)
# # ​show [0, 2] because nums[0]+nums[2] is 9
# print(result)

# 要求五 ( Optional ):演算法
# 給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大長度。

def maxZeros(nums):
# 請用你的程式補完這個函式的區塊 
    max_zero = 0
    temp = 0
    for num in nums:
        if num == 0:
            temp += 1
        else:
            temp = 0
        if temp > max_zero:
            max_zero = temp 
    print(max_zero)

# 得到 2
maxZeros([0, 1, 0, 0])
# 得到 4
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
# 得到 0
maxZeros([1, 1, 1, 1, 1])














