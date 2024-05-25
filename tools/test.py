import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
import os
path = r'C:\Users\蔡昌亨\remoulder\images\"Pasted image 20240507154024.png"'  # 使用正确的用户名
if os.path.exists(path):
    print("ASD文件存在")
else:
    print("QWE文件不存在")
