import os
import re
# 成功解决了obsidian的图片引用格式只有自己看得懂的问题
def convert_image_syntax_to_custom_html(directory):
    # 正则表达式匹配Obsidian的图片格式
    obsidian_img_pattern = re.compile(r'!\[\[(.*?)\]\]')
    # 遍历指定目录和子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    contents = f.read()

                # 查找并替换所有匹配的图片格式为自定义的HTML格式
                new_contents = re.sub(obsidian_img_pattern, lambda match: convert_to_custom_html_img(match, root), contents)

                # 如果内容发生变化，则写回文件
                if new_contents != contents:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_contents)

                print(f"Converted images to custom HTML in {file_path}")

def convert_to_custom_html_img(match, root):
    # 获取文件名，并保持空格（或可选择替换）
    filename = match.group(1)
    # 使用相对路径../images/文件夹，根据需要调整
    full_path = os.path.join(root, '..', 'images', filename)
    relative_path = os.path.relpath(full_path, root).replace(os.sep, '/')
    # 创建包含居中对齐和指定宽度的HTML <img> 标签
    return f'<div align="center"><img width="550" src="{relative_path}" alt="{filename}"/></div>'

# 调用函数，指定需要转换的目录
convert_image_syntax_to_custom_html(r'C:\Users\ZhuanZ\Desktop\remoulder')
