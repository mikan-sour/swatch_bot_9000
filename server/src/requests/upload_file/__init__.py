from ...models.asset import Asset

class UploadFileRequestError(Exception):
    pass

def upload_file_request(repo, storage_client, request, upload_type):
    if 'file' not in request.files:
        raise UploadFileRequestError('No file received')

    file = request.files['file']
    file_path = request.form.get('filepath')
    asset_name = request.form.get('asset_name')

    if not (upload_type == 'silhouette' or upload_type == 'swatch'):
        raise UploadFileRequestError(f'received upload_type {upload_type} but need `silhouette` or `swatch`')

    if not (file and file_path and upload_type and asset_name):
        raise UploadFileRequestError('Invalid file or file_path or upload_type or asset_name')

    return Asset(repo=repo, storage_client=storage_client, upload_type=upload_type,asset_name=asset_name, file_path=file_path, file=file)


