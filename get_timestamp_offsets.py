import argparse
import os
from datetime import datetime

from dotenv import load_dotenv
from exif import Image

# Load environment variables
load_dotenv()
IMAGES_DIR = os.getenv('IMAGES_DIR')
TIMESTAMP = os.getenv('TIMESTAMP')
TIMESTAMP_FORMAT = os.getenv('TIMESTAMP_FORMAT').encode().decode('unicode_escape')

# Parse command line arguments
parser = argparse.ArgumentParser(description='Calculate difference between image timestamps and a given timestamp.')
parser.add_argument('desired_timestamp', help='Desired timestamp in YYYY-MM-DD HH:MM:SS format')
args = parser.parse_args()

try:
    desired_timestamp = datetime.strptime(args.desired_timestamp, '%Y-%m-%d %H:%M:%S')
except ValueError:
    raise ValueError('Desired timestamp must be in YYYY-MM-DD HH:MM:SS format')

# Get paths of images
image_paths = [os.path.join(IMAGES_DIR, entry) for entry in os.listdir(IMAGES_DIR) if os.path.isfile(os.path.join(IMAGES_DIR, entry))]

# Get timestamps of images
image_timestamps = {}
for path in image_paths:
    with open(path, 'rb') as file:
        image = Image(file)
        timestamp = datetime.strptime(image.get(TIMESTAMP), TIMESTAMP_FORMAT)
        image_timestamps[path] = timestamp

# Calculate timestamp statistics
min_timestamp = min(image_timestamps.values())
min_timestamp_delta = desired_timestamp - min_timestamp
max_timestamp = max(image_timestamps.values())
max_timestamp_delta = desired_timestamp - max_timestamp

# Print timestamp statistics
print(f'Desired timestamp: {desired_timestamp}')
print(f'Earliest timestamp: {min_timestamp}')
print(f'Latest timestamp: {max_timestamp}')
print(f'Difference between earliest and desired timestamps: {min_timestamp_delta}')
print(f'Difference between latest and desired timestamps: {max_timestamp_delta}')
