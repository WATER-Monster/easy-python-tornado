# coding:utf8
#  简易的本地文件读取，实际项目应使用数据库

def read_local(int, data):
    with open("local_data") as f:
        lines = f.readlines()
        for line in lines:
            if line.split()[int] == data:
                return line.split()
        else:
            return None


def update_local(int, data, int2, replace_data):
    with open("local_data", "r+") as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for i, line in enumerate(lines):
            if line.split()[int] == data:
                old_data = line.split()[int2]
                line = line.replace(old_data, replace_data)
                f.writelines(line)
            else:
                f.writelines(line)
