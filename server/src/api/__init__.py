from flask import Flask, request, make_response
import boto3

app = Flask(__name__)

class API:
    def __init__(self):
        self.app = Flask(__name__)

        # Add routes
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/users', 'get_users', self.get_users,methods=['POST'])
        self.app.add_url_rule('/posts', 'get_posts', self.get_posts)
        self.app.add_url_rule('/upload', 'new_file', self.upload_file, methods=['POST'])
        self.app.add_url_rule('/download', 'get_file', self.download, methods=['GET'])

    def index(self):
        return 'Welcome to the API!'

    def get_users(self):
        # Add logic to fetch and return users data
        return 'Users data'

    def get_posts(self):
        # Add logic to fetch and return posts data
        return 'Posts data'

    def upload_file(self):
        if 'file' not in request.files:
            return {'error': 'No file received'}, 400

        file = request.files['file']
        filepath = request.form.get('filepath')
        type = request.form.get('uploadType')

        if not file or not filepath:
            return {'error': 'Invalid file or filepath'}, 400

        if not type:
            return {'error': 'Missing upload type'}, 400

        try:
            # Save the file to LocalStack S3
            s3_client = boto3.client(
                's3',
                endpoint_url='http://localhost:4566',  # LocalStack endpoint
                region_name='us-east-1',  # Specify desired region
                aws_access_key_id='your-access-key',  # Provide your AWS access key
                aws_secret_access_key='your-secret-key'  # Provide your AWS secret key
            )

            s3_client.upload_fileobj(file, 'sb9000', filepath + '/' + file.filename)
        except Exception as e:
            return {'error': str(e)}, 500

        return {'filepath': filepath + '/' + file.filename}

    def download(self):
        filepath = request.args.get('filepath')

        if not filepath:
            return {'error': 'Missing filepath'}, 400

        try:
            # Download file from LocalStack S3
            s3_client = boto3.client(
                's3',
                endpoint_url='http://localhost:4566',  # LocalStack endpoint
                region_name='us-east-1',  # Specify desired region
                aws_access_key_id='your-access-key',  # Provide your AWS access key
                aws_secret_access_key='your-secret-key'  # Provide your AWS secret key
            )

            response = s3_client.get_object(Bucket='sb9000', Key=filepath)

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

    def run(self):
        self.app.run(port=5555)

api = API()