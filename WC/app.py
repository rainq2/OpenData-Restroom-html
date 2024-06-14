import csv
import math
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

def calculate_distance(lat1, lon1, lat2, lon2):
    # 將經度和緯度轉換為弧度
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine 公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    radius = 6371  # 地球半徑（公里）
    distance = radius * c

    return distance

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nearby_toilets', methods=['POST'])
def nearby_toilets():
    user_latitude = request.json['latitude']
    user_longitude = request.json['longitude']

    # 讀取 CSV 檔案，並將廁所資訊加入到 nearby_toilets 中
    nearby_toilets = []
    with open('re.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            toilet_latitude = float(row['latitude'])
            toilet_longitude = float(row['longitude'])
            distance = calculate_distance(user_latitude, user_longitude, toilet_latitude, toilet_longitude)
            # 如果廁所距離使用者小於5公里，則加入到附近的廁所列表中
            if distance <= 5:
                toilet = {
                    'name': row['name'],
                    'address': row['address'],
                    'latitude': toilet_latitude,
                    'longitude': toilet_longitude,
                    'type': row['type'],  
                    'type2': row['type2'],  
                    'grade': row['grade'],  
                    'administration': row['administration']
                }
                nearby_toilets.append(toilet)

    return jsonify(nearby_toilets)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5269, debug=True)

