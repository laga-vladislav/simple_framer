import os
from DirTraveler import lvl_down, get_file_list, transfer_file
from ImgFormater import frame


class WrongNumberException(Exception):
    pass


class App:
    def __init__(self) -> None:
        self.DV_IMG_RESIZE_PROG_DIR: str = os.getcwd().replace("\\", '/')
        self.DV_DIR: str = lvl_down(self.DV_IMG_RESIZE_PROG_DIR)
        self.OLD_IMG_DIR: str = f"{self.DV_DIR}/DATA/old_img/"
        self.NEW_IMG_DIR: str = f"{self.DV_DIR}/DATA/new_img/"
        self.RESIZING_RATE: float = 1.3

    def start(self) -> None:
        while True:
            try:
                choice = int(input('MAIN MENU\n'
                                   '1) Make a frame and move files to new_img folder\n'
                                   '2) Make a frame and leave files in olg_img folder\n'
                                   '3) Transfer files to new_img\n'
                                   '4) Exit\n'
                                   'Choose an option: '))
                files = get_file_list(self.OLD_IMG_DIR)
                if choice == 1:
                    frame(
                        self.OLD_IMG_DIR,
                        self.NEW_IMG_DIR,
                        files,
                        self.RESIZING_RATE
                    )
                    input("Done! Press enter\n")
                elif choice == 2:
                    frame(
                        self.OLD_IMG_DIR,
                        self.OLD_IMG_DIR,
                        files,
                        self.RESIZING_RATE
                    )
                    input("Done! Press enter\n")
                elif choice == 3:
                    if len(files) != 0:
                        print('There are some files...')
                        for index, file in enumerate(files):
                            print(f'{index + 1}) {file}')
                        print(f'{len(files) + 1}) Select all of them')
                        try:
                            answer = int(input("Choose an option: "))
                            if answer != len(files) + 1:
                                try:
                                    transfer_file(self.OLD_IMG_DIR, self.NEW_IMG_DIR, files[answer - 1])
                                except IndexError:
                                    raise WrongNumberException(f'Choice should be between 1 and {len(files) + 1}')
                            else:
                                for i in range(len(files)):
                                    transfer_file(self.OLD_IMG_DIR, self.NEW_IMG_DIR, files[i])
                        except ValueError:
                            raise ValueError
                        input('Done! Press enter\n')
                    else:
                        input('old_img dir is empty! Press enter\n')
                elif choice == 4:
                    print("See you again!")
                    exit(0)
                else:
                    raise WrongNumberException('Choice should be between 1 and 4')
            except ValueError:
                input("Error. Your choice is not an integer. Press enter to continue\n")
            except WrongNumberException as e:
                print(e)


if __name__ == '__main__':
    App().start()
