import urllib.request
import json
import re
import csv
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'

# 找出第一個圖片網址的 function
def findFirstPictureUrl(url):
  pattern = r'https?://[^ \n]+?\.(?:jpg|jpeg|png|gif|JPG|JPEG|PNG|GIF)'
  match = re.search(pattern, url)

  # 判斷是否有找出符合規則的結果，並取得截取的圖片網址
  if match:
    image_url = match.group(0)
    return image_url
  else:
    # 沒有找到符合規則的結果，回傳預設圖片 (貓咪圖)
    print('沒有找到符合的圖片，回傳預設圖片')
    return 'https://plus.unsplash.com/premium_photo-1675616553658-259d91ec4a16?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=987&q=80'

# 找出區域資訊的 function
def findDistrict(text):
  parts = text.split()
  district = parts[1]
  district = district[:3]
  return district

# 抓取資料時用 try except 包起來，避免程式出錯，並印出錯誤訊息
try:
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')
        json_data = json.loads(data)
        
        # 取得景點列表
        attractions = json_data['result']['results']

    # 開啟 CSV 檔案 attraction.csv
    with open('attraction.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
            
        # 使用 dictionary 來建立 MRT 到景點名稱的對應關係
        mrt_dict = {}

        # 使用迴圈取得每個景點資料
        for attraction in attractions:
            stitle = attraction['stitle']
            address = findDistrict(attraction['address'])
            longitude = attraction['longitude']
            latitude  = attraction['latitude']
            img = findFirstPictureUrl(attraction['file'])
            
            MRT = attraction['MRT']

            # attraction.csv 寫入資料
            writer.writerow([stitle, address, longitude, latitude, img])

            # 將景點名稱加入對應的 MRT 清單，若 MRT 不存在則建立新的清單，並加入景點名稱
            if MRT in mrt_dict:
                mrt_dict[MRT].append(stitle)
            else:
                mrt_dict[MRT] = [stitle]
                    
        print('景點資料已成功儲存至 attraction.csv')

    with open('mrt.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

      # 使用迴圈將每個 MRT 及對應的景點名稱寫入 mrt.csv
        for mrt, attractions in mrt_dict.items():
            writer.writerow([mrt] + attractions)
   
        print('由捷運站分類的周邊景點資料已成功儲存至 mrt.csv')

# 若無法取得資料，印出錯誤訊息            
except urllib.error.URLError as e:
    print('無法取得資料:', e)