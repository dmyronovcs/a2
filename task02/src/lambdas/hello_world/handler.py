import json
from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
 
class MSG(AbstractLambda):
 
    def handle_request(self, event, context):
       
        hdr = {
            'Content-Type': 'application/json'
        }

        path = event.get('rawPath')
        http_method = event.get('requestContext', {}).get('http', {}).get('method')
 
        if path == '/hello' and http_method == 'GET':
            jtext = {
                'statusCode': 200,
                'message': 'Hello from Lambda'
            }
            return {
                'statusCode': 200,
                'headers': hdr,
                'body': json.dumps(jtext)
            }
        else:
            e_msg = f'Bad request syntax or unsupported method. Requested path: {path}, HTTP method: {http_method}'
            jtext = {
                'statusCode': 400,
                'message': e_msg
            }
            
            return {
                'statusCode': 400,
                'headers': hdr,
                'body': json.dumps(jtext)
            }
 
HANDLER = MSG()
 
def lambda_handler(event, context):
    response = HANDLER.handle_request(event, context)
    return response