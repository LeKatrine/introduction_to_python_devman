# from PIL import Image
# import os

# # social_networks = ["vk","inst","fb"]
# # resize_list = ((1400, 1000), (1080, 1080), (1200, 628))

# for index in range(5):
#     folder_name = f"photo_end_{index}"
#     if not os.path.isdir(folder_name):
#         os.mkdir(folder_name)
        
#     photo = Image.open(f"photo_{index}.jpg")
# #     for num in range(len(social_networks)):
# #         file_name = f"photo_{index}_{social_networks[num]}.png"
# #         png = photo.resize(resize_list[num])
# #         if social_networks[num] == "inst":
# #             png.crop((10, 0, photo.width - 10, photo.height))
# #         png.save(os.path.join(folder_name, file_name))
        
#     vk = photo.resize((1400, 1000))
#     vk.save(os.path.join(folder_name, f"photo_{index}_vk.png"))
    
#     inst = photo.resize((1080, 1080))
#     inst = inst.crop((10, 0, inst.width - 10, inst.height))
#     inst.save(os.path.join(folder_name, f"photo_{index}_inst.png"))
    
#     fb = photo.resize((1200, 628))
#     fb.save(os.path.join(folder_name, f"photo_{index}_fb.png"))

    




import os
from PIL import Image

for num in range(5):

    path = "photo"
    if not os.path.isdir(path):
        os.mkdir(path)
    
    file_path = f"photo_end_{num}"
    if not os.path.isdir(file_path):
        os.mkdir(file_path)

    img = Image.open(f'photo_{num}.jpg')

    vk = img.resize((1400, 1000))
    vk.save(f'{file_path}/vk_{num}.png', 'png')

    inst = img.resize((1080, 1080))
    inst = inst.crop((10, 0, inst.width-10, inst.height))
    inst.save(f'{path}/{file_path}/inst_{num}.png', 'png')

    fb = img.resize((1200, 628))
    fb.save(f'{path}/{file_path}/fb_{num}.png', 'png')

    print(f'Сохраненно фото: photo_end_{num}')