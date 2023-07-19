import io
from waitress import serve
from toolz import pipe

from flask import Flask, request, make_response, send_file, Response
from flask_cors import CORS

from ..clients.db import DBClient
from ..clients.storage import StorageS3Client
from ..services.healthcheck import HealthcheckService
from ..responses.healthcheck_response import healthcheck_response

from ..requests.upload_file import upload_file_request, UploadFileRequestError

from ..services.assets import AssetService

from ..repos.assets import  AssetRepo

from ..utils.transparify import make_white_pixels_transparent, make_below_threshold_black
from ..utils.overlay import overlay_silhouette_on_floral_print
from ..utils.cleanup import make_outside_white
from ..utils.remove_black import remove_black_pixels, overlay_images
from ..utils.other import read_file_to_stream



class API:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app, resources={r"/*": {"origins": ["http://127.0.0.1:5173", "http://localhost"]}})

        # # Init db
        # db = DBClient()
        #
        # self.storage_client = StorageS3Client()
        # self.healthcheckService = HealthcheckService(db)
        # self.asset_repo = asset_repo = AssetRepo(db)

        # Add routes
        self.app.add_url_rule('/', 'health_check', self.healthcheck_controller)
        self.app.add_url_rule('/ping', 'pong', self.ping)
        self.app.add_url_rule('/posts', 'get_posts', self.get_posts)
        self.app.add_url_rule('/upload/<upload_type>', 'new_file', self.upload_file, methods=['POST'])
        self.app.add_url_rule('/download', 'get_file', self.download, methods=['GET'])
        self.app.add_url_rule('/thing','do_thing', self.thing, methods=['POST'])

    def healthcheck_controller(self):
        mig_ver = self.healthcheckService.healthCheck()
        return healthcheck_response(mig_ver)

    def ping(self):
        return 'pong'

    def get_posts(self):
        # Add logic to fetch and return posts data
        return 'Posts data'

    def upload_file(self, upload_type):
        try:
            # Parse the request
            asset  = upload_file_request(self.asset_repo, self.storage_client, request, upload_type)

            # Save the file to storage
            asset.upload_to_s3()

            # Save the file to DB
            result = asset.store_in_database()

        except UploadFileRequestError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': str(e)}, 500

        return {'ok':True, "result": result }

    def download(self):
        filepath = request.args.get('filepath')

        if not filepath:
            return {'error': 'Missing filepath'}, 400

        try:
            # Download file from LocalStack S3
            response = self.storage_client.get_object(filepath)

            # Get the file's contents and content type
            file_contents = response['Body'].read()
            content_type = response['ContentType']

            # Create a response with the file contents and headers
            file_response = make_response(file_contents)
            file_response.headers.set('Content-Type', content_type)
            file_response.headers.set('Content-Disposition', 'attachment', filename=filepath)

            return file_response
        except Exception as e:
            return {'error': str(e)}, 500

    def thing(self):
        silhouette_image_overlay = request.files['silhouette']
        swatch_image_background = request.files['swatch']
        sil_bytes = read_file_to_stream(silhouette_image_overlay)
        swatch_bytes = read_file_to_stream(swatch_image_background)

        overlay = make_white_pixels_transparent(sil_bytes, 220)
        result = pipe(
            sil_bytes,
            make_white_pixels_transparent,
            lambda x: make_below_threshold_black(x, 219),
            lambda x: overlay_silhouette_on_floral_print(x, swatch_bytes),
            make_outside_white,
            remove_black_pixels,
            lambda x: overlay_images(x, overlay),
        )

        result_stream = io.BytesIO()
        result.save(result_stream, format='PNG')

        headers = {
            'Content-Type': 'image/jpeg'  # Adjust the content type based on your image format
        }

        # Return the image data as the response
        return Response(result_stream.getvalue(), headers=headers)

    def run(self):
        serve(self.app, host='0.0.0.0', port=8080)

api = API()