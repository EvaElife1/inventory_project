import pytest
from inventory import equipment_db

def test_demo_data_count():
    assert len(equipment_db) >= 5, "Ошибка: В базе меньше 5 записей"

# TC-02: Проверка структуры карточки оборудования (наличие нужных полей)
def test_equipment_structure():
    assert len(equipment_db) > 0, "База пуста"
    item = equipment_db[0]
    expected_keys = {"id", "type", "name", "room", "status"}
    assert set(item.keys()) == expected_keys, "Ошибка: Неверный формат ключей в словаре"

# TC-03: Проверка уникальности инвентарных номеров
def test_unique_inventory_ids():
    ids = [item["id"] for item in equipment_db]
    assert len(ids) == len(set(ids)), "Ошибка: Найдены дублирующиеся инвентарные номера"