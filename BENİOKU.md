MANSUR_CHATBOT_NLP_0.1 Türkçe Sohbet Botu " Turkish Chat Bot "

Bu proje, kullanıcı girdilerine yanıt veren ve zamanla kendini geliştiren bir Türkçe sohbet botu oluşturmayı amaçlar. Bot, kullanıcının mesajlarını analiz eder, veri tabanında en uygun yanıtı arar ve kullanıcıdan geri bildirim alarak yanıtlarını günceller.
İçindekiler

    Özellikler
    Kurulum
    Kullanım
    Fonksiyonlar
    
Özellikler

    Kullanıcının mesajlarını ön işleme tabi tutar.
    TF-IDF ve kosinüs benzerliği kullanarak en uygun yanıtı seçer.
    Kullanıcı geri bildirimlerine göre yanıtlarını günceller ve geliştirir.
    Yanıtları JSON dosyasında saklayarak kalıcı hale getirir.

Kurulum

Bu projeyi çalıştırmak için aşağıdaki adımları izleyin:

    Bu depoyu klonlayın:

    bash

git clone https://github.com/sezermansur/MANSUR_CHATBOT_NLP_0.1.git

cd MANSUR_CHATBOT_NLP_0.1

Gerekli Python paketlerini yükleyin:

bash

pip install -r requirements.txt

NLTK veri dosyalarını indirin:

python

    import nltk
    nltk.download('stopwords')

Kullanım

Sohbet botunu başlatmak için aşağıdaki komutları kullanın:

    Python betiğini çalıştırın:

    bash

python main.py

Sohbet başlatın ve botun yanıtlarını görün:

text

Sen: Merhaba
MANSUR: Merhaba! Size nasıl yardımcı olabilirim?

Botun yanıtını doğrulayın veya yeni bir yanıt girin:

text

Cevabım doğru mu? (E/H): E

Yanıtı güncellemek isterseniz:

text

    Cevabım doğru mu? (E/H): H
    Lütfen Doğru cevabı yazınız: Nasılsınız?

Fonksiyonlar
save_responses()

learned_responses sözlüğünü learned_responses.json dosyasına yazar.
preprocess_message(message)

Verilen mesajı ön işler: küçük harfe çevirir, 1-2 harf uzunluğundaki kelimeleri çıkarır, fazla boşlukları tek boşluğa indirger ve durdurma kelimelerini çıkarır.
message_similarity(message1, message2)

İki mesaj arasındaki benzerliği TF-IDF vektörizer ve kosinüs benzerliği kullanarak hesaplar.
check_all_messages(message)

Verilen mesajın tüm öğrenilmiş yanıtlarla benzerliğini kontrol eder ve en yüksek benzerlik puanına sahip yanıtı döner.
update_response(question, old_response, new_response)

Verilen soruya ait eski yanıtı yeni yanıtla günceller.
