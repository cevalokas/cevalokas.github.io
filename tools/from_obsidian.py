import os
import re
import shutil

def find_and_copy_images(source_folder, image_folder, target_folder):
    # 确保目标文件夹存在
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 遍历source_folder中的所有.md文件
    for filename in os.listdir(source_folder):
        if filename.endswith(".md"):
            filepath = os.path.join(source_folder, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()

            # 查找所有的图片引用
            matches = re.findall(r'!\[\[(.*?)\]\]', content)
            modified = False

            # 创建与.md文件同名的目录在target_folder中
            doc_folder = os.path.join(target_folder, os.path.splitext(filename)[0])
            if not os.path.exists(doc_folder):
                os.makedirs(doc_folder)

            for match in matches:
                # 删除文件名中的空格
                new_match = match.replace(' ', '')
                image_path = os.path.join(image_folder, match)
                new_image_path = os.path.join(doc_folder, new_match)
                
                if os.path.exists(image_path):
                    # 复制图片到新的路径，删除空格
                    shutil.copy(image_path, new_image_path)
                    # 替换文本中的引用格式，同时删除空格
                    content = content.replace(f'![[{match}]]', f'![](/images/{os.path.join(os.path.basename(doc_folder), new_match)})')
                    modified = True

            # 如果有修改，更新.md文件
            if modified:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                print("down\n")

# 设置A，B，C文件夹的路径
source_folder = './_posts'  # Markdown文件所在文件夹
image_folder = r"C:\Users\蔡昌亨\Desktop\obsidian\__images"  # 图片所在文件夹
target_folder = './images'  # 图片要复制到的文件夹

# 调用函数
find_and_copy_images(source_folder, image_folder, target_folder)
