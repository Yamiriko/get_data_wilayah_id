import requests

respon_provinsi = requests.get('https://wilayah.id/api/provinces.json')
if respon_provinsi.status_code == 200:
    data_provinsi = respon_provinsi.json()
    for provinsi in data_provinsi['data']:
        print(f"Provinsi: {provinsi['name']} (ID: {provinsi['code']})")
else:
    print("Gagal mengambil data provinsi.")