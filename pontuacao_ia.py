nome_ia = input('Digite o nome da IA')
pontuacao_ia = float(input('Digite a pontuacao'))

if pontuacao_ia >= 39.9:
    print(f' Com esta pontuação{nome_ia} se encaixa em IA Aprendiz!⚙️')
elif pontuacao_ia >= 40:
    print(f' Com esta pontuação{nome_ia} se encaixa em "IA Mediana! ⚠️ ')
elif pontuacao_ia >= 69.9:
    print(f' Com esta pontuação{nome_ia} se encaixa em IA Boa! 📈')
elif pontuacao_ia >= 90: 
    print(f'Com esta pontuacao{nome_ia} se encaixa em IA Avançada! ✨🏆')
elif pontuacao_ia >= 100:
    print(f'Com esta pontuação{nome_ia} ... ❌é invalida❌!!')
else:
    print(F'Com esta pontuação... Evite{nome_ia}!! 📉')