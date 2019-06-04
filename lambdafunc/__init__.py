import base64
import json
from functools import wraps

import boto3


def register(func):
    @wraps(func)
    def wrapper(event, context):
        args = event.get('args', [])
        kwargs = event.get('kwargs', {})
        return func(*args, **kwargs)

    return wrapper


def invoke(func_name, func_path, aws_session=boto3, *args, **kwargs):
    client = aws_session.client('lambda')
    payload = dict(command=command_path)
    if args:
        payload['args'] = args
    if kwargs:
        payload['kwargs'] = kwargs

    resp = client.invoke(
        FunctionName=func_name,
        InvocationType='RequestResponse',
        LogType='Tail',
        Payload=json.dumps(payload))

    print(base64.b64decode(resp['LogResult']).decode())

    resp = json.loads(resp['Payload'].read())
    if isinstance(resp, dict) and resp.get('errorType', None):
        raise Exception(resp.get('errorMessage'))

    return resp
