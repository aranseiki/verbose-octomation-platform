# Especificação Técnica – a automação de Organização de Downloads

## 1. Descrição
Esta automação tem como objetivo organizar arquivos de forma automatizada em um diretório específico (como Downloads), movendo-os para subpastas com base na extensão de cada arquivo.  
O foco é manter a pasta de entrada limpa e categorizar arquivos de forma prática e intuitiva.

---

## 2. Escopo
- A automação será executado em um diretório fornecido pelo usuário.
- Apenas arquivos serão processados; subpastas devem ser preservadas.
- A automação deve criar automaticamente subpastas correspondentes às categorias de arquivo, se não existirem.
- Categorias de arquivos podem incluir: imagens, documentos, PDFs, áudios, vídeos, outros.
- A automação deve permitir a configuração de mapeamento entre extensões e pastas.

---

## 3. Regras de Negócio
1. **Entrada do diretório**: o usuário define o caminho onde os arquivos estão localizados.
2. **Processamento exclusivo de arquivos**: diretórios existentes não serão movidos ou renomeados.
3. **Categorias pré-definidas e personalizáveis**:
   - Imagens: `.jpg`, `.jpeg`, `.png`, `.gif`
   - Documentos: `.txt`, `.docx`, `.odt`
   - PDFs: `.pdf`
   - Áudios: `.mp3`, `.wav`
   - Vídeos: `.mp4`, `.avi`, `.mkv`
   - Outros: qualquer extensão não listada nas categorias acima
4. **Criação automática de subpastas**: se a pasta destino não existir, a automação deve criá-la.
5. **Resolução de conflitos**: se já existir um arquivo com o mesmo nome na pasta destino, a automação adiciona `_dup` ao novo nome.
   - Exemplo: `arquivo.pdf` → `arquivo_dup.pdf`
6. **Execução atômica**: nenhum arquivo deve ser sobrescrito ou perdido durante o processo.
7. **Registro de logs**: todos os processos devem ser logados em um arquivo de log do dia; apenas um arquivo de log deve ser criado por dia. 
8. **Relatório final**: ao término, a automação deve apresentar:
   - Total de arquivos encontrados
   - Total de arquivos movidos por categoria
   - Total de conflitos detectados

---

## 4. Requisitos Funcionais
- RF01: Permitir a escolha do diretório de entrada.
- RF02: Listar todos os arquivos do diretório ignorando subpastas.
- RF03: Criar subpastas para cada categoria de arquivo, se necessário.
- RF04: Mover arquivos para a subpasta correspondente à sua extensão.
- RF05: Tratar conflitos de nome com a regra `_dup`.
- RF06: Registrar log em todas as etapas do processo.  
- RF07: Gerar relatório de execução.

---

## 5. Requisitos Não Funcionais
- RNF01: O script deve ser implementado exclusivamente com bibliotecas nativas do Python.
- RNF02: O tempo de execução deve ser inferior a 1 segundo para até 100 arquivos.
- RNF03: O processo deve ser idempotente (rodar duas vezes não deve duplicar efeitos inesperados).

---

## 6. Fluxo Simplificado
1. Usuário informa diretório de entrada.  
2. A automação lista arquivos do diretório.  
3. Para cada arquivo:  
   - Identifica categoria com base na extensão  
   - Cria pasta destino, se não existir  
   - Verifica conflito de nome  
   - Move o arquivo ou adiciona `_dup`  
4. Registrar log em todas as etapas do processo.  
5. Exibe relatório final.
