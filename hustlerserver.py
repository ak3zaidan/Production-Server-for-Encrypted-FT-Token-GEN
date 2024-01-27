from flask import Flask, request
from src.RtcTokenBuilder2 import RtcTokenBuilder, Role_Publisher, time

app = Flask(__name__)

@app.route('/process_data', methods=['GET'])
def process_data():
    x = int(request.args.get('x', 0))
    y = request.args.get('y', 'default')
   
    appId = ""
    appCertificate = ""
    expirationTimeInSeconds = 3600

    channelName = y
    uid = x  # The integer uid, required for an <Vg k="VSDK" /> token

    current_timestamp = int(time.time())
    expired_ts = current_timestamp + expirationTimeInSeconds

    token = RtcTokenBuilder.build_token_with_uid(appId, appCertificate, channelName, uid, Role_Publisher, token_expire=expired_ts, privilege_expire=expired_ts)
 
    return {"token": token} # return token back


# to request
# https://hustles-3e34a4a2709c.herokuapp.com/process_data?x=0&y=DiscordCook