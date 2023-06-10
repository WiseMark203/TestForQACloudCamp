# Использование официальной среды выполнения Python в качестве родительского образа
FROM python:3.10

# Устанавка рабочего каталога в контейнере
WORKDIR /usr/src/app

# Добавление кода текущего каталога в рабочий каталог в контейнере
ADD . /usr/src/app

#Установка всех необходимых пакетов, указанных в requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Команда для запуска
CMD ["pytest", "-vv"]
