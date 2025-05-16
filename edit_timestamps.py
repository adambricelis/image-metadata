import argparse
import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from exif import Image

# Load environment variables
load_dotenv()
IMAGES_DIR = os.getenv('IMAGES_DIR')
OUTPUT_DIR = os.getenv('OUTPUT_DIR')
TIMESTAMP = os.getenv('TIMESTAMP')
TIMESTAMP_FORMAT = os.getenv('TIMESTAMP_FORMAT').encode().decode('unicode_escape')

# Parse command line arguments
parser = argparse.ArgumentParser(description='Change image timestamps by a given offset.')
parser.add_argument('--days', type=int, help='Number of days to offset (optional)')
parser.add_argument('--time', type=str, help='Time offset in HH:MM:SS (optional)')
args = parser.parse_args()

# Set defaults if not provided
days = args.days if args.days is not None else 0
time = args.time if args.time is not None else '00:00:00'

# Parse time offset
try:
    hours, minutes, seconds = map(int, time.split(':'))
except ValueError:
    raise ValueError('Time offset must be in HH:MM:SS format')

time_offset = timedelta(days=days, hours=hours, minutes=seconds, seconds=seconds)

# Get paths of images
image_paths = [os.path.join(IMAGES_DIR, entry) for entry in os.listdir(IMAGES_DIR) if os.path.isfile(os.path.join(IMAGES_DIR, entry))]

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Edit image timestamps
for path in image_paths:
    print(path)
    with open(path, 'rb') as file:
        image = Image(file)
        original_timestamp = datetime.strptime(image.get(TIMESTAMP), TIMESTAMP_FORMAT)
        print(f'Original: {original_timestamp}')

        modified_timestamp = original_timestamp + time_offset
        image.datetime_original = datetime.strftime(modified_timestamp, TIMESTAMP_FORMAT)
        print(f'Modified: {image.get(TIMESTAMP)}')

        with open(f'{OUTPUT_DIR}/{os.path.basename(file.name)}', 'wb') as new_file:
            new_file.write(image.get_file())
