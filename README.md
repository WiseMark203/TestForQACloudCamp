## **Установка**
1. _Клонируйте репозиторий_:
    ```
    git clone https://github.com/WiseMark203/TestForQACloudCamp.git
    ```
2. _Перейдите в каталог проекта_:
    ```
    cd jsonplaceholder_tests
    ```
3. _Установите необходимые зависимости_:
    ```
    pip install -r requirements.txt
    ```

## **Запуск тестов**
Чтобы запустить тесты, используйте команду pytest: 
    ```
    pytest -vv
    ```

## **Запуск с помощью Docker**

Проект также можно запустить в Docker. Убедитесь, что у вас установлен Docker, и выполните следующие шаги:

1. Соберите Docker образ:
    ```
    docker build -t jsonplaceholder_tests .
    ```
2. Запустите контейнер:
    ```
    docker run jsonplaceholder_tests
    ```

## **Задание** 
_**Стратегия тестирования нового функционала**:_

1. _Функциональное тестирование_

Цель: Проверить, работает ли новая функциональность, как ожидается.

1.1 Попытаться создать базу данных с недопустимыми значениями, такими как: слишком длинное имя базы данных, 
недопустимый регион размещения, слишком большой размер и убедиться, что система корректно обрабатывает 
такие ситуации и предотвращает создание базы данных.

1.2 Создать базу данных без заполнения одного или нескольких обязательных полей и убедиться, что система не позволяет создать такую
базу данных и предлагает заполнить все обязательные поля.

2. _Тестирование производительности_

Цель: Убедиться, что новая функциональность не снижает общую производительность системы.

2.1 Создать несколько баз данных одновременно и убедиться, что время ответа системы остается приемлемым.

2.2 Создать базу данных большого размера и убедиться, что время создания базы данных остается в разумных пределах.

3. _Тестирование пользовательского интерфейса_

Цель: Убедиться, что пользовательский интерфейс новой функциональности интуитивно понятен и работает корректно.

3.1 Проверить, что все элементы интерфейса (поля формы, кнопка "Создать" и т.д.) отображаются корректно и работают, как ожидается.

3.2 Проверить, что все сообщения об ошибках или подсказки, которые появляются при работе с новой функциональностью, понятны и полезны для пользователя.

4. _Тестирование безопасности_

Цель: Проверить насколько новая функциональность защищена от возможных атак.

4.1 Проверка на уязвимости на SQL-инъекции при вводе имени базы данных.

4.2 Проверка, что доступ к базе данных ограничен только уполномоченными пользователями.

4.3 Проверка на возможность перебора различных вариантов ввода данных с целью выявить уязвимости системы.





