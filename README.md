# GSB Wi-Fi Otomatik Giriş

GSB Wi-Fi giriş sayfasına (`https://wifi.gsb.gov.tr/`) Selenium ile otomatik giriş yapar.
Sayfa internet gelmeden önce açıldığı için script, **internetsiz** çalışacak şekilde yerel `chromedriver` kullanır.

## Gereksinimler

- Windows
- [Python](https://www.python.org/downloads/) (kurulumda **"Add Python to PATH"** kutusunu işaretle)
- Google Chrome

Python kurulu mu kontrol et:

```
python --version
```

## Kurulum

### 1) Projeyi indir

```
git clone https://github.com/muammerbyrm/GSBWifi-Auto.git
cd GSBWifi-Auto
```

### 2) Sanal ortam oluştur ve aç

```
python -m venv venv
venv\Scripts\activate
```

PowerShell "betik çalıştırma devre dışı" hatası verirse:

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\activate
```

Satırın başında `(venv)` görünmeli. (Klasik CMD kullanırsan bu sorun çıkmaz.)

### 3) Bağımlılıkları kur

```
pip install -r requirements.txt
```

> Bu adım internet ister. Wi-Fi'ye girmeden önce, internet varken bir kez yapman yeterli.

### 4) chromedriver'ı indir

1. Chrome sürümünü öğren: Chrome'da `chrome://version` adresine git.
2. Aynı ana sürümün **chromedriver (win64)** dosyasını Google'ın [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/) sayfasından indir.
3. Zip'ten çıkan `chromedriver.exe` dosyasını proje içindeki `drivers` klasörüne koy:

```
mkdir drivers
move %USERPROFILE%\Downloads\chromedriver-win64\chromedriver.exe drivers\
```

`chromedriver.exe` doğrudan `drivers` klasörünün içinde olmalı:

```
drivers\chromedriver.exe
```

Kontrol:

```
drivers\chromedriver.exe --version
```

### 5) `.env` dosyasını oluştur

```
copy .env.example .env
notepad .env
```

Açılan dosyaya bilgilerini yaz ve kaydet:

```
GSB_USERNAME=TC_KIMLIK_NO
GSB_PASSWORD=SIFRE
```

İsteğe bağlı: chromedriver başka bir yerdeyse yolunu ekleyebilirsin:

```
CHROMEDRIVER_PATH=C:/Drivers/chromedriver-win64/chromedriver.exe
```

> `.env` dosyası `.gitignore` ile GitHub'a gönderilmez. Bilgilerini kimseyle paylaşma.

## Çalıştırma

Wi-Fi'ye bağlıyken ama giriş yapılmamış durumdayken:

```
python gsb_wifi_login.py
```

Chrome açılır, giriş yapılır ve script Enter bekler. Enter'a basınca tarayıcı kapanır.

## Sorun Giderme

| Sorun | Çözüm |
|---|---|
| "Chrome başlatılıyor..." satırında takılıyor | `drivers\chromedriver.exe` yolunu kontrol et. "Yerel chromedriver bulunamadı" yazıyorsa dosya yanlış yerde demektir. |
| Sürüm uyuşmazlığı hatası | Chrome ve chromedriver ana sürümleri aynı olmalı. Chrome güncellendiyse sürücüyü yeniden indir. |
| Eski işlemler takılı kaldı | `taskkill /F /IM chromedriver.exe` ve `taskkill /F /IM chrome.exe` |
| chromedriver çalışmıyor | Antivirüs engelliyor olabilir. Dosyaya sağ tıklayıp Özellikler'de "Engellemeyi kaldır" kutusunu işaretle. |
| `venv\Scripts\activate` hata veriyor | 2. adımdaki `Set-ExecutionPolicy` komutunu çalıştır ya da CMD kullan. |

## Dosya Yapısı

```
proje/
├── gsb_wifi_login.py
├── drivers/
│   └── chromedriver.exe
├── .env              (sen oluşturursun, GitHub'a gitmez)
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```
