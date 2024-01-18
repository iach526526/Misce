import random
#by chatGPT
def generate_expression(result_limit):
    operators = ['+', '-', '*', '/']

    def generate_term():
        return str(random.randint(1, 1000))

    def generate_factor():
        return f"({generate_expression(result_limit)})" if random.choice([True, False]) else generate_term()

    expression = generate_factor()
    while random.choice([True, False]):
        operator = random.choice(operators)
        expression += f" {operator} {generate_factor()}"

    return expression

def generate_random_expression():
    result_limit = 99999  # 5位數以內
    return generate_expression(result_limit)

random_expression = generate_random_expression()
print("隨機生成的四則運算式：", random_expression)
