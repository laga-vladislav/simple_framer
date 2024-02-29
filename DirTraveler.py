import os, shutil


def lvl_down(dir_path: str) -> str:
    return os.path.split(dir_path)[0]


def lvl_up(dir_path: str, up_dir: str) -> str:
    return os.path.join(dir_path, up_dir)


def get_file_list(dir_name: str) -> list[str]:
    files = os.listdir(dir_name)
    try:
        files.remove('main.lnk')
    except:
        pass
    finally:
        return files


def transfer_file(src: str, dst: str, file: str) -> None:
    try:
        origin_path: str = os.path.join(src, file)
        destination_path: str = os.path.join(dst, file)
        print(origin_path + '->' + destination_path)

        shutil.copyfile(origin_path, destination_path)
        if os.path.isfile(origin_path):
            os.remove(origin_path)
    except Exception as e:
        print(e)
