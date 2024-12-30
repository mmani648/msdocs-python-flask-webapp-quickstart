
from pydantic import BaseModel, Field
from typing import Optional, List
class Passport(BaseModel):
    """
    Pydantic class for Passport details.
    """

    # employee_code: str = Field(None, description="Employee code")
    properly_scanned: bool = Field(None, description="Whether the passport is properly scanned")

    name_on_passport: str = Field(None, description="Name of the person whose passport is it")
    gender: str = Field(None, description="Gender of the person")
    nationality: str = Field(None, description="Nationality of the person")
    date_of_birth: str = Field(None, description="Date of birth of the person in ISO 8601 format (YYYY-MM-DD)")
    passport_number: str = Field(None, description="Passport number")
    passport_issue_place: str = Field(None, description="Place of issue of the passport")
    passport_issue_date: str = Field(None, description="Date of issue of the passport in ISO 8601 format (YYYY-MM-DD)")
    passport_expiry_date: str = Field(None, description="Date of expiry of the passport in ISO 8601 format (YYYY-MM-DD)")
    address: str = Field(None, description="Address of the person")
    file_number: str = Field(None, description="File number")
    document_validity: str = Field(None, description="is the uploaded Document is valid mention reason if not valid")
    document_validity_check: bool = Field(None, description="is the uploaded Document is valid or  invalid")

class Labor_Card(BaseModel):
    """
    Pydantic class for Labor Card details.
    """

    # employee_code: str = Field(None, description="Employee code")
    properly_scanned: bool = Field(None, description="Whether the Labor Card is properly scanned")

    name_on_labor_card: str = Field(None, description="Name of the person whose labor card is it")
    expiry_date: str = Field(None, description="Date of expiry of the labor card in ISO 8601 format (YYYY-MM-DD)")
    work_permit_number: str = Field(None, description="Work permit number")
    personal_number: str = Field(None, description="Personal number")
    profession: str = Field(None, description="Profession of the person")
    nationality: str = Field(None, description="Nationality of the person")
    establishment: str = Field(None, description="Name of the establishment")
    document_validity: str = Field(None, description="is the uploaded Document is valid mention reason if not valid")
    document_validity_check: bool = Field(None, description="is the uploaded Document is valid or  invalid")    




class Residence_Visa(BaseModel):
    """
    Pydantic class for Residence Visa details.
    """

    # employee_code: str = Field(None, description="Employee code")
    properly_scanned: bool = Field(None, description="Whether the Residence Visa is properly scanned")

    name_on_visa: str = Field(None, description="Name of the person whose visa is it")
    UID_number: str = Field(None, description="UID number")
    file_number: str = Field(None, description="File number")
    profession: str = Field(None, description="Profession of the person")
    sponsor: str = Field(None, description="Sponsor of the visa")
    place_of_issue: str = Field(None, description="Place of issue of the visa")
    date_of_issue: str = Field(None, description="Date of issue of the visa in ISO 8601 format (YYYY-MM-DD)")
    date_of_expiry: str = Field(None, description="Date of expiry of the visa in ISO 8601 format (YYYY-MM-DD)")
    document_validity: str = Field(None, description="is the uploaded Document is valid mention reason if not valid")
    document_validity_check: bool = Field(None, description="is the uploaded Document is valid or  invalid")



class Emirates_ID(BaseModel):
    """
    Pydantic class for Emirates ID details.
    """

    # employee_code: str = Field(None, description="Employee code")
    properly_scanned: bool = Field(None, description="Whether the Emirates ID is properly scanned")

    name_on_emirates_id: str = Field(None, description="Name of the person whose Emirates ID is it")
    id_number: str = Field(None, description="ID number")
    date_of_birth: str = Field(None, description="Date of birth of the person in ISO 8601 format (YYYY-MM-DD)")
    date_of_issue: str = Field(None, description="Date of issue of the Emirates ID in ISO 8601 format (YYYY-MM-DD)")
    date_of_expiry: str = Field(None, description="Date of expiry of the Emirates ID in ISO 8601 format (YYYY-MM-DD)")
    document_validity: str = Field(None, description="is the uploaded Document is valid mention reason if not valid")
    document_validity_check: bool = Field(None, description="is the uploaded Document is valid or  invalid")    


