def filter_users(users):
    countries = ['USA', 'Canada']
    return [u[1] for u in users if u[2] > 30 and u[3] in countries]

def sort_users(users):
    return sorted(users, key=lambda x: x[2], reverse=True)[:10]

def find_dupes(users):
    names = [u[1] for u in users]
    return set([n for n in names if names.count(n) > 1])


users = [
    (1, 'John', 31, 'USA'), 
    (2, 'Alice', 29, 'Canada'), 
    (3, 'Bob', 32, 'Canada'), 
    (4, 'Eve', 33, 'UK'), 
    (5, 'John', 31, 'USA')
]

filtered = filter_users(users)
print("Filtered Users:", filtered)

top_10 = sort_users(users)
print("Top 10 Oldest Users:", top_10)

dupes = find_dupes(users)
print("Duplicate Names:", dupes)
