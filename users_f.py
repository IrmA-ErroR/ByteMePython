from lists.filter_by_age import filter_by_age

social_network_users = {
    1: {
        "username": "john_doe",
        "full_name": "John Doe",
        "email": "john.doe@example.com",
        "age": 28,
        "friends": [2, 3, 4],
        "posts": [
            {"post_id": 101, "content": "Hello, world!", "likes": 10},
            {"post_id": 102, "content": "Just had a great lunch!", "likes": 5}
        ]
    },
    2: {
        "username": "jane_smith",
        "full_name": "Jane Smith",
        "email": "jane.smith@example.com",
        "age": 25,
        "friends": [1, 3],
        "posts": []
    }
}

ecommerce_users = {
    "user_001": {
        "username": "shopaholic123",
        "email": "shopaholic123@example.com",
        "purchase_history": [
            {"order_id": "A123", "item": "Laptop", "price": 1200.00, "date": "2023-01-15"},
            {"order_id": "A124", "item": "Headphones", "price": 150.00, "date": "2023-02-20"}
        ],
        "wishlist": ["Smartphone", "Smartwatch"]
    },
    "user_002": {
        "username": "fashionista",
        "email": "fashionista@example.com",
        "purchase_history": [],
        "wishlist": ["Dress", "Shoes"]
    }
}

project_management_users = {
    "emp_001": {
        "name": "Alice Johnson",
        "role": "Project Manager",
        "email": "alice.johnson@company.com",
        "projects": [
            {"project_id": "P001", "project_name": "Website Redesign", "status": "In Progress"},
            {"project_id": "P002", "project_name": "Mobile App Development", "status": "Completed"}
        ]
    },
    "emp_002": {
        "name": "Bob Brown",
        "role": "Developer",
        "email": "bob.brown@company.com",
        "projects": [
            {"project_id": "P001", "project_name": "Website Redesign", "status": "In Progress"}
        ]
    }
}


# print([(user['full_name'], user['email']) for user in social_network_users.values()])

output = [f"{i}. {user['full_name']} — {user['email']}"
          for i, user in enumerate(social_network_users.values(), start=1)]

print("\n".join(output))

friends = [user['friends'] for key, user in social_network_users.items()]
print(friends)
print(f'Всего: {sum([len(i) for i in friends])}')
unique_friends = set()
for i in friends:
    unique_friends.update(i)
print(f'Уникальные ID: {unique_friends}\n')


wishlist = []
for value in ecommerce_users.values():
    if value['purchase_history'] and value['wishlist']:
            wishlist.extend(value['wishlist'])

print(wishlist)
print()

adult_user = filter_by_age(social_network_users, 21)
for i in adult_user:
    print(i)
