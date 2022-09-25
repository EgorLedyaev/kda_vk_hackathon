![](https://github.com/EgorLedyaev/kda_vk_hackathon/blob/main/backend/storage/public/logo.svg)


<a href="https://drive.google.com/file/d/1bb4uoVznEImTt7DJehBVLVycWIaOocb_/view?usp=sharing" target="_blank"><img src="https://github.com/EgorLedyaev/kda_vk_hackathon/blob/main/backend/storage/public/qr_cast.png" width="200" height="200" border="10" alt="QR Screencast"/></a>     <a href="https://cloud.mail.ru/public/1tEm/rFZSUKjEu" target="_blank"><img src="https://github.com/EgorLedyaev/kda_vk_hackathon/blob/main/backend/storage/public/qr_pdf.png" width="200" height="200" alt="QR PDF">
# Пример использования:

Скачиваем репозиторий

```
git clone https://github.com/EgorLedyaev/kda_vk_hackathon.git
cd kda_vk_hackathon
```

Устаналиваем зависимости

```
pip install -r requirements.txt
```

Обучаем модель и сохраняем ее в файл baseline.model

```
python main.py --action=train --path_to_dataset="" --path_to_model="baseline.model"
```

Оцениваем ROC-AUC на тестовом подмножестве пользователей

```
python main.py --action=evaluate --path_to_dataset="" --path_to_model="baseline.model"
```

Получаем прогнозы для пользователей 1000100,1000121

```
python main.py --action=predict --path_to_dataset="" --path_to_model="baseline.model" --idx=1000100,1000121
```


# Требования & Зависимости Backend:

Чтобы использовать решение kda_vk_hackathon, вам понадобятся:

## Зависимости

* Python 3.7+
* Latest version of OpenSSL
* Pip3

```
sudo apt-get install python3.7-dev python3-pip libssl-dev build-essential python3-venv
```
## Активация виртуальной среды (необязательно)
```
python -m venv venv
source venv/bin/activate
```
## Скачать Masonite
```
pip install masonite-orm
pip install masonite
```
## После установки вы можете запустить сервер:
```
python craft serve
```
