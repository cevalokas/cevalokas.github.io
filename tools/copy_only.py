import os
import re
import shutil

def copy_images_only(source_md_dir, source_image_dir, target_image_dir):
    # 正则表达式匹配Obsidian的图片格式
    obsidian_img_pattern = re.compile(r'!\[\[(.*?)\]\]')

    # 确保目标图片目录存在
    os.makedirs(target_image_dir, exist_ok=True)

    # 遍历目录中的所有Markdown文件
    for root, dirs, files in os.walk(source_md_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    contents = f.read()

                # 查找所有匹配的图片引用
                matches = obsidian_img_pattern.findall(contents)
                for match in matches:
                    # 在源图片目录中找到图片的完整路径
                    original_image_path = os.path.join(source_image_dir, match)
                    # 在目标图片目录中构建目标图片的完整路径
                    target_image_path = os.path.join(target_image_dir, match.replace(' ', '_'))

                    # 复制图片，如果图片存在
                    if os.path.exists(original_image_path):
                        shutil.copy(original_image_path, target_image_path)
                        print(f"Copied '{original_image_path}' to '{target_image_path}'")
                    else:
                        print(f"Image not found: {original_image_path}")

# 使用示例
source_md_dir = r'./_posts'
source_image_dir = r'C:\Users\蔡昌亨\remoulder\images'
target_image_dir = r'C:\Users\蔡昌亨\Desktop\cevalokas.github.io\images'
copy_images_only(source_md_dir, source_image_dir, target_image_dir)
