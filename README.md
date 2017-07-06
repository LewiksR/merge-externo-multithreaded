# Relatório do script Merge Sort Externo com threads

Código em Python 3
Executado em sistema Ubuntu, processador Intel Core i5-3470 @ 3.2GHz Quad core.

O arquivo providenciado pelo professor contém aproximadamente 700 mil registros de endereços. Para simular uma situação onde o sistema processando tal arquivo não o conseguiria armazená-lo inteiramente na memória RAM, escrevemos o script de merge sort externo, ou seja, modificando o arquivo diretamente em disco.

----

Para uma última atividade no semestre, escolhi tentar acelerar esse script, fazendo-o utilizar vários núcleos do processador. O esperado era de que o tempo de execução fosse ligeiramente reduzido, limitado apenas pela velocidade de escrita do disco rígido. Porém, isso não ocorreu. Pelo contrário, o tempo de execução aumentou.

Reli o código que escrevi, prestando atenção no aumento de complexidade causado pela execução multithread que tentei, mas por falta de experiência em aplicações multithread não consegui descobrir o porquê da diferença de eficiência.

----

# Análise

No relatório gerado pelo utilitário cProfile, da linguagem Python, o tempo de execução das 5 funções mais custosas do programa foram todos reduzidos consideravelmente.

- 
  > 10231775    0.846    0.000    0.846    0.000 {built-in method builtins.len}
- 
  > 
- 
- 
- 
