import os
import pandas as pd

# Đường dẫn tới thư mục chứa các file CSV
folder_path = "./crawl_data"

# Khởi tạo biến để lưu tổng số mẫu
total_samples = 0

# Lặp qua tất cả các file trong thư mục
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        # Đọc file CSV và đếm số mẫu
        df = pd.read_csv(file_path)
        total_samples += len(df)

print("Tổng số mẫu CSV là:", total_samples)
