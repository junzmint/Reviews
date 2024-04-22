import re
import json
import requests
import pandas as pd
import threading
from datetime import datetime

def get_cmt_from_shopee_url(url):

    r = re.search(r"i\.(\d+)\.(\d+)", url)
    shop_id, item_id = r[1], r[2]
    ratings_url = "https://shopee.vn/api/v2/item/get_ratings?filter=0&flag=1&itemid={item_id}&limit=50&offset={offset}&shopid={shop_id}&type={rating}"

    # d = {"username": [], "rating": [], "comment": []}
    d = {"itemid" : [], "product_name" : [], "cmtid": [], "author_username" : [], "time": [], "comment": [], "rating": []}

    for rate in range(1, 6):
        offset = 0
        while True:
            try:
                data = requests.get(ratings_url.format(shop_id=shop_id, item_id=item_id, offset=offset, rating = rate)).json()
                
                # for key, value in data["data"]["ratings"][0].items():
                #     print(f"{key}: {value}")
                i = 1
                for i, rating in enumerate(data["data"]["ratings"], 1):
                    if(rating["comment"] == ""):
                        continue
                    else:
                        d["itemid"].append(rating["itemid"])
                        d["product_name"].append(rating["original_item_info"]["name"])
                        d["author_username"].append(rating["author_username"])
                        d["rating"].append(rating["rating_star"])
                        d["comment"].append(rating["comment"])
                        d["cmtid"].append(rating["cmtid"])
                        d["time"].append(datetime.utcfromtimestamp(rating["mtime"]).strftime('%Y-%m-%d %H:%M:%S'))

                        # print(rating["rating_star"])
                        # print(rating["comment"])
                        # print("-" * 100)

                offset += 50
            except TypeError:
                break
    return d

def read_json_product_url(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    converted_data = {}

    for category, links in data.items():
        converted_data[category] = links

    return converted_data

def log(key,value):
    print(key + " has " + str(value) + " samples")

def crawl_category(category, url_list):
    # Mở file CSV để ghi
    with open(f'./crawl_data/{category}.csv', 'a', newline='', encoding='utf-8') as csvfile:
        for index, url in enumerate(url_list):
            print(f"Processing {index+1}/{len(url_list)}")
            data = get_cmt_from_shopee_url(url)  # Giả sử hàm get_cmt_from_shopee_url trả về một list hoặc một đối tượng có thể chuyển đổi thành DataFrame
            df = pd.DataFrame(data)
            df.to_csv(csvfile, index=False, header=not index)  # Ghi dữ liệu vào file CSV, không ghi header nếu không phải lần đầu tiên ghi vào file
            log(category, df.shape[0])  # Ghi log cho mỗi lần ghi dữ liệu vào file

def main():
    print("Crawl started")
    start_time = datetime.now()

    # converted_data = read_json_product_url("./get_product_url/product_url.json")
    converted_data = read_json_product_url("./get_product_url/product_url_2.json")
    category_list = list(converted_data.keys())

    t0 = threading.Thread(target=crawl_category, args=(category_list[0],converted_data[category_list[0]]))
    t1 = threading.Thread(target=crawl_category, args=(category_list[1],converted_data[category_list[1]]))
    t2 = threading.Thread(target=crawl_category, args=(category_list[2],converted_data[category_list[2]]))
    t3 = threading.Thread(target=crawl_category, args=(category_list[3],converted_data[category_list[3]]))
    t4 = threading.Thread(target=crawl_category, args=(category_list[4],converted_data[category_list[4]]))
    t5 = threading.Thread(target=crawl_category, args=(category_list[5],converted_data[category_list[5]]))
    t6 = threading.Thread(target=crawl_category, args=(category_list[6],converted_data[category_list[6]]))
    t7 = threading.Thread(target=crawl_category, args=(category_list[7],converted_data[category_list[7]]))
    t8 = threading.Thread(target=crawl_category, args=(category_list[8],converted_data[category_list[8]]))
    t9 = threading.Thread(target=crawl_category, args=(category_list[9],converted_data[category_list[9]]))
    t10 = threading.Thread(target=crawl_category, args=(category_list[10],converted_data[category_list[10]]))
    t11 = threading.Thread(target=crawl_category, args=(category_list[11],converted_data[category_list[11]]))

    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()

    t0.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()

    end_time = datetime.now()

    processing_time = end_time - start_time

    print("Start time:", start_time)
    print("End time:", end_time)
    print("Process time:", processing_time)

    log_file_name = f"log_{start_time.strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    with open("./log/" + log_file_name, "w") as log_file:
        log_file.write(f"Start time: {start_time}\n")
        log_file.write(f"End time: {end_time}\n")
        log_file.write(f"Process time: {processing_time}\n")


if __name__ == "__main__":
    main()
