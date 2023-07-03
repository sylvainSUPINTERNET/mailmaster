import multipart

def uploadEmailList( event, context ) :
    
    # const { file, fields } = await parseFormData(event);
    # const tags = { filename: file.filename };

    # multipart_headers = {'Content-Type': environ['CONTENT_TYPE']}
    # multipart_headers['Content-Length'] = environ['CONTENT_LENGTH']
    multipart.parse_form_data(event['body'], event['headers'])

    return {
        "statusCode": 200,  
        "body": "Email list uploaded"
    }