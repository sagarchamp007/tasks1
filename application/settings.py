import os


def load_cred_dict(inp_path):
    credentials_dict = {}
    with open(inp_path, "r") as f:
        for line in f:
            username, password = line.strip().split(",")
            credentials_dict[username] = password

    return credentials_dict


COUNTER_INF_PATH = os.path.abspath("application/user_counter_info")
CREDENTIALS_INF_PATH = os.path.abspath("application/credentials")
CREDENTIALS_DICT = load_cred_dict(CREDENTIALS_INF_PATH)