class Home_Country_ID(BaseModel):
    """
    Pydantic class for Home country ID details.
    """

    properly_scanned: bool = Field(None, description="Whether the Home Country ID is properly scanned")

    name_on_id: str = Field(None, description="Name of the person whose Home Country ID is it")
    id_number: str = Field(None, description="ID number")
    date_of_birth: str = Field(None, description="Date of birth of the person in ISO 8601 format (YYYY-MM-DD)")
    gender: str = Field(None, description="Gender of the person")
    nationality: str = Field(None, description="Nationality of the person")
    address: str = Field(None, description="Address of the person")
    document_validity: str = Field(None, description="is the uploaded Document is valid mention reason if not valid")
    document_validity_check: bool = Field(None, description="is the uploaded Document is valid or  invalid")    


class Labor_Contract_Information(BaseModel):
    """
    Pydantic class for Labor Contract Information details.
    """
    properly_scanned: bool = Field(None, description="Whether the Home Labor Contract Information is properly scanned")

    transaction_number: str = Field(None, description="Transaction Number")
    contract_date: str = Field(None, description="Contract Date in ISO 8601 format (YYYY-MM-DD)")
    establishment_name: str = Field(None, description="Establishment Name")
    employee_name: str = Field(None, description="Employee Name")
    nationality: str = Field(None, description="Nationality of the Employee")
    passport_number: str = Field(None, description="Passport Number of the Employee")
    position: str = Field(None, description="Position of the Employee")
    daily_working_hours: str = Field(None, description="Daily Working Hours of the Employee")
    weekly_rest_paid_day: str = Field(None, description="Weekly Rest Paid Day")
    paid_annual_leave: str = Field(None, description="Paid Annual Leave details")
    contract_duration: str = Field(None, description="Contract Duration")
    contract_start_date: str = Field(None, description="Contract Start Date in ISO 8601 format (YYYY-MM-DD)")
    contract_end_date: str = Field(None, description="Contract End Date in ISO 8601 format (YYYY-MM-DD)")
    wage_stipulated: str = Field(None, description="Wage Stipulated")
    probation_period: str = Field(None, description="Probation Period")
    notice_period: str = Field(None, description="Notice Period")
    basic_salary: float = Field(None, description="Basic Salary of the Employee")
    house_allowance: float = Field(None, description="House Allowance provided to the Employee")
    transport_allowance: float = Field(None, description="Transport Allowance provided to the Employee")
    total_contract_salary: float = Field(None, description="Total Contract Salary")
    training_fees: str = Field(None, description="Training Fees details")
    basic_salary    = Field(None, description="Basic Salary of the Employee minus all allowances")
    food_allowance: float = Field(None, description="Food Allowance provided to the Employee")
    telephone_allowance: float = Field(None, description="Telephone Allowance provided to the Employee")
    AditonalTerms: List[str] = Field(None, description="Additional Terms all points in article (4) box all")
    document_validity: str = Field(None, description="is the uploaded Document is valid mention reason if not valid")
    document_validity_check: bool = Field(None, description="is the uploaded Document is valid or  invalid")    

class TouristVisa(BaseModel):
    """
    Pydantic class for Tourist Visa details.
    """
    visa_type : str = Field(None, description="Type of Visa")
    entry_permit_number : str = Field(None, description="Entry Permit Number remove if any space ")
    daate_of_issue : str = Field(None, description="Date of Issue of the Visa")
    place_of_issue : str = Field(None, description="Place of Issue of the Visa")
    uid_number : str = Field(None, description="UID Number")
    full_name : str = Field(None, description="Full Name of the Person")
    nationality : str = Field(None, description="National   of the Person")
    date_of_birth : str = Field(None, description="Date of Birth of the Person")
    place_of_birth : str = Field(None, description="Place of Birth of the Person")
    passport_number : str = Field(None, description="Passport Number of the Person")
    profession : str = Field(None, description="Profession of the Person")
    trip_days : str = Field(None, description="Number of Days of the Trip")
    document_validity: str = Field(None, description="is the uploaded Document is valid mention reason if not valid")
    document_validity_check: bool = Field(None, description="is the uploaded Document is valid or  invalid")    


