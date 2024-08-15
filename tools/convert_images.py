import os
import re
import shutil

def convert_images_and_copy(source_md_dir, source_image_dir, target_image_dir):
    # 正则表达式匹配Obsidian的图片格式
    obsidian_img_pattern = re.compile(r'!\[\[(.*?)\]\]')

    # 确保目标图片目录存在
    os.makedirs(target_image_dir, exist_ok=True)

    # 遍历目录A中的所有Markdown文件
    for root, dirs, files in os.walk(source_md_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    contents = f.read()

                # 使用闭包函数处理匹配到的内容
                def replace_and_copy(match):
                    original_filename = match.group(1)
                    # 构建在目录B中的原始图片完整路径
                    original_image_path = os.path.join(source_image_dir, original_filename)
                    # 在目录C中构建目标图片的完整路径
                    target_image_path = os.path.join(target_image_dir, original_filename.replace(' ', '_'))
                    
                    # 复制图片，如果图片存在
                    if os.path.exists(original_image_path):
                        shutil.copy(original_image_path, target_image_path)
                        # 更新相对路径用于HTML标签
                        relative_path = os.path.relpath(target_image_path, os.path.dirname(file_path)).replace(os.sep, '/')
                        return f'<div align="center"><img width="550" src="{relative_path}" alt="{original_filename}"/></div>'
                    else:
                        # 如果文件不存在，保留原始格式
                        return match.group(0)

                new_contents = re.sub(obsidian_img_pattern, replace_and_copy, contents)

                # 如果内容发生变化，则写回文件
                if new_contents != contents:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_contents)

                print(f"Processed {file_path}")

# 使用示例
source_md_dir = r'./_posts'
source_image_dir = r'C:\Users\蔡昌亨\remoulder\images'
target_image_dir = r'C:\Users\蔡昌亨\Desktop\cevalokas.github.io\images'
convert_images_and_copy(source_md_dir, source_image_dir, target_image_dir)
