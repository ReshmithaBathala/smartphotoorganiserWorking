import sys
import os
import exifread
from datetime import datetime
from PIL import Image
import shutil

def get_image_metadata(image_path):
    try:
        with open(image_path, 'rb') as f:
            # Read the EXIF tags
            tags = exifread.process_file(f)

            # Extract GPS coordinates if available
            gps_latitude = tags.get('GPS GPSLatitude')
            gps_longitude = tags.get('GPS GPSLongitude')
            date_time = tags.get('EXIF DateTimeOriginal')

            # Print metadata for debugging
            print(f"Processing {image_path}:")
            print(f"  GPS Latitude: {gps_latitude}")
            print(f"  GPS Longitude: {gps_longitude}")
            print(f"  Date: {date_time}")

            if gps_latitude and gps_longitude:
                lat_degrees = gps_latitude.values[0].num / gps_latitude.values[0].den
                lat_minutes = gps_latitude.values[1].num / gps_latitude.values[1].den
                lat_seconds = gps_latitude.values[2].num / gps_latitude.values[2].den
                latitude = lat_degrees + lat_minutes / 60 + lat_seconds / 3600

                lon_degrees = gps_longitude.values[0].num / gps_longitude.values[0].den
                lon_minutes = gps_longitude.values[1].num / gps_longitude.values[1].den
                lon_seconds = gps_longitude.values[2].num / gps_longitude.values[2].den
                longitude = lon_degrees + lon_minutes / 60 + lon_seconds / 3600

                gps_location = (latitude, longitude)
            else:
                gps_location = None

            date_time = tags.get('EXIF DateTimeOriginal')
            if date_time:
                date_time_str = str(date_time)
                date_obj = datetime.strptime(date_time_str, '%Y:%m:%d %H:%M:%S')
                day_date = date_obj.strftime('%Y-%m-%d')
            else:
                day_date = None

        return gps_location, day_date

    except (IOError, OSError, exifread.ExifReadError, ValueError) as e:
        print(f"Error processing {image_path}: {e}")
        return None, None

def process_files_in_directory(source_directory, destination_directory, no_metadata_directory):
    for filename in os.listdir(source_directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            file_path = os.path.join(source_directory, filename)
            gps_location, day_date = get_image_metadata(file_path)

            if day_date and gps_location:
                # Create directories based on date and location
                date_folder = os.path.join(destination_directory, day_date)
                location_folder = os.path.join(date_folder, f"{gps_location[0]}, {gps_location[1]}")

                os.makedirs(location_folder, exist_ok=True)

                # Copy the file to the location-based folder
                shutil.copy(file_path, location_folder)
            else:
                # Copy files without metadata to another directory
                no_metadata_folder = os.path.join(no_metadata_directory, "NoMetadata")
                os.makedirs(no_metadata_folder, exist_ok=True)

                shutil.copy(file_path, no_metadata_folder)

source_directory = r"Images"

destination_directory = r"Location"

no_metadata_directory = r"Location"



process_files_in_directory(source_directory, destination_directory, no_metadata_directory)
