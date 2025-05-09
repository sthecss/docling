"""
Conversor em lote: PDF → Markdown (.md)
Automatiza a conversão de múltiplos arquivos PDF para Markdown usando docling.
"""

from docling.document_converter import DocumentConverter
from pathlib import Path

# Configuração de pastas
input_dir = Path("D:/docling/PDF/")            # Pasta de origem (PDFs)
output_dir = Path("D:/docling/MD/")            # Pasta de destino (arquivos .md)
output_dir.mkdir(parents=True, exist_ok=True)  # Cria a pasta de saída se não existir

converter = DocumentConverter()                # Inicializa o conversor

# Processamento até acabar os PDF:
for pdf_file in input_dir.glob("*.pdf"):       # Filtra apenas arquivos .pdf
    try:
        print(f"Convertendo: {pdf_file.name}...")
        
        # Conversão e exportação
        result = converter.convert(str(pdf_file))
        markdown_content = result.document.export_to_markdown()
        output_file = output_dir / f"{pdf_file.stem}.md"  # Mantém o nome original
        
        # Salva o arquivo .md
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        
        print(f"✅ Sucesso: {output_file}")
    
    except Exception as e:
        print(f"❌ Falha em {pdf_file.name}: {str(e)}")
