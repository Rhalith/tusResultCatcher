
# TUS Result Catcher / TUS Sonuç Yakalama Uygulaması

## English

This is a Python-based application that monitors the "sonuc.osym.gov.tr" website for the release of TUS (Tıpta Uzmanlık Sınavı) results. The application automatically reloads the page every 30 seconds and sends an email notification when it detects that the TUS results have been published.

### Features
- Reloads the OSYM result page every 30 seconds.
- Checks for the text "TUS" in the latest results.
- Sends an email notification when the TUS results are found.

### Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `smtplib` (default Python library for sending emails)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/tus-result-catcher.git
   ```

2. Navigate to the project directory:

   ```bash
   cd tus-result-catcher
   ```

3. Install the required dependencies:

   ```bash
   pip install requests beautifulsoup4
   ```

### Configuration

1. Open the `main.py` file in a text editor.
2. Replace the following placeholders with your own email information:
   - `sender_email`: Your email address.
   - `receiver_email`: The email address to send the notification to.
   - `password`: Your email password or an app-specific password (if using Gmail, ensure you enable "Less Secure Apps" or generate an app password).

### Usage

1. Run the Python script:

   ```bash
   python main.py
   ```

2. The script will reload the page every 30 seconds, check for "TUS," and send an email notification when the TUS results are available.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Türkçe

Bu Python tabanlı uygulama, "sonuc.osym.gov.tr" sitesini TUS (Tıpta Uzmanlık Sınavı) sonuçlarının açıklanıp açıklanmadığını kontrol etmek için kullanılır. Uygulama sayfayı her 30 saniyede bir yeniden yükler ve TUS sonuçlarının yayınlandığını tespit ettiğinde bir e-posta bildirimi gönderir.

### Özellikler
- OSYM sonuç sayfasını her 30 saniyede bir yeniler.
- Son yayınlanan sonuçlarda "TUS" ifadesini kontrol eder.
- TUS sonuçları bulunduğunda bir e-posta bildirimi gönderir.

### Gereksinimler

- Python 3.x
- `requests` kütüphanesi
- `beautifulsoup4` kütüphanesi
- `smtplib` (Python ile birlikte gelen varsayılan e-posta gönderim kütüphanesi)

### Kurulum

1. Depoyu yerel makinenize klonlayın:

   ```bash
   git clone https://github.com/your-username/tus-result-catcher.git
   ```

2. Proje dizinine gidin:

   ```bash
   cd tus-result-catcher
   ```

3. Gerekli bağımlılıkları yükleyin:

   ```bash
   pip install requests beautifulsoup4
   ```

### Yapılandırma

1. `main.py` dosyasını bir metin düzenleyicide açın.
2. Aşağıdaki yer tutucuları kendi e-posta bilgilerinizle değiştirin:
   - `sender_email`: E-posta adresiniz.
   - `receiver_email`: Bildirimin gönderileceği e-posta adresi.
   - `password`: E-posta şifreniz veya uygulamaya özel şifre (Gmail kullanıyorsanız, "Daha Az Güvenli Uygulamalar" seçeneğini etkinleştirin ya da uygulamaya özel bir şifre oluşturun).

### Kullanım

1. Python betiğini çalıştırın:

   ```bash
   python main.py
   ```

2. Betik, sayfayı her 30 saniyede bir yeniden yükleyip "TUS" ifadesini kontrol edecek ve TUS sonuçları mevcut olduğunda bir e-posta bildirimi gönderecektir.

### Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasına bakın.
