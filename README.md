# menumenu

# SPECTER-ALLIANCE PENTEST FRAMEWORK

Termux üzerinde çalışan güçlü ve modüler bir pentest framework.  
Ethical hacking ve güvenlik testleri için tasarlanmıştır.

---

## Özellikler

- Nmap ile port ve servis taraması  
- SQLMap ile SQL Injection testi  
- Slowloris DDOS testi (Yasal izinle kullanılmalı)  
- Hydra brute-force saldırısı  
- WHOIS sorgusu  
- HTTP Header analizi  
- Basit Subdomain taraması  
- Çoklu port taraması (1-1024)

---

## Kurulum (Termux)

1. Termux'u güncelle ve yükselt:

    ```bash
    pkg update && pkg upgrade -y
    ```

2. Gerekli paketleri yükle:

    ```bash
    pkg install python git wget curl openssl nmap hydra -y
    ```

3. Python kütüphanelerini yükle:

    ```bash
    pip install requests colorama whois
    ```

4. Script dosyasını klonla:

    ```bash
    git clone https://github.com/Mustafa550/menumenu.git
    cd menumenu
    ```

5. Script'i çalıştır:

    ```bash
    python specter.py
    ```

---

## Kullanım

Script açıldıktan sonra menüden istediğiniz modülü seçip hedef bilgilerini girerek testlerinizi gerçekleştirebilirsiniz.

---

## Önemli Yasal Uyarı

Bu araçlar **sadece izniniz olan sistemlerde** kullanılmalıdır.  
Yetkisiz kullanım yasa dışıdır ve cezai yaptırımlara tabidir.  
Yasalara uygun hareket ettiğinizden emin olun.

---

## Katkıda Bulunmak İsteyenler

Pull request, issue veya önerileriniz için memnuniyetle bekleriz!

---

## Lisans

MIT License

---

**By SPECTER(:AdMiN**
