import itertools
def part1():
    with open('../inputs/7.txt', "r") as f:
        lines = f.readlines()
        left, right = [], []
        for line in lines:
            data = line.strip().split(':')
            left.append(data[0])
            right.append(data[1].split())
    
    def generate_combs(numbers):
        operators = ['*', '+']
        n = len(numbers)
        opr_combs = list(itertools.product(operators, repeat=n-1))
        
        expressions = []
        for opr in opr_combs:
            expression = [numbers[0]]
            for i, op in enumerate(opr):
                expression.append(op)
                expression.append(numbers[i+1])
            expressions.append(expression)
        return expressions
    res = []
    
    def evaluate_expr(expr):
        total = int(expr[0])
        for i in range(1, len(expr), 2):
            opr = expr[i]
            num = int(expr[i+1])
            if opr == '+':
                total += num
            else:
                total *= num
        return total 
        
    for i in range(len(left)):
        expressions = generate_combs(right[i])
        for expr in expressions:

            if evaluate_expr(expr) == int(left[i]):
                res.append(int(left[i]))
                break
        
    return sum(res)

def part2():
    with open('../inputs/7.txt', "r") as f:
        lines = f.readlines()
        left, right = [], []
        for line in lines:
            data = line.strip().split(':')
            left.append(data[0])
            right.append(data[1].split())
    
    def generate_combs(numbers):
        operators = ['*', '+', '||']
        n = len(numbers)
        opr_combs = list(itertools.product(operators, repeat=n-1))
        
        expressions = []
        for opr in opr_combs:
            expression = [numbers[0]]
            for i, op in enumerate(opr):
                expression.append(op)
                expression.append(numbers[i+1])
            expressions.append(expression)
        return expressions
    res = []
    
    def evaluate_expr(expr):
        total = int(expr[0])
        for i in range(1, len(expr), 2):
            opr = expr[i]
            num = int(expr[i+1])
            if opr == '+':
                total += num
            elif opr == '||':
                total = (total * (10 ** len(str(num)))) + num
            else:
                total *= num
        return total 
        
    for i in range(len(left)):
        expressions = generate_combs(right[i])
        for expr in expressions:

            if evaluate_expr(expr) == int(left[i]):
                res.append(int(left[i]))
                break
    return sum(res)
    
if __name__ == "__main__":
    print(part2())
