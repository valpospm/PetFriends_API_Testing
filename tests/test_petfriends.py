from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_with_invalid_email(email='''mailmail.ru''', password=valid_password):
    '''Запрашиваем API ключ с некорректно указанным адресом электронной почты'''

    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_with_invalid_password(email=valid_email, password=""):
    '''Запрашиваем API ключ с пустым паролем'''

    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_invalid_key(filter='my_pets'):
    '''Запрашиваем список питомцев с некорректно указанным API ключом'''

    auth_key = {
        "key": "123456789"
    }
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0

def test_simple_add_new_pet_with_valid_data(name='Рыжик', animal_type='лайка', age='2'):
    '''Проверяем, что можно добавить питомца без фотографии с корректными данными'''

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_simple_add_new_pet_with_invalid_name(name='''/d+w=;A6~d#PNHaz^kh!K4w4(Li4MAAC%soZD{)D_GP!§'w]@xBctJ5stgytO$DiB&:b'D`±±H*%U+_L02`~*Qpwt$l±j2}@1W(^b)f{t5'HZYWj`&mTo%J`9Zp{{cAE{i'nDcFLbmGlOq§D-u+TAq'rkEy-NKABsbzDr&+8"&Nwz^L@yJ=a*As}^(C]ZR!rhf37n-l`0Z#fyMjmikxZA+y)vLSrX&f%64hx]$$vO!wqpRX&y:-Vda}jUelkpe}Y''', animal_type='лайка', age='2'):
    '''Упрощенно (без фото) добавляем питомца с некорректным именем (свыше 150 символов, включая спецсимволы)'''

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_simple_add_new_pet_with_invalid_age(name='Тимофей', animal_type='кот', age='100'):
    '''Упрощенно (без фото) добавляем питомца с некорректно указанным возрастом'''

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_simple_add_new_pet_with_blank_data(name='', animal_type='', age=''):
    '''Упрощенно (без фото) добавляем питомца с пустыми параметрами (имя, тип животного, возраст)'''
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_delete_pet_with_blank_id():
    '''Удаляем питомца с пустым id'''

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Вводим пустой id и отправляем запрос на удаление
    pet_id = ''
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Проверяем что статус ответа равен 200
    assert status == 200

def test_successful_add_pet_png_photo(pet_photo='images/img_001.png'):
    '''Проверяем возможность добавление фото питомца в формате png'''

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем добавить фото
    if len(my_pets['pets']) > 0:
        status, result = pf.add_pet_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)

        # Проверяем что статус ответа = 200
        assert status == 200
    else:
        # если спиcок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

def test_successful_add_pet_pdf_photo(pet_photo='images/img_001.pdf'):
    '''Проверяем возможность добавление фото питомца в формате pdf'''

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем добавить фото
    if len(my_pets['pets']) > 0:
        status, result = pf.add_pet_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)

        # Проверяем что статус ответа = 200
        assert status == 200
    else:
        # если спиcок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")
