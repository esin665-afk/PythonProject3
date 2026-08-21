"""
Модуль main отвечает за основную логику проекта.
"""


from src.file_reader import read_csv_file, read_excel_file
from src.utils import load_transactions_from_json
from src.processing import filter_by_state, sort_by_date, search_by_description
from src.widget import mask_account_card, get_date
from src.external_api import convert_to_rubles


def main() -> None:
    """
    Основная функция программы.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # 1. Выбор источника данных
    print("\nВыберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("\nВаш выбор: ").strip()

    transactions = []

    if choice == "1":
        print("\nДля обработки выбран JSON-файл.")
        transactions = load_transactions_from_json("data/operations.json")
    elif choice == "2":
        print("\nДля обработки выбран CSV-файл.")
        transactions = read_csv_file("data/transactions.csv")
    elif choice == "3":
        print("\nДля обработки выбран XLSX-файл.")
        transactions = read_excel_file("data/transactions_excel.xlsx")
    else:
        print("\nНеверный выбор. Попробуйте снова.")
        return

    if not transactions:
        print("\nНе найдено ни одной транзакции.")
        return

    # 2. Фильтрация по статусу
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input("Статус: ").strip().upper()

        if status in valid_statuses:
            break
        print(f"Статус операции \"{status}\" недоступен.")

    transactions = filter_by_state(transactions, status)
    print(f"\nОперации отфильтрованы по статусу \"{status}\"")

    if not transactions:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    # 3. Сортировка по дате
    sort_choice = input("\nОтсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice in ["да", "yes", "д", "y"]:
        order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        if order in ["по возрастанию", "возрастанию", "возрастание", "asc"]:
            transactions = sort_by_date(transactions, reverse=False)
        else:
            transactions = sort_by_date(transactions, reverse=True)

    # 4. Фильтр по рублёвым транзакциям
    rub_choice = input("\nВыводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if rub_choice in ["да", "yes", "д", "y"]:
        transactions = [t for t in transactions if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"]

    if not transactions:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    # 5. Фильтр по описанию
    desc_choice = input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if desc_choice in ["да", "yes", "д", "y"]:
        search_word = input("Введите слово для поиска: ").strip()
        transactions = search_by_description(transactions, search_word)

    if not transactions:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    # 6. Вывод результатов
    print("\nРаспечатываю итоговый список транзакций...")
    print(f"\nВсего банковских операций в выборке: {len(transactions)}")

    for transaction in transactions:
        print("\n" + "-" * 50)

        # Дата
        date_str = transaction.get("date", "")
        if date_str:
            try:
                formatted_date = get_date(date_str)
                print(f"{formatted_date}", end=" ")
            except ValueError:
                print(f"{date_str[:10]}", end=" ")

        # Описание
        description = transaction.get("description", "Без описания")
        print(description)

        # Откуда → куда
        from_account = transaction.get("from", "")
        to_account = transaction.get("to", "")

        if from_account and to_account:
            # Маскируем счета/карты
            from_masked = mask_account_card(from_account) if " " in from_account else from_account
            to_masked = mask_account_card(to_account) if " " in to_account else to_account
            print(f"{from_masked} -> {to_masked}")
        elif to_account:
            to_masked = mask_account_card(to_account) if " " in to_account else to_account
            print(f"-> {to_masked}")

        # Сумма
        op_amount = transaction.get("operationAmount", {})
        amount = op_amount.get("amount", "0")
        currency = op_amount.get("currency", {}).get("code", "RUB")

        # Если не RUB — конвертируем
        if currency != "RUB":
            try:
                rub_amount = convert_to_rubles(transaction)
                print(f"Сумма: {rub_amount:.2f} руб.")
            except Exception:
                print(f"Сумма: {amount} {currency}")
        else:
            print(f"Сумма: {amount} руб.")

    print("\n" + "=" * 50)
    print("Программа завершена.")


if __name__ == "__main__":
    main()