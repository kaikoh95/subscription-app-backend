import uuid
from flask import g, request
from . import create_app

app = create_app()

"""Configure global hash for all API requests."""


@app.before_request
def set_request_hash(*args, **kwargs):
    print("before request", g.__dict__)
    environ = request.environ
    print(f"""-----
    Incoming Request Payload
        {environ.get("REQUEST_METHOD")}  {environ.get("PATH_INFO")}
        Query: {environ.get("QUERY_STRING")}
        Body: {request.get_data().decode('utf-8')}
        View Function: {request.endpoint} 
        HTTP Origin: {environ.get("HTTP_HOST")}
        HTTP User Agent: {environ.get("HTTP_USER_AGENT")}
    -----""")
    g.event_hash = str(uuid.uuid4())
    print('after request', g.__dict__)
