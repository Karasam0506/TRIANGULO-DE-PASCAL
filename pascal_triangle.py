"""Modulo cria uma classe que execute as aplicações do ▲ (Triângulo) de Pascal"""
import math
import re

def add_text_up(ori, new):
    """
    Adiciona um texto no início de outro, separando-os por uma quebra de linha.

    Parâmetros:
    ori (str): O texto original que será mantido.
    new (str): O texto a ser adicionado no início.

    Retorna:
    str: A concatenação do novo texto seguido do texto original, separados por uma quebra de linha.
    """
    return f"{new}\n{ori}"

def spacer( txt:str, len_ori:int) -> str:
    """
    Centraliza um texto dentro de uma largura especificada,
    adicionando espaços em branco antes do texto.

    Parâmetros:
    txt (str): O texto que será centralizado.
    len_ori (int): O comprimento total da linha em que o texto será centralizado.

    Retorna:
    str: O texto centralizado com espaços à esquerda para alcançar o comprimento especificado.
    """
    tamano_lin = len(txt)
    espaco = math.ceil((len_ori - tamano_lin)/2)
    txt_espacado = espaco*' ' + txt
    return txt_espacado


class Pascal:
    """
    Gera e exibe o triângulo (▲) de Pascal junto com a potência correspondente de 2 para cada linha.

    Atributos:
    ----------
    num_linhas (int): O número de linhas do ▲ de Pascal a ser gerado.
    triangle (list): A representação do ▲ de Pascal como uma lista de listas.
    num_combination (list): Lista com o número de combinações em cada linha.

    Métodos:
    --------
    gerar_triangulo() -> list:
        Gera o ▲ de Pascal com base no número de linhas especificado.

    gerar_combination() -> list:
        Gera uma lista contendo as potências de 2 para cada linha do ▲.

    prinTriangle():
        Exibe o ▲ de Pascal de forma centralizada, e o número total de combinações de cada linha.
    """
    def __init__(self, num_linhas: int  ):
        """
        Inicializa a classe Pascal.

        Parâmetros:
        -----------
        num_linhas (int): O número de linhas para o ▲ de Pascal. Deve ser um valor não negativo.

        Lança:
        -------
        ValueError: Se o número de linhas fornecido for negativo.
        """
        if num_linhas < 0:
            raise ValueError("O número de linhas não deve ser negativo")
        self.num_linhas = num_linhas
        self.triangle = self.gerar_triangulo()
        self.num_combination = self.gerar_combination()

    def gerar_triangulo(self) -> list:
        """
        Gera o ▲ de Pascal.

        Retorna:
        --------
        list: Uma lista de listas representando o ▲ de Pascal.
        """
        triangle = []
        for linha in range(self.num_linhas + 1):
            triangle.append( [math.comb( linha, column) for column in range( linha + 1)] )
        return triangle

    def gerar_combination(self) -> list:
        """
        Gera uma lista contendo o número de combinações de cada linha.

        Retorna:
        --------
        list: Uma lista com potências de 2 para cada linha do ▲.
        """
        combination = [ [2**quantiti] for quantiti in range(0, self.num_linhas+1)]
        return combination

    def print_triangle(self):
        """
        Exibe o ▲ de Pascal de forma centralizada e alinhada, com o número de combinações.

        A formatação inclui:
        - Centralização das linhas do ▲.
        - Exibição do título "▲ de Pascal" no topo.
        - Indicação das potências de 2 (N.) ao lado direito das linhas.
        """
        triangle_text = ""

        for linhas in range(self.num_linhas , -1, -1):

            brut_lin  = str(self.triangle[linhas])
            pre_lin = re.sub(r'[^0-9, ]', '', brut_lin)

            if linhas == self.num_linhas :
                max_len = len(pre_lin) + 4

            read_lin = spacer(txt = pre_lin, len_ori = max_len)
            dif_espaco = max_len - len(read_lin)

            pre_final_text = read_lin + dif_espaco*' '+ str(self.num_combination[linhas][0])

            triangle_text = add_text_up(ori = triangle_text, new = pre_final_text)

        cabecalho = spacer(txt = "▲ de Pascal", len_ori = max_len)

        dif_espaco_two = max_len - len(cabecalho)

        cabecalho_end = cabecalho + dif_espaco_two*' '+ "N."

        pascal_trianglu = add_text_up(ori = triangle_text, new = cabecalho_end)

        print( pascal_trianglu)

p = Pascal(20)
p.print_triangle()
