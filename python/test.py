# 导入所需要的库
import requests
import time,datetime


# 定义日期,默认为当前时间点,可以更换end_time_create前的#注释,#这行不执行,并修改具体时间
start_time_create = "2024-01-01 00:00:00"   #订单开始时间点,明康汇是每晚20点48分左右更新订单
#end_time_create = "2024-02-02 23:59:59"
end_time_create = datetime.datetime.now().replace(microsecond=0)

# 网站的链接
timeStrap = int(time.time())
base_url = "https://srm.mkh.cn/els/"
token_url = f"{base_url}account/login?_t={timeStrap}"
id_url = f"{base_url}reconciliation/saleReconciliationStore/list?"
token_file_path = "token.txt"

# 获取token的函数
def get_access_token():
    headers = {"Content-Type": "application/json"}
    data = {
        "elsAccount": "3171025",
        "subAccount": "1001",
        "password": "p2>Hb.nln?S;",
    }
    response = requests.post(token_url, json=data, headers=headers)
    json_data = response.json()
    if json_data["success"]:
        access_token = json_data.get("result", {}).get("token")
        with open(token_file_path, 'w') as file:
            file.write(access_token)
        return access_token
    else:
        print(f"获取token失败: {response.text}")
        return None

# 获取订单数据的函数
def fetch_order_data(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"获取数据失败: {e}")
        return None

# 处理token失效的函数
def handle_token_expired():
    print("已失效,重新获取token")
    access_token = get_access_token()
    if access_token:
        main()
    else:
        print("无法获取token")

# 保存数据的函数
def save_to_file(id_records, base_url, headers_with_token):
    order_numbers = []
    for record in id_records:
        id_value = record["id"]
        print(id_value)
        url = f"{base_url}reconciliation/saleReconciliationStore/queryById?id={id_value}"
        response = fetch_order_data(url, headers_with_token)
        if response:
            orders = response["result"].get('recAcceptReturnList', [])
            if orders:
                for item in orders:
                    order_number = item["orderNumber"]
                    order_numbers.append(order_number)
    with open('saleOrder.md', 'w') as file:
        for order_number in order_numbers:
            file.write(f'{order_number}\n')


# 主函数
def main():
    with open(token_file_path, 'r') as file:
        access_token = file.read().strip()
        print(f"token为:{access_token}")
        headers_with_token = {"Accept": "application/json, text/plain, */*",
                              "X-Access-Token": access_token}
        body = {
            #"companyCode": "9669",
            "filter": {},
            "order": "desc",
            "keyword": None,
            "name": None,
            "column": "id",
            "pageNo": 1,
            "pageSize": 100,
            "startTimeCreate": f'{start_time_create}',
            "endTimeCreate": f'{end_time_create}',
        }
        try:
            response = requests.get(id_url,json=body, headers=headers_with_token)
            json_data = response.json()
            if json_data["success"]:
                id_records = json_data.get("result", {}).get("records", [])
                save_to_file(id_records, base_url, headers_with_token)
            elif not json_data["success"]:
                handle_token_expired()
            else:
                print("获取数据失败:请检查网络")
        except requests.exceptions.RequestException as e:
            print(f'{e}')

if __name__ == "__main__":
    main()