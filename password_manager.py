
# # step 1 Setting up a SQLite database ------
# import sqlite3

# def set_db():
#     connection = sqlite3.connect('password_manager.db')
#     cursor = connection.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
#                         user_id TEXT PRIMARY KEY, 
#                         site_name TEXT NOT NULL,
#                         site_url TEXT,
#                         encryption_key BLOB)''')
#     connection.commit()
#     cursor.close()
#     connection.close()

# set_db()








# # step 2 argparse
# import argparse

# def parse_arguments():
#     parser = argparse.ArgumentParser(description='Password Manager CLI')
    
#     # Add arguments
#     parser.add_argument('action', choices=['add', 'get', 'delete'], help='Action to perform: add, get, or delete passwords')
#     parser.add_argument('--site', help='Site name or URL for the password entry')
#     parser.add_argument('--user-id', help='User ID or username')
#     parser.add_argument('--url', help='URL of the site (optional)')
    
#     # Add more arguments as needed
    
#     return parser.parse_args()

# def main():
#     args = parse_arguments()
    
#     # Example usage
#     if args.action == 'add':
#         if not args.site or not args.user_id:
#             print('Error: Site name and user ID are required for adding a password entry.')
#             return
#         # Implement your add password functionality here
#         print(f'Adding password for {args.user_id} on {args.site}')
#     elif args.action == 'get':
#         if not args.user_id:
#             print('Error: User ID is required for retrieving passwords.')
#             return
#         # Implement your get password functionality here
#         print(f'Retrieving passwords for {args.user_id}')
#     elif args.action == 'delete':
#         if not args.user_id:
#             print('Error: User ID is required for deleting passwords.')
#             return
#         # Implement your delete password functionality here
#         print(f'Deleting passwords for {args.user_id}')

# if __name__ == '__main__':
#     main()









# store and retreve from db---------------


# def store_encryption_key(user_id, encryption_key):
#     connection = sqlite3.connect('password_manager.db')
#     cursor = connection.cursor()
#     cursor.execute("INSERT OR REPLACE INTO passwords (user_id, encryption_key) VALUES (?, ?)",
#                    (user_id, encryption_key))
#     connection.commit()
#     connection.close()


# def retrieve_encryption_key(user_id):
#     connection = sqlite3.connect('password_manager.db')
#     cursor = connection.cursor()
#     cursor.execute("SELECT encryption_key FROM passwords WHERE user_id=?", (user_id,))
#     result = cursor.fetchone()
#     connection.close()
#     if result:
#         return result[0]
#     else:
#         return None
