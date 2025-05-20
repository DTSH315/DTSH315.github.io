import os
from collections import defaultdict

EXPECTED_NUMBERS = [str(i) + '.jpg' for i in [1,2,3,5,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,29,30,31,32]]

def find_missing_by_number(base_folder):
    missing_map = defaultdict(list)  # key = "3.jpg", value = [資料夾1, 資料夾2...]

    for root, dirs, files in os.walk(base_folder):
        if root == base_folder:
            continue  # 跳過主資料夾
        folder_name = os.path.basename(root)

        file_set = set(f.lower() for f in files)

        for filename in EXPECTED_NUMBERS:
            if filename not in file_set:
                missing_map[filename].append(folder_name)

    for filename in sorted(missing_map.keys(), key=lambda x: int(x[:-4])):
        folders = missing_map[filename]
        if folders:
            number = filename[:-4]
            print(f"{number:<2} 號尚未繳交 {len(folders)} 個：{', '.join(folders)}")

if __name__ == "__main__":
    base_folder = os.path.dirname(os.path.abspath(__file__))
    find_missing_by_number(base_folder)
