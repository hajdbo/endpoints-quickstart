# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from flask import Flask
from flask import request
from createiotdevice import CreateIotDevice

app = Flask(__name__)
iotdevice = CreateIotDevice()

@app.route('/addDevice', methods=['GET'])
def createdevice():
    devstring = request.args.get('deviceString')
    if devstring is None:
      return 'No devstring code provided.', 400
    maybe = iotdevice.create_device(devstring)
    if maybe is None:
      return 'Did not create the device : %s' % devstring, 400
    return maybe, 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
