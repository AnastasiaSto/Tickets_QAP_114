qnt_tickets = int(input("Введите количество билетов, которые Вы хотите приобрести: "))
persons_ages = []
for i in range(0, qnt_tickets):
    input_value = int(input(f"Введите возраст участника конференции №{i + 1}:\n"))
    persons_ages.append(input_value)
    def price(age):
        if age < 18:
            return 0
        elif 18 <= age <= 25:
            return 990
        else:
            return 1390
    total_price = sum(map(price, persons_ages))
discount_price = int(total_price * 0.9)
if qnt_tickets > 3:
    print("Стоимость Ваших билетов со скидкой: ", discount_price, "руб.")
else:
    print("Стоимость Ваших билетов: ", total_price, "руб.")

    



