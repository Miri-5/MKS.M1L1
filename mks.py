meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "Bir şakaya karşılık cevap",
    "SHEESH": "Onaylamamak",
    "CREEPY": "Korkunç",
    "AGGRO": "Agresifleşmek/sinirlenmek"
}

word = input("Anlamadığınız bir kelime yazın: ").upper()

if word in meme_dict:
    print(meme_dict[word])
else:
    print("İstediğiniz kelime yok")
    print("Bu kelimelerden birini seçiniz: LOL, CRINGE, ROFL,  SHEESH, CREEPY, AGGRO")
