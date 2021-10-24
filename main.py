import magic
import os.path
import zipfile
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload_docx():
    """
    Check if given file is docx or not and saves it.
    """

    # Checks if docx field is available
    if 'docx' not in request.files:
        # When no docx field is available
        _resp = jsonify({"message":"No docx file uploaded"})
        _resp.status_code = 400
    else:
        _file = request.files['docx']
        # Checks if file is actually a docx file
        if 'application/octet-stream' != magic.from_buffer(_file.read(2048),mime=True):
            # Non docx files
            _resp = jsonify({"message":"Uploaded file is not supported"})
            _resp.status_code = 400
        else:
            # Docx files
            _resp = jsonify({"message":"Docx file uploaded "+_file.filename})
            _resp.status_code = 200
            # Saving to upload/docx/
            _file_path = os.path.join('upload/docx/'+secure_filename(_file.filename))
            _file.save(_file_path)

        with open("upload/docx/1-INNER_PAGE_LAW1.docx", 'rb') as f:
            zipp = zipfile.ZipFile(f)
            xmll = zipp.read('word/document.xml')


    return _resp

@app.route("/translate", methods=['POST'])
def translate_xml():
    pass


@app.route("/translate/get", methods=['POST'])
def translate_get():
    pass

if __name__=='__main__':
    app.run()


