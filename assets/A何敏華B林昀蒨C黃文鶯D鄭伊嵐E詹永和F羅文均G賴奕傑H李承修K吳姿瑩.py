import os
import re

# 正規表示式：數字（可能有前導0）+ 一個英文字母 + .jpg 或 .png
pattern = re.compile(r"^0*(\d+)[A-Za-z]\.(jpg|png)$", re.IGNORECASE)

def process_folder(folder_path):
    count = 0
    for root, _, files in os.walk(folder_path):
        for filename in files:
            match = pattern.match(filename)
            if match:
                number = str(int(match.group(1)))  # 去掉前導0
                new_filename = f"{number}.jpg"
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_filename)

                # 檢查是否已有同名檔案避免覆蓋
                if os.path.exists(new_path):
                    print(f"⚠️ 目標檔案已存在，略過：{new_filename}")
                    continue

                os.rename(old_path, new_path)
                print(f"✅ {filename} → {new_filename}")
                count += 1
    print(f"\n🎉 總共處理了 {count} 個檔案")

# 執行
if __name__ == "__main__":
    base_folder = os.path.dirname(os.path.abspath(__file__))
    process_folder(base_folder)
