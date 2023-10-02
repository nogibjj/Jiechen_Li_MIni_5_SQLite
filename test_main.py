"""
Test goes here

"""

import os
from main import connect_to_db, create_table, insert_data, read_data
#import pytest
from unittest.mock import patch
from main import main

def test_main_function():
    with patch('builtins.input', return_value=''):  # Mocking user input
        with patch('main.extract') as mock_extract:
            with patch('main.load') as mock_load:
                with patch('main.query') as mock_query:
                    main()
                    mock_extract.assert_called_once()
                    mock_load.assert_called_once()
                    mock_query.assert_called_once()

#if __name__ == "__main__":
    #pytest.main()

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