class Items_(BaseModel):
    """Pydantic class for all Invoice items ."""
    item_description: str = Field(..., description="Description of the item")
    item_quantity: int = Field(..., description="Quantity of the item")
    item_unit_price: float = Field(..., description="Unit price of the item")
    item_total_price: float = Field(..., description="Total price for the item (Quantity × Unit Price)")
    discounts: Optional[float] = Field(None, description="Discounts applied on the item, if applicable")
    tax_details: Optional[float] = Field(None, description="Tax amount for the item, if applicable")
    shipping_or_handling_charges: Optional[float] = Field(None, description="Shipping or handling charges, if applicable")    

class Invoice(BaseModel):
    """Pydantic class for Invoice details.""" 
    # Invoice Details
    invoice_number: str = Field(..., description="Unique invoice number")
    invoice_date: str = Field(..., description="Date the invoice was issued")
    invoice_due_date: str = Field(..., description="Due date for the invoice")
    invoice_type: str = Field(..., description="Type of invoice (e.g., Tax Invoice, Proforma Invoice, Credit Note)")

    # Supplier Details
    supplier_name: str = Field(..., description="Supplier's name")
    supplier_address: str = Field(..., description="Supplier's address")
    supplier_contact_information: str = Field(..., description="Supplier's contact information (Phone, Email)")
    supplier_tax_identification_number: Optional[str] = Field(None, description="Supplier's tax identification number (e.g., VAT, GST, or TIN)")

    # Customer Details
    customer_name: str = Field(..., description="Customer's name")
    customer_address: str = Field(..., description="Customer's address")
    customer_contact_information: str = Field(..., description="Customer's contact information")
    customer_tax_identification_number: Optional[str] = Field(None, description="Customer's tax identification number, if applicable")

    # Invoice Items/Line Details
    
    items: Optional[List[Items_]] = Field(None, description="List of eligibility maximums details. get this data from Plan Summary")


    # Tax Details
    taxable_amount: float = Field(..., description="Subtotal before tax")
    tax_rate: float = Field(..., description="Tax rate (e.g., VAT/GST percentage)")
    tax_amount: float = Field(..., description="Tax amount")
    exempted_tax_details: Optional[str] = Field(None, description="Exempted tax details, if applicable")

    # Total Amounts
    subtotal_before_tax: float = Field(..., description="Total amount before tax")
    total_tax_amount: float = Field(..., description="Total tax amount")
    discounts_or_adjustments: Optional[float] = Field(None, description="Discounts or adjustments applied")
    grand_total: float = Field(..., description="Final payable amount, including tax")
    amount_in_words: Optional[str] = Field(None, description="Amount in words")
    currency: str = Field(..., description="Currency for the transaction")

    # Payment Details
    payment_terms: str = Field(..., description="Payment terms (e.g., Net 30, Net 60)")
    bank_account_details: Optional[str] = Field(None, description="Bank account details (IBAN, SWIFT code, or bank name)")
    payment_method: str = Field(..., description="Payment method (e.g., Bank Transfer, Credit Card, Cash)")
    payment_status: str = Field(..., description="Payment status (Paid, Unpaid, or Partially Paid)")

    # Other Supporting Information
    purchase_order_number: Optional[str] = Field(None, description="Purchase order number, if applicable")
    delivery_note_number: Optional[str] = Field(None, description="Delivery note number, if applicable")
    remarks_or_notes: Optional[str] = Field(None, description="Additional instructions or notes")
    company_logo: Optional[str] = Field(None, description="Company logo for validation purposes")

    document_validity: str = Field(None, description="is the uploaded Document is valid mention reason if not valid")
    document_validity_check: bool = Field(None, description="is the uploaded Document is valid or  invalid")    



