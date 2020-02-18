__all__ = ['fetch_rows', 'execute_one']


def fetch_rows(conn, sql_stmt, params):
    with conn.cursor() as cursor:
        cursor.execute(sql_stmt, params)
        return cursor.fetchall()


def execute_one(conn, sql_stmt, params):
    with conn.cursor() as cursor:
        cursor.execute(sql_stmt, params)
        result_id = cursor.lastrowid
        result = {
            "id": result_id
        }
        return result