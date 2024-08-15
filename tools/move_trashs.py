import re

def remove_hyperlinks(md_file_path):
    # 正则表达式匹配Markdown超链接格式
    hyperlink_pattern = re.compile(r'\[(.*?)\]\(https?://[^\s\)]+\)')

    # 读取Markdown文件
    with open(md_file_path, 'r', encoding='utf-8') as file:
        contents = file.read()

    # 替换超链接，只保留链接文字
    new_contents = re.sub(hyperlink_pattern, r'\1', contents)

    # 写回修改后的内容到文件
    with open(md_file_path, 'w', encoding='utf-8') as file:
        file.write(new_contents)
    
    print(f"Hyperlinks removed from {md_file_path}")

# 使用示例
md_file_path = r"C:\Users\蔡昌亨\remoulder\社会思潮\2077.md"
remove_hyperlinks(md_file_path)