class PurchaseOrder(BaseModel):
    """Pydantic class for Purchase Order details."""
    # Purchase Order Details
    purchase_order_number: str = Field(..., description="Unique identifier for the purchase order")
    purchase_order_date: str = Field(..., description="Date when the purchase order was created")
    purchase_order_expiry_date: Optional[str] = Field(None, description="Expiry or validity date of the purchase order")
    purchase_order_type: str = Field(..., description="Type of the purchase order (e.g., Standard, Blanket, Contract)")
    
    # Buyer Details
    buyer_name: str = Field(..., description="Name of the buyer (Organization or Individual)")
    buyer_address: str = Field(..., description="Physical address of the buyer")
    buyer_contact_info: str = Field(..., description="Contact information of the buyer (Phone, Email)")
    buyer_tax_id: Optional[str] = Field(None, description="Buyer’s Tax Identification Number (if applicable)")
    
    # Supplier Details
    supplier_name: str = Field(..., description="Name of the supplier")
    supplier_address: str = Field(..., description="Physical address of the supplier")
    supplier_contact_info: str = Field(..., description="Contact information of the supplier (Phone, Email any)")
    supplier_tax_id: Optional[str] = Field(None, description="Supplier’s Tax Identification Number (e.g., VAT, GST, TIN)")
    
    # Line Item Details
    item_code_sku: str = Field(..., description="Item code or SKU")
    item_description: str = Field(..., description="Description of the item")
    item_quantity_ordered: int = Field(..., description="Quantity of the item ordered")
    unit_of_measure: str = Field(..., description="Unit of measure (e.g., kg, pcs, liters)")
    item_unit_price: float = Field(..., description="Unit price of the item")
    item_total_price: float = Field(..., description="Total price of the item (Quantity × Unit Price)")
    discounts: Optional[float] = Field(None, description="Discounts (if applicable, per item or total)")
    delivery_date: Optional[str] = Field(None, description="Expected delivery date for the item")
    tax_details: Optional[str] = Field(None, description="Tax details (e.g., GST, VAT, etc.) for the item")
    
    # Total Amounts
    subtotal_before_tax: float = Field(..., description="Subtotal amount before tax")
    total_tax_amount: float = Field(..., description="Total tax amount")
    total_discounts_adjustments: Optional[float] = Field(None, description="Total discounts or adjustments (if applicable)")
    grand_total: float = Field(..., description="Grand total amount (including tax)")
    currency: str = Field(..., description="Currency for the transaction")
    
    # Payment Terms
    payment_terms: str = Field(..., description="Payment terms (e.g., Net 30, Net 60, or advance payment details)")
    payment_method: str = Field(..., description="Payment method (e.g., Bank Transfer, Credit Card, etc.)")
    
    # Shipping and Delivery Details
    delivery_address: str = Field(..., description="Shipping or delivery address")
    shipping_method: Optional[str] = Field(None, description="Shipping method (e.g., Air, Ground, Sea)")
    shipping_charges: Optional[float] = Field(None, description="Shipping charges (if applicable)")
    delivery_date_expected: Optional[str] = Field(None, description="Expected delivery date or deadline")
    
    # Other Supporting Information
    reference_numbers: Optional[str] = Field(None, description="Reference numbers (e.g., Contract Number, Quotation Number, RFQ Number)")
    remarks_or_notes: Optional[str] = Field(None, description="Additional remarks or notes (Optional)")
    buyer_signature_or_approval: Optional[str] = Field(None, description="Signature or authorized approval from the buyer")
    company_logo: Optional[str] = Field(None, description="Company logo for validation purposes")
    document_validity: str = Field(None, description="is the uploaded Document is valid mention reason if not valid")
    document_validity_check: bool = Field(None, description="is the uploaded Document is valid or  invalid")    

class Member(BaseModel):
    number: int  # Represents 'No.'
    name: str    # Represents 'Name'
    nationality: str
    role: str
    share: float  # Assuming share is a float percentage; adjust if it's a different data type

