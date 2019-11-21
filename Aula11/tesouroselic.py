def rentabilidade(valorinvestido, cotas, taxaselic):
    resultado = valorinvestido / cotas * (1+taxaselic+0.02)**4
    return resultado
