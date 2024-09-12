import time
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def check_for_tus():
    url = "https://sonuc.osym.gov.tr"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Kötü isteklerde hata ver
        soup = BeautifulSoup(response.text, 'html.parser')

        # Sonuçları içeren HTML kısmını bul
        table = soup.find_all('a')

        # Sonuçlar arasında 'TUS' olup olmadığını kontrol et
        for link in table:
            if "TUS" in link.text:
                print("TUS bulundu! E-posta gönderiliyor...")
                send_email_notification()
                return True
        print("TUS bulunamadı, 30 saniye sonra tekrar kontrol edilecek.")
        return False

    except requests.exceptions.RequestException as e:
        print(f"Bir hata oluştu: {e}")
        return False


def send_email_notification():
    sender_email = "gonderici-email@example.com"
    receiver_email = "alici-email@example.com"
    password = "sifreniz"

    subject = "TUS Sonuçları Açıklandı!"
    body = "TUS sonuçları ÖSYM sitesinde yayınlandı. Buradan kontrol edebilirsiniz: https://sonuc.osym.gov.tr"

    # Çok parçalı bir e-posta mesajı oluştur
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Mesajın gövdesini ekle
    message.attach(MIMEText(body, "plain"))

    try:
        # E-posta sunucusuna bağlan ve e-posta gönder
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()

        print("E-posta başarıyla gönderildi!")
    except Exception as e:
        print(f"E-posta gönderilirken bir hata oluştu: {e}")


if __name__ == "__main__":
    while True:
        if check_for_tus():
            break  # TUS bulunduysa döngüyü sonlandır
        time.sleep(30)  # 30 saniye bekle ve tekrar kontrol et