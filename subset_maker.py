import os
import sys
import shutil
import numpy as np

dataset_dir, subset_dir, subset_size = sys.argv[1], sys.argv[2], int(sys.argv[3])

images = [file for file in os.listdir(dataset_dir)]
subset = np.random.choice(images, size=subset_size, replace=False)

if not os.path.isdir(subset_dir):
  os.makedirs(subset_dir)

for image in subset:
  shutil.move(f'{dataset_dir}/{image}', f'{subset_dir}/{image}')
