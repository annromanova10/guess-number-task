# функция для оценки
import numpy as np

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
    
    # моя функция
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    min_n, max_n = 0, 101 #объявляем границы как минимум и максимум
    predict_number = np.random.randint(1,100) # предполагаемое число

    while predict_number != number: #цикл пока загаданное не равно нашему
      count += 1 # увеличиваем счетчик
      if predict_number > number:
        max_n = predict_number # меняем верхнюю границу
        predict_number = (max_n + min_n)//2
      elif predict_number < number:
        min_n = predict_number # меняем нижнюю границу
        predict_number = (max_n + min_n)//2

    # Ваш код заканчивается здесь
   
    return count

# оценка качества
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)



def count_attempt(loocking_number):
    """ Функция для сбора статистики расчетов нашего когда.
        Принимает функцию, выдает сообщение о максимальном, минимальном и среднем
        количестве результатов выполнения нашего кода за 1000 запусков
    """
    
    count_lst = []
    np.random.seed(5)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:   
        count_lst.append(loocking_number(number))


    print(f'Среднее число попыток {int(np.mean(count_lst))}') # Ожидаемо 6
    print(f'Максимальное количество попыток {max(count_lst)}') # Ожидаемо до 8 при целочисленном делении диапазона
    print(f'Минимальное количество попыток {min(count_lst)}') # Ожидаемо 1
    
    
count_attempt(game_core_v3)