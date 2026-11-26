# Blockchain para Leitura de Sensores



Protótipo de blockchain permissionada, em Python, para registrar de forma íntegra e verificável leituras de sensores (temperatura) de um meio naval. Código desenvolvido no Trabalho de Conclusão de Curso *"Aplicabilidade da Tecnologia do Blockchain na Marinha do Brasil"* (CIAA, 2023) – Apêndices A e B.

## Conteúdo

|Arquivo|Descrição|
|-|-|
|`arduino/leitura\_temperatura/leitura\_temperatura.ino`|Programa Arduino para leitura de temperatura (Apêndice A)|
|`blockchain\_dados.py`|Blockchain de leitura de sensores – classes `Block` e `Blockchain`, login e carga das leituras (Apêndice B)|
|`data.csv`|Arquivo de exemplo com 10 leituras (`data-hora,temperatura`), conforme Figuras 9 e 10 do trabalho|

## Funcionamento

1. As leituras do sensor são gravadas em `data.csv` (uma leitura por linha: data-hora e valor).
2. O usuário faz login (credenciais cadastradas no próprio código: usuário `CIAA`, senha `2023`).
3. Cada linha de `data.csv` é adicionada como um novo bloco, encadeado pelo hash SHA-256 do bloco anterior.
4. O programa informa se a blockchain é válida (comparando os hashes de cada bloco *i* com o bloco *i-1*) e exibe todos os blocos com seus hashes.

## 

## Requisitos e execução

* Python 3 (apenas biblioteca padrão: `hashlib`, `datetime`, `csv`).
* Arduino IDE (opcional, para o sensor de temperatura no pino A4).

```bash
python blockchain\_dados.py
```

Execute no diretório que contém `data.csv`.

> Protótipo acadêmico/didático: as credenciais estão fixas no código e não há rede distribuída. Não use em produção sem as devidas adaptações.

## 

## Como citar

Veja `CITATION.cff` (o GitHub mostra o botão *Cite this repository*). Trabalho de origem:

ALMEIDA, Rodrigo Antonio Ribeiro de. **Aplicabilidade da tecnologia do blockchain na Marinha do Brasil**. 2023. Trabalho de Conclusão de Curso (Curso de Aperfeiçoamento Avançado em Segurança da Informação e Comunicações) – Centro de Instrução Almirante Alexandrino (CIAA), Marinha do Brasil, Rio de Janeiro, 2023. Orientadores: Prof. Dr. Carlos Vinicio Rodriguez; Capitão-Tenente Warlley Paulo Freire.

## Licença

MIT – veja `LICENSE`.

