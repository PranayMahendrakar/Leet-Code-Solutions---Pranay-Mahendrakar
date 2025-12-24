# Problem: Parse Lisp Expression
# Difficulty: Hard
# URL: https://leetcode.com/problems/parse-lisp-expression/
# Runtime: 7 ms
# Memory: 12.5 MB

class Solution:
    def evaluate(self, expression):
        def parse(expr, scope):
            if expr[0] != '(':
                # Integer or variable
                if expr[0].isdigit() or expr[0] == '-':
                    return int(expr)
                return scope[expr]
            
            # Remove outer parentheses
            inner = expr[1:-1]
            
            # Tokenize
            tokens = []
            balance = 0
            start = 0
            for i, c in enumerate(inner):
                if c == '(':
                    balance += 1
                elif c == ')':
                    balance -= 1
                elif c == ' ' and balance == 0:
                    tokens.append(inner[start:i])
                    start = i + 1
            tokens.append(inner[start:])
            
            op = tokens[0]
            
            if op == 'add':
                return parse(tokens[1], scope) + parse(tokens[2], scope)
            elif op == 'mult':
                return parse(tokens[1], scope) * parse(tokens[2], scope)
            else:  # let
                new_scope = scope.copy()
                i = 1
                while i < len(tokens) - 1:
                    var = tokens[i]
                    val = parse(tokens[i + 1], new_scope)
                    new_scope[var] = val
                    i += 2
                return parse(tokens[-1], new_scope)
        
        return parse(expression, {})