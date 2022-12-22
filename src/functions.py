def create_query_string(sql_full_path):
    with open(sql_full_path, 'r') as f_in:
        lines = f_in.read()

    return lines