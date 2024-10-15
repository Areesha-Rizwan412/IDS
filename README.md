Smart Data Aggregator Assignment
Overview
The Smart Data Aggregator is a Python tool designed to manage and analyze large sets of user data efficiently. This project focuses on utilizing various data structures such as lists, tuples, sets, and dictionaries to perform a range of tasks, including user data processing, immutable data management, unique data handling, and data aggregation.

Table of Contents
Part 1: User Data Processing with Lists
Part 2: Immutable Data Management with Tuples
Part 3: Unique Data Handling with Sets
Part 4: Data Aggregation with Dictionaries
Usage
Example
Clone the Repository
Part 1: User Data Processing with Lists
In this section, user information is managed using a list of tuples. Each tuple represents user data in the format (user_id, user_name, age, country). The following tasks are performed:

Filtering: Users older than 30 from specific countries (e.g., USA, Canada) are filtered, and their names are extracted.
Sorting: The list is sorted by age to retrieve the top 10 oldest users.
Duplicate Checking: The program checks for duplicate names among the users.
Part 2: Immutable Data Management with Tuples
This section focuses on handling transaction data represented as immutable tuples in the format (transaction_id, user_id, amount, timestamp). The functions implemented include:

Unique User Count: The total number of unique users involved in transactions is calculated.
Highest Transaction: The transaction with the highest amount is identified without altering the original data.
ID Separation: The transaction IDs and user IDs are extracted into separate lists.
Validation: The function validates that each tuple contains the correct number of elements.
Part 3: Unique Data Handling with Sets
This section manages sets of unique user IDs representing visitors to different pages (A, B, and C). The functionalities include:

Visitors Intersection: Identifying users who visited both Page A and Page B.
Symmetric Difference: Finding users who visited either Page A or Page C but not both.
Updating Sets: New user IDs can be added to Page A, and specific user IDs can be removed from Page B.
Part 4: Data Aggregation with Dictionaries
This section handles user feedback stored in dictionaries, where user IDs are keys, and the values are nested dictionaries containing feedback details (i.e., rating and comments). The implemented functions include:

High Ratings Filter: Users who rated 4 or higher are filtered and stored in a new dictionary.
Top Users: The feedback is sorted by rating to return the top 5 users.
Feedback Combination: Feedback from multiple dictionaries is combined, updating ratings and appending comments for users present in more than one dictionary.
Ratings Filter: A dictionary is created for users whose ratings are greater than 3.