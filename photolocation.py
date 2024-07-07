from PIL import Image
import exifread
import requests

def get_exif_data(image_path):
    with open(image_path, 'rb') as img_file:
        exif_data = exifread.process_file(img_file)
    return exif_data

def get_gps_info(exif_data):
    gps_info = {}
    if 'GPS GPSLatitude' in exif_data and 'GPS GPSLongitude' in exif_data:
        gps_info['latitude'] = exif_data['GPS GPSLatitude']
        gps_info['latitude_ref'] = exif_data['GPS GPSLatitudeRef']
        gps_info['longitude'] = exif_data['GPS GPSLongitude']
        gps_info['longitude_ref'] = exif_data['GPS GPSLongitudeRef']
    return gps_info

def convert_to_degrees(value):
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)
    return d + (m / 60.0) + (s / 3600.0)

def get_coordinates(gps_info):
    lat = convert_to_degrees(gps_info['latitude'])
    if gps_info['latitude_ref'].values[0] != 'N':
        lat = -lat

    lon = convert_to_degrees(gps_info['longitude'])
    if gps_info['longitude_ref'].values[0] != 'E':
        lon = -lon

    return lat, lon

def get_location(lat, lon):
    response = requests.get(f'https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}')
    return response.json()

def main(image_path):
    exif_data = get_exif_data(image_path)
    gps_info = get_gps_info(exif_data)
    if gps_info:
        lat, lon = get_coordinates(gps_info)
        location = get_location(lat, lon)
        print(f"Latitude: {lat}, Longitude: {lon}")
        print(f"Location: {location['display_name']}")
    else:
        print("No GPS information found.")

if __name__ == "__main__":
    image_path = 'path_to_your_image.jpg'  # Replace with your image path
    main(image_path)