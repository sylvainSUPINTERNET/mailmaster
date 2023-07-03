import json
import logging
import re
logging.basicConfig(level=logging.INFO)


def is_valid_email(email):
    # Email regular expression pattern
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    return bool(re.fullmatch(email_regex, email))


# npx serverless invoke local -f sendEmail -p payload.json 
def sendEmail(event, context):

    batch_size = 1000
    data = json.loads(event['body'])

    if "emails" in data:

        emails = data["emails"]

        invalid_emails_list = []
        valid_emails_list = []

        for email in emails:
            if is_valid_email(email):
                valid_emails_list.append(email)
            else:
                invalid_emails_list.append(email)

        return {
            "statusCode": 200,
            "invalid_emails_found": invalid_emails_list
        }
    else:
        return {
            "statusCode": 400,
            "body": "No email provided"
        }
    

