import os
from PIL import Image


def delete_file(full_file_path: str) -> None:
    os.remove(f'{full_file_path}')


def to_png(full_file_path: str) -> None:
    img = Image.open(full_file_path).convert("RGB")
    img.save(f'{full_file_path[:-5]}.png')
    delete_file(full_file_path)


def png_to_jpg(full_file_path: str) -> None:
    img = Image.open(full_file_path).convert("RGB")
    img.save(f'{full_file_path[:-4]}.jpg')
    delete_file(full_file_path)


def png_white_back(files: list[str]):
    for file in files:
        name = ''
        for i in file[::-1]:
            if i != '.':
                name += i
            else:
                break
        print(name[::-1])
        if name[::-1] not in ['jpeg', 'jpg']:
            print('opa', file, file[:-4])
            try:
                png_to_jpg(file)
            except Exception as e:
                print(e)


def webp_check(files: list[str]):
    for file in files:
        name = ''
        for i in file[::-1]:
            if i != '.':
                name += i
            else:
                break
        print(name[::-1])
        if name[::-1] not in ['png', 'jpeg', 'jpg']:
            print('opa', file, file[:-5], file[-5:])
            try:
                to_png(file)
            except Exception as e:
                print(e)


def frame(old_dir: str, new_dir: str, file_names: list[str], resizing_rate: float):
    webp_check(file_names)

    for file in file_names:
        print(file)
        try:
            img = Image.open(f"{old_dir}{file}")
        except PermissionError:
            pass
        img_w, img_h = img.size
        print(img_h / img_w)
        if 0.6 < (img_h / img_w) < 1.6:
            print(img.size, img_w, img_h, '\n')
            frame = Image.new('RGB', (int(img_w * resizing_rate), int(img_h * resizing_rate)), (255, 255, 255))
            bg_w, bg_h = frame.size
            offset = (int((bg_w - img_w) / 2), int((bg_h - img_h) / 2))
            frame.paste(img, offset)
            frame.save(f'{new_dir}resized_{file}')
            os.remove(f'{old_dir}{file}')
        else:
            print('resizing')
            print(img.size, img_w, img_h, '\n')
            if img_w > img_h:
                frame = Image.new('RGB', (int(img_w * resizing_rate), int(img_w * resizing_rate)), (255, 255, 255))
            else:
                frame = Image.new('RGB', (int(img_h * resizing_rate), int(img_h * resizing_rate)), (255, 255, 255))
            bg_w, bg_h = frame.size
            offset = (int((bg_w - img_w) / 2), int((bg_h - img_h) / 2))
            frame.paste(img, offset)
            frame.save(f'{new_dir}resized_{file}')
            os.remove(f'{new_dir}{file}')
