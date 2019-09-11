import sys
import json
import argparse
import datetime
import traceback

from flask import Flask, request
from flask import jsonify

from app import APP


# Start api as an app service using Flask
app = Flask(__name__)

@app.route('/')
@app.route('/api')
@app.route('/api/v1')
def default_route():
    return 'Try /api/v1/weather?place=PLACE_NAME', 400

@app.route('/api/v1/weather', methods=['GET'])
def get_weather_monthly():
    
    data = request.args.to_dict()
    
    if 'place' in data:
        return jsonify(main(data['place']))

    return 'Bad Request', 400
    

def main(place, date=None, forecast=None):
    """
    The main method takes the command line arguments and call the app.py
    to get the info of entered place

    """
    if not date:
        date = (datetime.date.today()).strftime("%b %d").upper()

    if not forecast:
        forecast = "monthly"

    obj = APP(place, date, forecast)
    
    try:
        data = obj.run()
        
        if not data:
            return {}

        return data
    except:
        return {}

if __name__ == '__main__':
    app.run(debug=True)

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
    
#     parser.add_argument('-p', '--place', type=str)
#     parser.add_argument('-d', '--date', type=str)
#     parser.add_argument('-f', '--forecast', type=str)

#     args = parser.parse_args()

#     if not args.place:
#         print("\n Need place to find the weather info.")
#         print("\n Use python3 source.py --place 'Mumbai, Maharashtra' --date '11 SEP' --forecast daily")
#         sys.exit()
    
#     try:
        
#         result = main(args.place, args.date, args.forecast)

#         if not result:
#             print("No information found.")
    
#         print(json.dumps(result, indent=4))
#     except:
#         traceback.print_exc()
#         print ()
    



