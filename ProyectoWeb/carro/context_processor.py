def importe_total_carro(request):
    total=0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total=total+float(value["precio"])
    else:
        total= "Debes logearte"
        # este else despues ya no va a ser necesario
    return {"importe_total_carro": total}
