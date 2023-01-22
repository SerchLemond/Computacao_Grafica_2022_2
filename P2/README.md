## Construção Final - Satélite

### Conteúdo da pasta:
- __ __pychache__ __: Um pasta de cache que o OpenGL cria ao botar o código para rodar;
- __pipeline__: Uma pasta contendo duas sub-pastas, SimpleTexture e WhiteDotsPipeline; responsaveis por renderizarem os poligonos da construção;
- __texture__: Uma pasta contendo as duas texturas a serem usadas;
- __requirements__.txt: Um txt que contém todas as extenções/pacotes Phyton necessários para fazer o código funcionar;
- __sateliteF__.py: O arquivo que contem o código para gerar a construção do satélite e do cenário;
- __print01.png__: Um print do código funcionando; faz parte da entrega da tarefa e foram salvos no github como bacukp.

### Como rodar o código:
- Abrir o terminal ou prompt de comando já direcionado na pasta onde estão salvos os arquivos e rodar o comando "python sateliteF.py"
  - ex: C:\Users\funalo\Documents\CG> python sateliteF.py

### Observações:
- É necessário que os arquivos dentro das pastas "pipeline" e "texture" estejam juntos a "sateliteF.py", na mesma pasta, para que este funcione devidamente;
- É necessário que as extensões numpy, Pillow, PyGLM, PyOpenGl, PySDL2 e pysdl2-dll estejam instaladas nas versões sugeridas (ou superiores). Consultar "requirements.txt" em caso de dúvida.
