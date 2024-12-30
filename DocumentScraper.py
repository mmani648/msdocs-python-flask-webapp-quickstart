import os
import tempfile


os.environ['OPENAI_API_KEY'] =os.environ.get('OPENAI_API_KEY')



from PIL import Image
from io import BytesIO
import base64
from openai import OpenAI
import base64
from io import BytesIO
from pdf2image import convert_from_path
Image.MAX_IMAGE_PIXELS = None

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
        print(temp_file_name)
             
        images = convert_from_path(temp_file_name, dpi=600,grayscale=True)
        # save imaeges to a disk
        try: os.remove(temp_file_name)
        except: pass
        # for i, img in enumerate(images):
        #     img.save(f"output{i}.png", "PNG")
        
        return images


def DocumentParser(file, image: bool, document_type: str,response_format):
    print(f"Document is {document_type} and promt is {document_type}.txt",response_format)
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
            {"role": "system", "content": open(f"prompts/{document_type}.txt", "r").read()},

            {"role": "user", "content": content},
        ],
    
        response_format=response_format,
        temperature=0,
    )

    message = completion.choices[0].message
    return message


