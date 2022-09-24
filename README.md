![](https://github.com/EgorLedyaev/kda_vk_hackathon/blob/main/backend/storage/public/logo.svg)

# Пример использования:

## Скачиваем репозиторий

```
git clone https://github.com/EgorLedyaev/kda_vk_hackathon.git
cd kda_vk_hackathon
```

## Устаналиваем зависимости

```
pip install -r requirements.txt
```

## Обучаем модель и сохраняем ее в файл baseline.model

```
python main.py --action=train --path_to_dataset="" --path_to_model="baseline.model"
```

## Оцениваем ROC-AUC на тестовом подмножестве пользователей

```
python main.py --action=evaluate --path_to_dataset="" --path_to_model="baseline.model"
```

## Получаем прогнозы для пользователей 1000100,1000121

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
