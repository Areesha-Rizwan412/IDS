# Function to find the total number of unique users involved in transactions
def unique_users(transactions):
    # Use a set to automatically discard duplicate user_ids
    user_ids = set([t[1] for t in transactions])
    return len(user_ids)

# Function to identify and return the transaction with the highest amount
def highest_transaction(transactions):
    # Find the transaction with the highest amount
    return max(transactions, key=lambda t: t[2])

# Function to return two separate lists: one containing all transaction_ids and the other all user_ids
def separate_ids(transactions):
    # Separate the transaction_ids and user_ids into two lists
    trans_ids = [t[0] for t in transactions]
    user_ids = [t[1] for t in transactions]
    return trans_ids, user_ids

# Function to validate tuple size and separate transaction_ids and user_ids, handling inconsistent tuples
def validate_and_separate(transactions):
    trans_ids = []
    user_ids = []
    
    for t in transactions:
        if len(t) == 4:  # Check that the tuple has exactly 4 elements (transaction_id, user_id, amount, timestamp)
            trans_ids.append(t[0])
            user_ids.append(t[1])
        else:
            print(f"Skipping invalid transaction: {t}")  # Handle inconsistent tuples by skipping them
    
    return trans_ids, user_ids

# Example usage
transactions = [
    (101, 1, 150.0, '2023-10-01'), 
    (102, 2, 200.5, '2023-10-02'), 
    (103, 1, 175.75, '2023-10-03'),
    (104, 3, 300.0, '2023-10-04'),
    (105, 2, 50.0, '2023-10-05')
]

# Find total number of unique users involved in transactions
print("Unique Users:", unique_users(transactions))

# Find the transaction with the highest amount
print("Highest Transaction:", highest_transaction(transactions))

# Separate transaction_ids and user_ids
trans_ids, user_ids = separate_ids(transactions)
print("Transaction IDs:", trans_ids)
print("User IDs:", user_ids)

# Validate and separate IDs while handling inconsistent tuples
trans_ids_valid, user_ids_valid = validate_and_separate(transactions)
print("Validated Transaction IDs:", trans_ids_valid)
print("Validated User IDs:", user_ids_valid)
