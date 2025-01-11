# TRIANGULO DE PASCAL
Código Python para emular a criação do Triângulo de Pascal.

## Oque é?
O Triângulo de Pascal é uma construção matemática em formato triangular que organiza os coeficientes binomiais. Cada número no triângulo é obtido somando os dois números diretamente acima dele. Essa estrutura simples e poderosa é amplamente utilizada em diversas áreas da matemática, como análise combinatória, álgebra e probabilidades.

                                                                 1            
                                                               1, 1        
                                                              1, 2, 1       
                                                            1, 3, 3, 1      
                                                           1, 4, 6, 4, 1     
                                                      Triângulo de Pascal para n = 4

Embora seja chamado de Triângulo de Pascal em homenagem ao matemático francês Blaise Pascal, que aprofundou seu estudo no século XVII, sua origem remonta a séculos antes. Uma das primeiras referências conhecidas do triângulo foi feita na China. No século XIII, o matemático chinês Yang Hui (1238–1298) destacou-se como um dos mais renomados estudiosos deste Triângulo Aritmético. Ele escreveu dois livros que buscavam compreender suas propriedades e aplicações.

## Número Binomial

Um **número binomial**, é um coeficiente que aparece na expansão do **Binômio de Newton** e é usado para contar o número de maneiras de escolher k elementos de um conjunto com n elementos, sem levar em conta a ordem. Por isso, também é chamado de **coeficiente binomial**.

A fórmula para calcular um número binomial é:

![image](https://github.com/user-attachments/assets/18084589-243e-49c6-a8b4-af588a970f27)

onde n! representa o fatorial de n, que é o produto de todos os números inteiros positivos de 1 até n.

## Construção do Triângulo

O triângulo de Pascal é construído colocando-se os números binomiais de mesmo numerador na mesma linha e os coeficientes de mesmo denominador na mesma coluna. Assim, temos:

![image](https://github.com/user-attachments/assets/f0fa8538-8b61-4756-beaf-bfeffbc72d63)

O código disponibilizado consegue apresentar o triângulo e o total de combinações possíveis em cada linha.



                                                             ▲ de Pascal                                                            N.
                                                                  1                                                                 1
                                                                1, 1                                                                2
                                                               1, 2, 1                                                              4
                                                             1, 3, 3, 1                                                             8
                                                            1, 4, 6, 4, 1                                                           16
                                                         1, 5, 10, 10, 5, 1                                                         32
                                                       1, 6, 15, 20, 15, 6, 1                                                       64
                                                     1, 7, 21, 35, 35, 21, 7, 1                                                     128
                                                   1, 8, 28, 56, 70, 56, 28, 8, 1                                                   256
                                                1, 9, 36, 84, 126, 126, 84, 36, 9, 1                                                512
                                            1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1                                           1024
                                         1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1                                         2048
                                       1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1                                      4096
                                  1, 13, 78, 286, 715, 1287, 1716, 1716, 1287, 715, 286, 78, 13, 1                                  8192
