# Демонстрационные данные (минимум 5 записей)
equipment_db = [
    {"id": "INV-001", "type": "ПК", "name": "Dell OptiPlex 3080", "room": "А-101", "status": "исправно"},
    {"id": "INV-002", "type": "Монитор", "name": "Samsung 24\"", "room": "А-101", "status": "исправно"},
    {"id": "INV-003", "type": "Принтер", "name": "HP LaserJet Pro", "room": "А-102", "status": "требует ремонта"},
    {"id": "INV-004", "type": "ПК", "name": "Lenovo ThinkCentre", "room": "А-102", "status": "исправно"},
    {"id": "INV-005", "type": "Проектор", "name": "Epson EB-X41", "room": "А-103", "status": "списано"},
]

def show_equipment():
    print("\n--- Список оборудования ---")
    if not equipment_db:
        print("База оборудования пуста.")
        return
    for item in equipment_db:
        print(f"[{item['id']}] {item['type']} '{item['name']}' | Кабинет: {item['room']} | Статус: {item['status']}")
    print("-" * 27)