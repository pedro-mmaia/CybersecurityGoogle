# Automate Cybersecurity Tasks with Python

Este diretório contém scripts Python criados para automatizar tarefas comuns de cibersegurança, demonstrando o uso de programação para agilizar processos operacionais.

## Arquivos e Estrutura

- **`atualizarUmArquivo.py`**: Script em Python responsável por ler um arquivo de lista de permissões (`allow_list.txt`), remover endereços IP especificados (através de uma lista de remoção) e gerar um novo arquivo atualizado (`allow_list_updated.txt`). 
- **`allow_list.txt`**: Arquivo de texto contendo a lista original de endereços IP permitidos.
- **`allow_list_updated.txt`**: Arquivo de texto gerado pelo script, contendo a lista atualizada de endereços IP após a limpeza.
- **`testes/`**: Pasta destinada a scripts de teste e dados temporários (esta pasta é ignorada pelo controle de versão do git).

## Como Executar

Para executar o script que atualiza a lista de permissões, basta rodar o seguinte comando no terminal:

```bash
python3 atualizarUmArquivo.py
```

Isso fará com que as alterações sejam aplicadas e o arquivo `allow_list_updated.txt` seja salvo neste mesmo diretório.
