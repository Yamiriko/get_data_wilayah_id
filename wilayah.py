import requests

def main():
    try:
        # --- LANGKAH 1: PROVINSI ---
        print("\n=== DAFTAR PROVINSI ===")
        res_prov = requests.get("https://wilayah.id/api/provinces.json")
        res_prov.raise_for_status()
        data_prov = res_prov.json()

        for prov in data_prov['data']:
            print(f"[{prov['code']}] {prov['name']}")

        pilih_prov = input("\nMasukkan KODE PROVINSI: ")
        
        # Validasi apakah kode ada dalam list
        prov_obj = next((p for p in data_prov['data'] if p['code'] == pilih_prov), None)
        if not prov_obj:
            print("Kode Provinsi tidak ditemukan!")
            return

        # --- LANGKAH 2: KABUPATEN/KOTA ---
        print(f"\n=== DAFTAR KABUPATEN/KOTA DI {prov_obj['name'].upper()} ===")
        res_kab = requests.get(f"https://wilayah.id/api/regencies/{pilih_prov}.json")
        res_kab.raise_for_status()
        data_kab = res_kab.json()

        for kab in data_kab['data']:
            print(f"[{kab['code']}] {kab['name']}")

        pilih_kab = input("\nMasukkan KODE KABUPATEN/KOTA: ")
        
        kab_obj = next((k for k in data_kab['data'] if k['code'] == pilih_kab), None)
        if not kab_obj:
            print("Kode Kabupaten tidak ditemukan!")
            return

        # --- LANGKAH 3: KECAMATAN ---
        print(f"\n=== DAFTAR KECAMATAN DI {kab_obj['name'].upper()} ===")
        res_kec = requests.get(f"https://wilayah.id/api/districts/{pilih_kab}.json")
        res_kec.raise_for_status()
        data_kec = res_kec.json()

        for kec in data_kec['data']:
            print(f"[{kec['code']}] {kec['name']}")

        pilih_kec = input("\nMasukkan KODE KECAMATAN: ")

        kec_obj = next((kc for kc in data_kec['data'] if kc['code'] == pilih_kec), None)
        if not kec_obj:
            print("Kode Kecamatan tidak ditemukan!")
            return

        # --- LANGKAH 4: KELURAHAN/DESA ---
        print(f"\n=== DAFTAR KELURAHAN/DESA DI KECAMATAN {kec_obj['name'].upper()} ===")
        res_desa = requests.get(f"https://wilayah.id/api/villages/{pilih_kec}.json")
        res_desa.raise_for_status()
        data_desa = res_desa.json()

        for desa in data_desa['data']:
            print(f"[{desa['code']}] {desa['name']}")

        print("\n" + "="*40)
        print("Pencarian Selesai!")
        print("="*40)

    except requests.exceptions.RequestException as e:
        print(f"\nTerjadi kesalahan koneksi atau API: {e}")
    except Exception as e:
        print(f"\nTerjadi kesalahan sistem: {e}")

if __name__ == "__main__":
    main()