class CompanyLicense(BaseModel):
    """ Pydantic class for Company License details. """
    # License Details
    license_type: str = Field(None, description="Type of license")
    license_no: str = Field(None, description="License number")
    company_name: str = Field(None, description="Name of the company")
    business_name: str = Field(None, description="Business name of the company")
    legal_type: str = Field(None, description="Legal type of the company (e.g., LLC, Corporation, etc.)")
    issue_date: str = Field(None, description="Date the license was issued")
    expiry_date: str = Field(None, description="License expiration date")
    dnb_duns_number: str = Field(None, description="D&B D-U-N-S® number")
    main_license_no: Optional[str] = Field(None, description="Main license number, if applicable")
    register_no: Optional[str] = Field(None, description="Registration number")
    dcci_no: Optional[str] = Field(None, description="DCCI number (if applicable)")

    # License Members
    license_members: List[Member] = Field(None, description="List of license members with their details")

    # License Activities
    license_activities: Optional[List[str]] = Field(None, description="List of activities allowed by the license")

    # Address
    address: Optional[str] = Field(None, description="Company's registered address")

    # Contact Information
    phone_no: Optional[str] = Field(None, description="Company's phone number")
    fax_no: Optional[str] = Field(None, description="Company's fax number")
    mobile_no: Optional[str] = Field(None, description="Company's mobile number")
    po_box: Optional[str] = Field(None, description="Company's P.O. Box number")
    parcel_id: Optional[str] = Field(None, description="Parcel ID for the company's registered address")
    email: Optional[str] = Field(None, description="Company's email address")

    # Partners
    partners: List[dict] = Field(None, description="List of partners with their details")

    document_validity: str = Field(None, description="is the uploaded Document is valid mention reason if not valid")
    document_validity_check: bool = Field(None, description="is the uploaded Document is valid or  invalid")    

class CompanyVATCertificate(BaseModel):
    """ Pydantic class for Company VAT Certificate details. """
    # VAT Certificate Details
    vat_number: str = Field(None, description="VAT number of the company")
    registration_number: str = Field(None, description="Company's registration number")
    legal_name_arabic: str = Field(None, description="Legal name of the entity in Arabic")
    legal_name_english: str = Field(None, description="Legal name of the entity in English")
    registered_address_and_contact: str = Field(None, description="Registered address and contact number of the company")
    effective_registration_date: str = Field(None, description="The effective date of VAT registration")
    first_vat_return_period: str = Field(None, description="The first VAT return period")
    vat_return_due_date: str = Field(None, description="The due date for VAT return")
    start_and_end_dates_of_tax_periods: str = Field(None, description="Start and end dates of tax periods")
    date_of_issue: str = Field(None, description="Date of issue of VAT certificate")
    
    # Trade Licenses, Sole Establishments, and Branches Information
    # trade_licenses_details: List[dict] = Field(None, description="List of trade license details, including sole establishments and branches")
    document_validity: str = Field(None, description="is the uploaded Document is valid mention reason if not valid")
    document_validity_check: bool = Field(None, description="is the uploaded Document is valid or  invalid")    



from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal
from datetime import date

class Cheque(BaseModel):
    cheque_number: str = Field(..., description="Unique identifier for the cheque, typically printed in the top right corner")
    account_number: str = Field(..., description="The account number linked to the cheque, usually printed at the bottom")
    routing_number: str = Field(..., description="The routing number that identifies the bank branch, printed at the bottom")
    payee_name: str = Field(..., description="The person or entity to whom the cheque is payable, written on the 'Pay to the order of' line")
    amount: Decimal = Field(..., description="The amount of money in numerical form, written in figures (e.g., 100.00)")
    amount_in_words: str = Field(..., description="The amount of money written out in words (e.g., 'One Hundred Dollars and Zero Cents')")
    date: str = Field(..., description="The date the cheque was issued, typically located near the top right corner")
    bank_name: str = Field(..., description="The name of the bank that issued the cheque, often found at the top left or bottom")
    signature: Optional[str] = Field(None, description="The signature of the issuer of the cheque, usually at the bottom right")
    memo: Optional[str] = Field(None, description="A memo or note field on the cheque, where the issuer can write additional details")

   

class photo(BaseModel):
    """ Response for photograph validation. """
    status: bool = Field(..., description="Indicates if the photograph is accepted (True) or rejected (False).")
    reasons: List[str] = Field(..., description="List of reasons why the photograph was accepted or rejected.")

