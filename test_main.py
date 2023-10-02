"""
Test goes here

"""

import os
from main import connect_to_db, create_table, insert_data, read_data


def test_mian():
    # Ensure clean slate
    if os.path.exists("test.db"):
        os.remove("test.db")

    conn, cursor = connect_to_db("test.db")
    create_table(cursor)

    insert_data(cursor, "Test User", 29)
    data = read_data(cursor)
    assert data == [(1, "Test User", 29)]

    conn.close()


if __name__ == "__main__":
    test_mian()
    print("All tests passed!")
