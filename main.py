from PIL import Image

def converter_para_cinza(caminho_entrada, caminho_saida):
    # Abre a imagem e converte para tons de cinza (L = "luminance")
    imagem = Image.open(caminho_entrada).convert('L')
    imagem.save(caminho_saida)
    print(f"Imagem em tons de cinza salva como {caminho_saida}")

def converter_para_binaria(caminho_entrada, caminho_saida, limiar=128):
    # Abre a imagem em tons de cinza
    imagem = Image.open(caminho_entrada).convert('L')

    # Aplica binarização: pixels >= limiar viram 255 (branco), senão 0 (preto)
    imagem_binaria = imagem.point(lambda p: 255 if p >= limiar else 0)

    # Salva imagem binária
    imagem_binaria.save(caminho_saida)
    print(f"Imagem binária salva como {caminho_saida}")

def main():
    entrada = 'imagem.png'  # pode ser .png, .jpeg, etc.
    cinza = 'imagem_cinza.png'
    binaria = 'imagem_binaria.png'

    converter_para_cinza(entrada, cinza)
    converter_para_binaria(cinza, binaria, limiar=128)

if __name__ == '__main__':
    main()
