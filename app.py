import os
from flask import Flask, request, jsonify, send_from_directory
import io
import json
# Import document processing functions
import traceback
from DocumentScraper import (
    passport, labor_card, residence_visa,
    emirates_id, home_country_id, labor_contract_information
)

app = Flask(__name__)

# Map document types to their corresponding functions
document_handlers = {
    'passport'                  : passport,
    'labor_card'                : labor_card,
    'residence_visa'            : residence_visa,
    'emirates_id'               : emirates_id,
    'home_country_id'           : home_country_id,
    'labor_contract_information': labor_contract_information
}


@app.route('/')
def test():
    return "All Systems are up and running"

@app.route('/DocumentScraping', methods=['POST'])
def document_scraping():

    # Parse JSON data from the request
    # access headers
    try:
        headers = request.headers
    
        if 'X-API-KEY' not in headers:
            return jsonify({"error": "API key is missing."}), 401
        
        if headers['X-API-KEY'] != os.environ.get('API_KEY'):
            return jsonify({"error": "Invalid API key."}), 401
        query_parameters = request.args
        if 'document_type' not in query_parameters:
            return jsonify({"error": "document_type is missing."}), 400
        
        document_type = query_parameters['document_type']
        
        file = request.files.get('file')
        

        # Validate the document type
        if not document_type or document_type not in document_handlers:

            return jsonify({"error": "Invalid or unsupported document_type."}), 400

        # Get the handler function for the document type
        handler_function = document_handlers[document_type]
        file_content = io.BytesIO(file.read())

        # Pass the file-like object to the handler function
        handler_function = document_handlers[document_type]
        
        resp= handler_function(file_content, file.mimetype.startswith("image")).content
        print(resp)
        # Call the handler function with the appropriate arguments

        return jsonify(json.loads(resp)), 200
    except Exception as e:
        
        return traceback.format_exc(), 500
        
            
if __name__ == '__main__':
    app.run()
