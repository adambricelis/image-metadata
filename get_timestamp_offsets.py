import os
from datetime import datetime
from exif import Image

IMAGES_DIRECTORY = 'images'
TIMESTAMP = 'datetime_original'
TIMESTAMP_FORMAT = '%Y:%m:%d %H:%M:%S'
DESIRED_TIMESTAMP = '2022:05:28 14:00:00'

image_paths = [os.path.join(IMAGES_DIRECTORY, entry) for entry in os.listdir(IMAGES_DIRECTORY) if os.path.isfile(os.path.join(IMAGES_DIRECTORY, entry))]

for path in image_paths:
    print(path)
    with open(path, 'rb') as file:
        image = Image(file)

        original_timestamp = datetime.strptime(image.get(TIMESTAMP), TIMESTAMP_FORMAT)
        print(f'Original: {original_timestamp}')

        modified_timestamp = datetime.strptime(DESIRED_TIMESTAMP, TIMESTAMP_FORMAT)
        print(f'Modified: {modified_timestamp}')

        delta = modified_timestamp - original_timestamp
        print(delta)
