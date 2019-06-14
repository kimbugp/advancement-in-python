#%%
def reversed_args(f):
    def inverter(*args):
        return f(*args[::-1])
    return inverter
        
int_func_map = {
    'pow': pow,
    'cmp': lambda a, b: 0 if a == b else [1, -1][a < b],
}

string_func_map = {
    'join_with': lambda separator, *args: separator.join(args),
    'capitalize_first_and_join': lambda first, *args: ''.join([first.upper()] + list(args)),
}

queries = int(input())
for _ in range(queries):
    line = input().split()
    func_name, args = line[0], line[1:]
    if func_name in int_func_map:
        args = list(map(int, args))
        print(reversed_args(int_func_map[func_name])(*args))
    else:
        print(reversed_args(string_func_map[func_name])(*args))


#%%
