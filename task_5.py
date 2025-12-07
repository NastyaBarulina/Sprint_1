class TestCase:

    def __init__(self):
        self.steps = {}
        self.result = None

    # Добавляет в словарь шаг ТК:
    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text

    # Удаляет шаг:
    def delete_step(self, step_number):
        if step_number in self.steps:
            del self.steps[step_number]
    
    # Устанавливает ОР:
    def set_result(self, result):
        self.result = result

    # Печатает информацию в нужном формате:
    def get_test_case(self):
        print({
            'Шаги': self.steps,
            'Ожидаемый результат': self.result
        })

# Примеры использования класса TestCase

# Создание экземпляра test_case_1
test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')           # Первый шаг
test_case_1.set_step(3, 'Перейти в раздел Товары')  # Третий шаг
test_case_1.delete_step(3)                          # Удаление третьего шага
test_case_1.set_step(2, 'Перейти в раздел Товары')  # Второй шаг
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')  # Третий шаг
test_case_1.set_result('Товар окажется в корзине')  # ОР
test_case_1.get_test_case()                         # Весь кейс

# Создание второго экземпляра test_case_2
test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')          # Первый шаг
test_case_2.set_step(2, 'Перейти в раздел Корзина') # Второй шаг
test_case_2.set_step(3, 'Нажать кнопку "Удалить"') # Третий шаг
test_case_2.set_result('Товар удален из корзины')   # ОР
test_case_2.get_test_case()                         # Весь кейс
