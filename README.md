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

- Método _len_ reduzido de 0.846 segundos para 0.226s (**26%** do tempo original)
  - > 10231775    0.846    0.000    0.846    0.000 {built-in method builtins.len}
  - > 2797379/2797373    0.226    0.000    0.226    0.000 {built-in method builtins.len}
- Método _pack_ reduzido de 1.395 segundos para 0.196s (**14%** do tempo)
  - > 5397228    1.395    0.000    1.395    0.000 {method 'pack' of 'Struct' objects}
  - > 699307    0.196    0.000    0.196    0.000 {method 'pack' of 'Struct' objects}
- Método _read_ reduzido de 2.346 segundos para 0.537s (**23%** do tempo)
  - > 6096675    2.346    0.000    2.346    0.000 {method 'read' of '_io.BufferedReader' objects}
  - > 1398616    0.537    0.000    0.537    0.000 {method 'read' of '_io.BufferedReader' objects}
- Método _unpack_ reduzido de 2.460 segundos para 0.740s (**30%** do tempo)
  - > 7570681    2.460    0.000    2.460    0.000 {method 'unpack' of 'Struct' objects}
  - > 2097919    0.740    0.000    0.740    0.000 {method 'unpack' of 'Struct' objects}
- Método _write_ reduzido de 3.844 segundos para 0.420s (**10%** do tempo)
  - > 5397228    3.844    0.000    3.844    0.000 {method 'write' of '_io.BufferedWriter' objects}
  - > 699307    0.420    0.000    0.420    0.000 {method 'write' of '_io.BufferedWriter' objects}

Apesar dessas melhoras, isso não impediu o tempo total de execução de aumentar. Não tenho certeza se é devido à maneira que utilizei de esperar os threads acabarem de executar ou por concorrêcia ao acesso no disco, como foi uma hipótese do professor.
Eu havia descartado essa possibilidade de concorrência devido à redução dos tempos individuais de _write_ e _read_, mas ao analisar os resultados de cProfile com mais cuidado, notei que o número de chamadas a _pack_ e _write_ foi reportado como exatamente o número de entradas de endereço no arquivo. Pela lógica do algoritmo _merge sort_ isso é impossível de ser verdade, já que as entradas individuais são reescritas diversas vezes toda vez que dois arquivos sao mesclados novamente. Portato, minha conclusão é que a hipótese do professor é verdadeira, e que o cProfile não reporta os resultados de programas multithread corretamente.
