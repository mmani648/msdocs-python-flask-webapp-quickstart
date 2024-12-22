import os
import tempfile


os.environ['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY')

import fitz
from PIL import Image
from io import BytesIO
import base64
from openai import OpenAI
from pydantic import BaseModel, Field
import base64
from io import BytesIO
from pdf2image import convert_from_path



client = OpenAI()

def encode_image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str





def pdf_to_images(binary_data):
    
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(binary_data.getvalue())
        temp_file_name = temp_file.name
        images = convert_from_path(temp_file_name, dpi=1200)
        print(type(images[0]))
        return images





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


def passport(file, image: bool):
    content = []
    if image:
        img = Image.open(file)

        base64_image = encode_image_to_base64(img)
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
        })
    else:
        images = pdf_to_images(file)

        for img in images:
            base64_image = encode_image_to_base64(img)
            content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            })


    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "You are a helpful assistant tasked with validating the quality of input passport images (front and back in case both are available otherwise just front). Your primary objective is to ensure these images are properly scanned, meaning they should not be captured by a mobile phone or any similar device in short it should be good enough for any governmental procedures. Once validation is complete, your next task is to extract the specified details from these images and return them in a defined format."},

            {"role": "user", "content": content},
        ],
    
        response_format=Passport,
    )

    message = completion.choices[0].message
    return message




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

#File can be either PDF or image
#PDF must be passed as bytes
def labor_card(file, image: bool):
    content = []

    if image:
        img = Image.open(file)

        base64_image = encode_image_to_base64(img)
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
        })
    else:
        images = pdf_to_images(file)

        for img in images:
            base64_image = encode_image_to_base64(img)
            content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            })

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": open("labourcard.txt", "r").read()},

            {"role": "user", "content": content},
        ],
        response_format=Labor_Card,
        temperature=0
    )

    message = completion.choices[0].message
    return message




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


#File can be either PDF or image
#PDF must be passed as bytes
def residence_visa(file, image: bool):
    content = []

    if image:
        img = Image.open(file)

        base64_image = encode_image_to_base64(img)
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
        })
    else:
        images = pdf_to_images(file)

        for img in images:
            base64_image = encode_image_to_base64(img)
            content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            })

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "You are a helpful assistant tasked with validating the quality of input Residence Visa images (front and back in case both are available otherwise just front). Your primary objective is to ensure these images are properly scanned, meaning they should not be captured by a mobile phone or any similar device in short it should be good enough for any governmental procedures. Once validation is complete, your next task is to extract the specified details from these images and return them in a defined format."},

            {"role": "user", "content": content},
        ],
        response_format=Residence_Visa,
    )

    message = completion.choices[0].message
    return message


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
    



#File can be either PDF or image
#PDF must be passed as bytes
def emirates_id(file, image: bool):
    content = []

    if image:
        img = Image.open(file)

        base64_image = encode_image_to_base64(img)
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
        })
    else:
        images = pdf_to_images(file)

        for img in images:
            base64_image = encode_image_to_base64(img)
            content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            })

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "You are a helpful assistant tasked with validating the quality of input Emirates ID images (front and back in case both are available otherwise just front). Your primary objective is to ensure these images are properly scanned, meaning they should not be captured by a mobile phone or any similar device in short it should be good enough for any governmental procedures. Once validation is complete, your next task is to extract the specified details from these images and return them in a defined format."},

            {"role": "user", "content": content},
        ],
        response_format=Emirates_ID,
    )

    message = completion.choices[0].message
    return message



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


#File can be either PDF or image
#PDF must be passed as bytes
def home_country_id(file, image: bool):
    content = []

    if image:
        img = Image.open(file)

        base64_image = encode_image_to_base64(img)
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
        })
    else:
        images = pdf_to_images(file)

        for img in images:
            base64_image = encode_image_to_base64(img)
            content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            })

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "You are a helpful assistant tasked with validating the quality of input Home Country ID images (front and back in case both are available otherwise just front). Your primary objective is to ensure these images are properly scanned, meaning they should not be captured by a mobile phone or any similar device in short it should be good enough for any governmental procedures. Once validation is complete, your next task is to extract the specified details from these images and return them in a defined format."},

            {"role": "user", "content": content},
        ],
        response_format=Home_Country_ID,
    )

    message = completion.choices[0].message
    return message




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



#File can be either PDF or image
#PDF must be passed as bytes
def labor_contract_information(file, image: bool):
    content = []

    if image:
        img = Image.open(file)
        # save image to disk 
      
        base64_image = encode_image_to_base64(img)
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
        })
    else:
        images = pdf_to_images(file)

        for img in images:
            base64_image = encode_image_to_base64(img)
    
            content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            })
    # save image to disk

        
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "You are a helpful assistant tasked with validating the quality of input Home Labor Contract Information images (front and back in case both are available otherwise just front). Your primary objective is to ensure these images are properly scanned, meaning they should not be captured by a mobile phone or any similar device in short it should be good enough for any governmental procedures. Once validation is complete, your next task is to extract the specified details from these images and return them in a defined format."},

            {"role": "user", "content": content},
        ],
        response_format=Labor_Contract_Information,
        temperature=0
    )

    message = completion.choices[0].message
    return message

