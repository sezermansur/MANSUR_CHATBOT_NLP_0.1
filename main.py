import json
import re
import nltk
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords

# NLTK veri yolu tanımlaması ve stopwords
nltk.data.path.append('nltk_data')
stop_words = set(stopwords.words('turkish'))

# Veri dosyası adı
DATA_FILE = 'learned_responses.json'

# Veri dosyasını yükle
try:
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        learned_responses = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    learned_responses = {}

# Yanıtları kaydetme
def save_responses():
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(learned_responses, file, ensure_ascii=False, indent=4)

# Mesajı ön işleme
def preprocess_message(message):
    message = message.lower()
    message = re.sub(r'\b\w{1,2}\b', '', message)
    message = re.sub(r'\s+', ' ', message)
    message = ' '.join(word for word in message.split() if word not in stop_words)
    return message

# Mesaj benzerliğini hesaplama
def message_similarity(message1, message2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([message1, message2])
    return cosine_similarity(tfidf_matrix)[0][1]

# Tüm mesajları kontrol etme
def check_all_messages(message):
    if not learned_responses:
        return None

    highest_prob_list = {}

    for details in learned_responses.values():
        similarity_score = message_similarity(preprocess_message(' '.join(message)), preprocess_message(' '.join(details['words'])))
        response_text = details['response'] if isinstance(details['response'], str) else random.choice(details['response'])
        highest_prob_list[response_text] = similarity_score

    if not highest_prob_list:
        return None

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    if highest_prob_list[best_match] < 0.1:
        return None

    return best_match

# Kullanıcıdan geri bildirim alma ve yanıtı güncelleme
def update_response(question, old_response, new_response):
    if question in learned_responses:
        responses = learned_responses[question]['response']
        if isinstance(responses, list):
            if old_response in responses:
                responses[responses.index(old_response)] = new_response
            else:
                responses.append(new_response)
        else:
            learned_responses[question]['response'] = [responses, new_response] if responses != old_response else [new_response]
        save_responses()
        print(f"'{question}' sorusu için cevap başarıyla güncellendi.")
    else:
        print(f"'{question}' sorusu veri setinde bulunamadı.")

# Kullanıcıdan girdi alma ve yanıt üretme
while True:
    user_input = input('Sen: ')
    if user_input.lower() == 'exit':
        break
    
    preprocessed_input = preprocess_message(user_input)
    bot_response = check_all_messages(preprocessed_input.split())
    
    if bot_response:
        print('MANSUR:', bot_response)
        # Bot tarafından verilen cevabı doğrulama
        user_answer = input("Cevabım doğru mu? (E/H): ")
        if user_answer.lower() == 'e':
            # Cevap doğru ise veri setini güncelle
            if user_input not in learned_responses:
                learned_responses[user_input] = {'words': user_input.split(), 'response': [bot_response]}
            elif isinstance(learned_responses[user_input]['response'], list):
                if bot_response not in learned_responses[user_input]['response']:
                    learned_responses[user_input]['response'].append(bot_response)
            else:
                learned_responses[user_input]['response'] = [learned_responses[user_input]['response'], bot_response]
            save_responses()
        elif user_answer.lower() == 'h':
            correct_answer = input("Lütfen Doğru cevabı yazınız: ")  # Doğru cevabı tekrar iste
            update_response(user_input, bot_response, correct_answer)
        else:
            print("Lütfen sadece 'E' veya 'H' giriniz.")
    else:
        print("Ne dediğinizi anlamadım. Soruyu farklı bir şekilde sorar mısınız?")
