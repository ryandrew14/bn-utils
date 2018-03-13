# Bottlenose Utilities

### Currently Working
- Grade Retrieval for Fundamentals II Accelerated
```
python get_grade.py [-c or --current]
```
Gets the user's current grade for the class.
```
python get_grade.py [-h or --highest]
```
Gets the user's highest possible grade for the class.
- User Management System
```
python add_user.py ref-name username password
```
Adds a user, who can then be referred to as _ref-name_ for the rest of the functions in this library.
```
python remove_user.py ref-name
```
Removes the user with the given _ref-name_.
```
python list_users.py
```
Lists the registered users.

### In Progress
- Reduce JSON representation (eliminate _ref-name_)
- Uploading a homework (upload.py)
- Shortening syntax for the commands (making a shell script that adds aliases)
