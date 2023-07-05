# import multipart

# https://www.serverless.com/blog/handling-aws-lambda-python-dependencies

from cgi import parse_header, parse_multipart
from io import BytesIO, StringIO
import base64
import csv

def uploadEmail(event, context):
    
    print(event)
    
    c_type, c_data = parse_header(event['headers']['content-type'])
    # Manually encode 'boundary' to bytes if it's present
    if 'boundary' in c_data:
        c_data['boundary'] = c_data['boundary'].encode()

    decoded_string = base64.b64decode(event['body'])
    form_data = parse_multipart(BytesIO(decoded_string), c_data)
    
    
    for file_name in form_data.keys():
        file_data = form_data[file_name][0]
        file_like_object = StringIO(file_data.decode())
        csv_reader = csv.reader(file_like_object)
         
        # reading CSV content
        for row in csv_reader:
            print(row)
            
        print("===============")
        
    # print(form_data)

    return {
        "statusCode": 200,  
        "body": "Email list uploaded"
    }