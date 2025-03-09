import os
from datetime import datetime, timedelta
from exif import Image

IMAGES_DIRECTORY = 'images'
OUTPUT_DIRECTORY = 'output'
TIMESTAMP = 'datetime_original'
TIMESTAMP_FORMAT = '%Y:%m:%d %H:%M:%S'

# Difference between desired and current timestamps
DELTA_DAYS = 791
DELTA_HOURS = 17
DELTA_MINUTES = 38
DELTA_SECONDS = 55
delta = timedelta(days=DELTA_DAYS, hours=DELTA_HOURS, minutes=DELTA_MINUTES, seconds=DELTA_SECONDS)

image_paths = [os.path.join(IMAGES_DIRECTORY, entry) for entry in os.listdir(IMAGES_DIRECTORY) if os.path.isfile(os.path.join(IMAGES_DIRECTORY, entry))]

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

for path in image_paths:
    print(path)
    with open(path, 'rb') as file:
        image = Image(file)
        original_timestamp = datetime.strptime(image.get(TIMESTAMP), TIMESTAMP_FORMAT)
        print(f'Original: {original_timestamp}')

        modified_timestamp = original_timestamp + delta
        image.datetime_original = datetime.strftime(modified_timestamp, TIMESTAMP_FORMAT)
        print(f'Modified: {image.get(TIMESTAMP)}')

        with open(f'{OUTPUT_DIRECTORY}/{os.path.basename(file.name)}', 'wb') as new_file:
            new_file.write(image.get_file())