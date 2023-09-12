def seg_min(seg):
    return seg / 60

def min_hor(min):
    return min / 60

if __name__ == "__main__":
    segundos = 150
    minutos = seg_min(segundos)
    print(f"{segundos} segundos son igual a {minutos} minutos")