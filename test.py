
def extract_vector(v):
    tmp = v.split(",")

    return float(tmp[0]), float(tmp[1])

def dot_product(v1, v2):
    v1x, v1y = extract_vector(v1)
    v2x, v2y = extract_vector(v2)

    # Fazer o cálculo
    dp = v1x * v2x + v1y * v2y

    return dp


print(dot_product("2.0, 0", "1, 1"))

