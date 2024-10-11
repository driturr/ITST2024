# Lista över användarnamn och deras korrekta lösenord
user_credentials = {
    "user1": "Password123",
    "admin": "Admin@2023",
    "user2": "Welcome123",
    "guest": "Guest1234"
}

# En lista över vanligt använda lösenord
password_list = ["Password123", "123456", "Welcome123", "Guest1234", "password"]

# ___________
passwords_from_dict = []

# Iterate over each user in user_credentials
for username, correct_password in user_credentials.items():
    # For each user, check each password in the password list
    for password in password_list:
        # Compare the password with the correct password
        if password == correct_password:
            result = f"{username}: {password} -> success"
        else:
            result = f"{username}: {password} -> failed"
        
        # Append the result to the list
        passwords_from_dict.append(result)

# Print the results to the console
for entry in passwords_from_dict:
    print(entry)