def hitung_bmi(berat_badan, tinggi_badan):
    bmi = berat_badan / (tinggi_badan ** 2)
    return bmi

def rekomendasi_bmi(bmi):
    if bmi < 18.5:
        return "berat badan kurang"
    elif 18.5 <= bmi < 24.9:
        return "berat badan normal"
    elif 25 <= bmi < 29.9:
        return "kelebihan berat badan"
    else:
        return "obesitas"

berat_badan = float(input("masukkan berat badan (kg)  : "))
tinggi_badan = float(input("masukkan tinggi badan (m)  : ").replace(',', '.'))
bmi_hasil = hitung_bmi(berat_badan, tinggi_badan)
kategori_bmi = rekomendasi_bmi(bmi_hasil)
print("berat badan   : {} kg".format(berat_badan))
print("tinggi badan  : {} m".format(tinggi_badan))
print("nilai BMI Anda: {:.2f}".format(bmi_hasil))
print("kategori BMI  :", kategori_bmi)