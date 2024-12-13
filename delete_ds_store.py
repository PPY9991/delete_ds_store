import os

def delete_ds_store_files(directory):
    """递归删除指定目录及其子目录中的 .DS_Store 文件"""
    deleted_count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == ".DS_Store":
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    deleted_count += 1
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")
    print(f"\nTotal .DS_Store files deleted: {deleted_count}")

if __name__ == "__main__":
    # 指定需要清理的目录（修改为实际的路径）
    target_directory = input("Enter the directory to clean: ").strip()
    if os.path.isdir(target_directory):
        delete_ds_store_files(target_directory)
    else:
        print("Invalid directory. Please check the path and try again.")