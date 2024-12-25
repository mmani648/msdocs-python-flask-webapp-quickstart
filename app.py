import os
from flask import Flask, request, jsonify
import io
import json
# Import document processing functions
import traceback
from DocumentScraper import DocumentParser
from DocumentClasses import Passport, Labor_Card, Residence_Visa, Emirates_ID, Home_Country_ID, Labor_Contract_Information,TouristVisa,Invoice,PurchaseOrder ,CompanyLicense,CompanyVATCertificate

app = Flask(__name__)

# Map document types to their corresponding functions
document_handlers = {

    'passport': Passport,
    'labor_card': Labor_Card,
    'residence_visa': Residence_Visa,
    'emirates_id': Emirates_ID,
    'home_country_id': Home_Country_ID,
    'labor_contract_information': Labor_Contract_Information,
    
    'tourist_visa':TouristVisa,
    'invoice':Invoice,
    'purchase_order':PurchaseOrder,
    'company_license':CompanyLicense,
    'company_vat_cert':CompanyVATCertificate,
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
        query_parameters = request.args
    
        # if 'X-API-KEY' not in headers:
        #     return jsonify({"error": "API key is missing."}), 401
        
        # if headers['X-API-KEY'] != os.environ.get('API_KEY'):
        #     return jsonify({"error": "Invalid API key."}), 401
        
        if 'document_type' not in query_parameters:
            return jsonify({"error": "document_type is missing."}), 400
        
        
        document_type = query_parameters['document_type']
        
        file = request.files.get('file')
        

        # Validate the document type
        if not document_type or document_type not in document_handlers:

            return jsonify({"error": "Invalid or unsupported document_type."}), 400

        file_content = io.BytesIO(file.read())
        
        resp= DocumentParser(file_content, file.mimetype.startswith("image"),document_type,document_handlers[document_type]).content
        print(resp)
        # Call the handler function with the appropriate arguments

        return jsonify(json.loads(resp)), 200
    except Exception as e:
        
        return traceback.format_exc(), 500
        
            
if __name__ == '__main__':
    app.run(port=5001)
