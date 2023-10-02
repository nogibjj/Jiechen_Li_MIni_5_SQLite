[![CI](https://github.com/nogibjj/Jiechen_Li_MIni_5_SQLite/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Jiechen_Li_MIni_5_SQLite/actions/workflows/cicd.yml)

## Jiechen_Li_Mini_5_SQLite

### Purpose
* To connect to a SQL database
* To perform CRUD operations
* To write at least two different SQL queries

### Lab

* Use an AI Assistant, but use a different one then you used from a previous lab (Anthropic's Claud, Bard, Copilot, CodeWhisperer, Colab AI, etc)
* ETL-Query:  [E] Extract a dataset from URL, [T] Transform, [L] Load into SQLite Database and [Q] Query
For the ETL-Query lab:
* [E] Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well.
* [T] Transform the data by cleaning, filtering, enriching, etc to get it ready for analysis.
* [L] Load the transformed data into a SQLite database table using Python's sqlite3 module.
* [Q] Write and execute SQL queries on the SQLite database to analyze and retrieve insights from the data.

## Code Location
All the relevant code in Python with SQL database can be found in ``main.py``.

For the "CRUD" with database:

### Connect
```python
def connect_to_db(db_name):
    """
    Connects to a SQLite database and returns the connection and cursor.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    return conn, cursor
```
### Create
```python
ddef create_table(cursor):
    """
    Creates a table named 'users' if it does not exist.
    """
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
    """
    )

```

### Insert
```python
def insert_data(cursor, name, age):
    """
    Inserts user data into the 'users' table.
    """
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
```

### Update
```python
def update_data(cursor, user_id, new_name):
    """
    Updates the name of a user given their user ID.
    """
    cursor.execute("UPDATE users SET name = ? WHERE id = ?", (new_name, user_id))
```

### Delete
```python
def delete_data(cursor, user_id):
    """
    Deletes a user given their user ID.
    """
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
```


All the functions are tested in the ``test_main.py`` file.


## Results

### Running ``main.py``:
<img decoding="async" src="code_result.png" width="85%">     



### Running make actions:
<img decoding="async" src="pass_actions.png" width="33%">


### Reference
Please click <a href="https://github.com/nogibjj/sqlite-lab" target="_blank">here</a> to see the template of this repo.
