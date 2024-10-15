# Function to filter users who rated 4 or higher
def filter_high_ratings(feedback):
    return {user_id: details['rating'] for user_id, details in feedback.items() if details['rating'] >= 4}

# Function to sort feedback by rating and return top 5 users
def top_users_by_rating(feedback):
    return dict(sorted(feedback.items(), key=lambda x: x[1]['rating'], reverse=True)[:5])

# Function to combine feedback from multiple dictionaries
def combine_feedback(*feedback_dicts):
    combined_feedback = {}
    for feedback in feedback_dicts:
        for user_id, details in feedback.items():
            if user_id in combined_feedback:
                # Update rating to the highest one and append comments
                combined_feedback[user_id]['rating'] = max(combined_feedback[user_id]['rating'], details['rating'])
                combined_feedback[user_id]['comments'] += " " + details['comments']
            else:
                combined_feedback[user_id] = details
    return combined_feedback

# Function to create a dictionary of user_id and rating for all users whose rating is greater than 3
def filter_ratings_above_3(feedback):
    return {user_id: details['rating'] for user_id, details in feedback.items() if details['rating'] > 3}

# Example usage for Part 4
feedback1 = {
    1: {'rating': 5, 'comments': 'Excellent!'},
    2: {'rating': 3, 'comments': 'Good.'},
    3: {'rating': 4, 'comments': 'Very nice!'}
}

feedback2 = {
    2: {'rating': 4, 'comments': 'Improvement needed.'},
    3: {'rating': 5, 'comments': 'Loved it!'},
    4: {'rating': 2, 'comments': 'Not great.'}
}

# Filter users who rated 4 or higher
high_ratings = filter_high_ratings(feedback1)
print("Users who rated 4 or higher:", high_ratings)

# Sort feedback by rating and return top 5 users
top_users = top_users_by_rating(feedback1)
print("Top 5 users by rating:", top_users)

# Combine feedback from multiple dictionaries
combined_feedback = combine_feedback(feedback1, feedback2)
print("Combined Feedback:", combined_feedback)

# Filter ratings above 3
ratings_above_3 = filter_ratings_above_3(combined_feedback)
print("Users with ratings above 3:", ratings_above_3)
