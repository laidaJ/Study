import os
from PIL import Image

# 设置目标文件夹路径和缩放后的图片宽度
folder_path = "/path/to/folder/"
target_width = 800

# 遍历目标文件夹内所有图片文件  
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # 打开图片并获取原始大小
        with Image.open(os.path.join(folder_path, filename)) as img:
            original_width, original_height = img.size

            # 计算缩放比例并缩放图片
            scale_ratio = target_width / original_width
            new_width = target_width
            new_height = int(original_height * scale_ratio)
            img = img.resize((new_width, new_height), Image.ANTIALIAS)

            # 保存缩放后的图片，覆盖原文件
            img.save(os.path.join(folder_path, filename), optimize=True, quality=90)