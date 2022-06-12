import os

for folder in os.listdir('input_images/dogs'):
  new_name = folder.split('-')[1]
  new_name = new_name.lower()
  os.rename(f'input_images/dogs/{folder}', f'input_images/dogs/{new_name}')
