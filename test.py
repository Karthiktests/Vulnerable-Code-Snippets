import sqlite3

def unsafe_query(database, user_input):
    conn = sqlite3.connect(database)
    # Unsafe query construction
    query = f"SELECT * FROM users WHERE username = '{user_json['username']}'"
    return conn.execute(query)

# This function can be exploited by SQL injection due to direct inclusion of user input in the query.
