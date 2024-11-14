def find_min_max(lst):
    min_num = min(lst)
    max_num = max(lst)
    return min_num, max_num

numbers = list(map(int, input("یک لیست از اعداد را با فاصله وارد کنید: ").split()))
min_num, max_num = find_min_max(numbers)
print(f"کوچکترین عدد: {min_num}")
print(f"بزرگترین عدد: {max_num}")
