# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
import sendgrid
import os
from flask import Flask
from sendgrid.helpers.mail import *


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/hello')
def hello():
    SENDGRID_API_KEY='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'
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    from_email = Email('githubtr@gmail.com')
    to_email = To('terrance.raphael@gmail.com')
    subject = 'Hello from Python'
    content = Content("text/plain","Hello from Python Body")
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print('response status:',response.status_code) # 202 status means successful in sending a mail
    print('response header:',response.headers) # gives some other info
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python38_app]