# QAP_PetFriends_Testing

Тестируемый ресурс: <a href="https://petfriends.skillfactory.ru/" target="_blank">https://petfriends.skillfactory.ru</a>

Описание API-методов доступно по адресу: <a href="https://petfriends.skillfactory.ru/apidocs/#/" target="_blank">https://petfriends.skillfactory.ru/apidocs/#/</a>

**Структура проекта:**

1. Директория _/tests_ содержит файл _test_petfriends.py_ с реализованными тестами.
   
3. Директория _/tests/images_ содержит фото в разных форматах для реализации теста с добавлением фото питомца.

4. Корневая директория содержит файл _settings.py_ с прописанными в нем валидными логином и паролем, а также файл _api.py_ с реализованными API-методами.


**Список тестов, реализованных в проекте:**

1. Запрос API ключа с некорректным email - **FAIL**

2. Запрос API ключа с пустым паролем - **FAIL**

3. Запрос списка питомцев с некорректным API ключом - **FAIL**

4. Упрощенное (без фото) добавление питомца с корректными данными - **PASS**

5. Упрощенное (без фото) добавление питомца с некорректным именем (свыше 150 символов + спецсимволы) - **PASS**

6. Упрощенное (без фото) добавление питомца с некорректным возарстом - **PASS**

7. Упрощенное (без фото) добавление питомца с пустыми параметрами - **PASS**

8. Удаление питомца с пустым id - **FAIL**

9. Добавление фото к ранее опубликованному питомцу в формате png - **FAIL**

10. Добавление фото к ранее опубликованному питомцу в формате pdf - **FAIL**
