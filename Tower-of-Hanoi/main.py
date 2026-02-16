def hanoi_solver(n):
    origen = list(range(n, 0, -1))
    destino = []
    auxiliar = []
    historial = []

    historial.append(f"{origen} {auxiliar} {destino}")

    def mover_disco(n, fuente, meta, aux):
        if n == 0:
            return
        mover_disco(n - 1, fuente, aux, meta)
        movimiento = meta.append(fuente.pop())
        historial.append(f"{origen} {auxiliar} {destino}")
    
        mover_disco(n - 1, aux, meta, fuente)

    mover_disco(n, origen, destino, auxiliar)
    return "\n".join(historial)

