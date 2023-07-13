from PIL import Image
import os

# import numpy as np

# list [ position , value]

#   (208,206,206)-- dark grey
#   (240, 240, 240) -- light grey
#   x -- 1130px

# ------------------------

file_path = 'D:\\pythonCode\\UdemyPython\\MyCodePython\\Section_11\\crop_img\\tests_Images'
#st = 'D:\\pythonCode\\UdemyPython\\MyCodePython\\Section_11\\crop_img\\tests_Images\\test_pdj.png'
pos_lis = []

check = False
crop_width_check = True
crop_width = 0
with Image.open(file_path, mode='r') as im:
    # for y in range()
    test = []
    for i in range(0, im.height - 1):
        if im.getpixel((im.width // 2, i)) in [(208, 206, 206)]:
            test.append(i)

            check = True

        if check and im.getpixel((im.width // 2, i)) in [(240, 240, 240)]:
            test.append(i)
            pos_lis.append(test)

            test = []
            check = False
        for u in range(0, im.width - 1):
            if crop_width_check and im.getpixel((u, i)) in [(242, 248, 250)]:
                crop_width = u
                crop_width_check = False
                print(u)
                break

# left -- 0
# right -- 1316
print(pos_lis)
if len(pos_lis[0]) == 2:
    pos_lis[0].append(0)
    pos_lis[0].sort()
if 0 not in pos_lis[0]:
    for i in range(0, im.height - 1):
        if im.getpixel((im.width // 2, i)) in [(240, 240, 240)]:
            pos_lis.append([0, 0, i])
            pos_lis.sort()
            break

no = 0
print(pos_lis)
for i in os.listdir(file_path):

    with Image.open(file_path + '\\' + i) as im:
        new_folder = f'{os.path.basename(file_path)}' + 'Folder'
        path = 'D:\\pythonCode\\UdemyPython\\MyCodePython\\Section_11\\crop_img'
        os.chdir(path)

        os.makedirs(new_folder)
        for x, y, z in pos_lis:
            no += 1
            im1 = im.crop((0, y, crop_width, z))
            im1.save(f'D:\\pythonCode\\UdemyPython\\MyCodePython\\Section_11\\crop_img\\{new_folder}\\Q{no}.png')
            # im1.show()

# print(u)
