# Conversor de PDF para Markdown (com docling)

Script Python que converte arquivos PDF em documentos Markdown (`.md`) usando a biblioteca [`docling`](https://github.com/docling-project/docling). Desenvolvi o algoritmo de conversão em masso no PyCharm.

## 📋 Pré-requisitos
- **Python 3.8+** (recomendado)
- [**PyCharm**](https://www.jetbrains.com/pycharm/) (ou outra IDE/editor de sua preferência)
- **Pacote `docling`** instalado
- **Arquivos PDF** para conversão
  
---

## 🛠 Instalação

### 1. Configurar ambiente no PyCharm
- Crie um `Novo Projeto`, `Pure Python`
- Vá no `Terminal` (`Ctrl` + `` ), e execute `pip install docling`

### 2. Main.py
- Com isso, pode criar um arquivo [`main.py`](https://github.com/sthecss/docling/blob/main/main.py) e colar o código.

---

## 🚀 Como Usar

### Estrutura de Pastas recomendada:
```
/docling
  ├── /PDF/          # Coloque seus PDFs aqui
  ├── /MD/           # Arquivos Markdown gerados
  └── main.py   # Script principal
```

### Executando o Script
1. Modifique no código os caminhos das pastas (se necessário):
   ```python
   input_dir = Path("D:/docling/PDF/")
   output_dir = Path("D:/docling/MD/")
   ```
2. Execute.

---

### Saída Esperada
- Cada PDF será convertido em um arquivo `.md` com o mesmo nome.
- Logs no console indicarão sucesso/erros:
  ```
  Convertendo: aula1.pdf...
  ✅ Salvo em: D:/docling/MD/aula1.md
  ```

---

## ⚙️ Algoritmo (Lógica do Script)
1. **Entrada**: Lista todos os arquivos `.pdf` da pasta de entrada.
2. **Processamento**:
   - Para cada PDF, usa `docling.DocumentConverter()` para extrair texto.
   - Converte o resultado para Markdown com `.export_to_markdown()`.
3. **Saída**: Salva um arquivo `.md` na pasta de destino, preservando o nome original.

---

## 💡 Dicas
- **PDFs com imagens**: O `docling` pode não extrair texto de imagens (depende do modelo usado).
- **Erros comuns**:
  - Caminhos incorretos (verifique se as pastas existem).
  - PDFs corrompidos (teste individualmente).
- **Otimização**: Para muitos arquivos, considere adicionar um delay entre conversões.

---

## 📄 Licença
Projeto livre para uso e modificação. Consulte a licença do `docling` para detalhes sobre redistribuição.

---
