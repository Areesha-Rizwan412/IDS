# Function to find users who visited both Page A and Page B
def users_visited_both(page_a, page_b):
    return page_a.intersection(page_b)

# Function to find users who visited either Page A or Page C, but not both
def users_visited_either(page_a, page_c):
    return page_a.symmetric_difference(page_c)

# Function to update the set for Page A with new user IDs
def update_page_a(page_a, new_visitors):
    page_a.update(new_visitors)

# Function to remove a list of user IDs from the set for Page B
def remove_from_page_b(page_b, remove_visitors):
    page_b.difference_update(remove_visitors)

# Example usage for Part 3
page_a = {1, 2, 3, 4}
page_b = {3, 4, 5, 6}
page_c = {5, 6, 7, 8}

# Find users who visited both Page A and Page B
print("Users who visited both Page A and B:", users_visited_both(page_a, page_b))

# Find users who visited either Page A or Page C, but not both
print("Users who visited either Page A or C but not both:", users_visited_either(page_a, page_c))

# Update Page A with new user IDs
new_visitors = {7, 8}
update_page_a(page_a, new_visitors)
print("Updated Page A visitors:", page_a)

# Remove a list of user IDs from Page B
remove_visitors = {3, 5}
remove_from_page_b(page_b, remove_visitors)
print("Updated Page B visitors:", page_b)
