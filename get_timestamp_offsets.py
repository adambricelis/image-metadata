import os
from datetime import datetime
from exif import Image

IMAGES_DIRECTORY = 'images'
TIMESTAMP = 'datetime_original'
TIMESTAMP_FORMAT = '%Y:%m:%d %H:%M:%S'
DESIRED_TIMESTAMP = '2022:05:28 14:00:00'

image_paths = [os.path.join(IMAGES_DIRECTORY, entry) for entry in os.listdir(IMAGES_DIRECTORY) if os.path.isfile(os.path.join(IMAGES_DIRECTORY, entry))]

image_timestamps = {}

for path in image_paths:
    with open(path, 'rb') as file:
        image = Image(file)
        timestamp = datetime.strptime(image.get(TIMESTAMP), TIMESTAMP_FORMAT)
        image_timestamps[path] = timestamp

desired_timestamp = datetime.strptime(DESIRED_TIMESTAMP, TIMESTAMP_FORMAT)
min_timestamp = min(image_timestamps.values())
min_timestamp_delta = desired_timestamp - min_timestamp
max_timestamp = max(image_timestamps.values())
max_timestamp_delta = desired_timestamp - max_timestamp

print(f'Desired timestamp: {desired_timestamp}')
print(f'Earliest timestamp: {min_timestamp}')
print(f'Latest timestamp: {max_timestamp}')
print(f'Difference between earliest and desired timestamps: {min_timestamp_delta}')
print(f'Difference between latest and desired timestamps: {max_timestamp_delta}')
