import os
import subprocess
import sys

def process_folders():
    base_dir = "data/freedo"
    script = "bilateral_normal_depth_integration.py"
    
    print(f"开始遍历目录: {base_dir}")
    
    # 检查基础目录是否存在
    if not os.path.exists(base_dir):
        print(f"错误: 目录 {base_dir} 不存在")
        return
    
    # 遍历所有子目录
    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)
        
        if os.path.isdir(folder_path):
            print(f"正在处理: {folder_path}")
            
            # 构建命令
            cmd = [
                "python", script,
                "-p", folder_path,
                "-k", "6",
                "-l", "5e-4"
            ]
            
            try:
                # 执行命令
                result = subprocess.run(cmd, check=True, capture_output=True, text=True)
                print(f"完成: {folder_path}")
                if result.stdout:
                    print(f"输出: {result.stdout}")
            except subprocess.CalledProcessError as e:
                print(f"错误: 处理 {folder_path} 时出现问题")
                print(f"错误信息: {e.stderr}")
            except FileNotFoundError:
                print(f"错误: 找不到 Python 或脚本文件")
                break
            
            print()

    print("所有文件夹处理完成!")

if __name__ == "__main__":
    process_folders()