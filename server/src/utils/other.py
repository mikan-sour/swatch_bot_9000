import io

def read_file_to_stream(image_file):
    file_data = image_file.read()
    bytes = io.BytesIO(file_data)
    return bytes
