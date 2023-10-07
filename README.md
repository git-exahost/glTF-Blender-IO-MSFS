## FlightSim Blender glTF 2.0 Importador e Exportador + Bloom

Este repositório contém uma versão modificada do plugin de importação/exportação do Microsoft Flight Simulator para Blender, baseado na versão 1.3.2 do plugin oficial da Asobo, com algumas pequenas modificações e traduções para o Português do Brasil.

Link do Plugin Oficial:
https://github.com/AsoboStudio/glTF-Blender-IO-MSFS

Este plugin desbloqueia o recurso **Emissive Color** responsável por gerar Light Bloom ou Glow, que reproduz os efeitos de iluminação do mundo real. O efeito Bloom funciona aplicando um filtro na imagem que aumenta o brilho das partes mais claras e cria um borrão nas bordas. Isso faz com que a luz pareça mais intensa e difusa, como acontece na vida real quando olhamos para uma fonte de luz muito forte.

#### Como utilizar o efeito Bloom ao gear o gLTF para a SDK

Em **MSFS Material Params**, como na imagem abaixo, selecione **Emissive Color** e aumente seu valor para **1**. Este é o valor máximo de emissão. Observe que agora o objeto passa a emitir a iluminação brilhando no escuro, mas ele ainda não emite o efeito Bloom.

![MSFS Material Params](https://github.com/git-exahost/glTF-Blender-IO-MSFS/blob/main/misc/MSFSMaterialParams.jpg)

Para adicionar o efeito Bloom, procure por **General Parameters** e altere o parâmetro **Emissive Scale**, e adicione valores acima de 1; quanto maior o valor, maior será o nível de emissão. Os valores adicionados serão multiplicados pelo **Emissive Color** definido, gerando o efeito Bloom. Fique à vontade para testar diversos valores.

![Emission Strengths](https://github.com/git-exahost/glTF-Blender-IO-MSFS/blob/main/misc/GeneralParameters.jpg)

Para ver o resultado do efeito Bloom no Blender sem ter que compilar e gerar o glTF, vá em **Render Properties** e marque o item **Reluzir**, como na imagem abaixo:

![Reluzir](https://raw.githubusercontent.com/git-exahost/glTF-Blender-IO-MSFS/main/misc/Reluzir.jpg) 

#### Guia de Instalação do Plugin Blender

Esta versão é projetada para compatibilidade com o **Blender 3.6.4**. Certifique-se de ter o **Blender 3.6.4** instalado, utilizando o link abaixo:<br>
[Download Blender 3.6.4](https://www.blender.org/download/lts/3-6/)

### Instruções de Instalação

1. Certifique-se de que o Blender está fechado.
2. Faça o download do arquivo **glTF-Blender-IO-MSFS** clicando em **Releases** e, em seguida, clique em **glTF-Blender-IO-MSFS.zip**.
3. Extraia o conteúdo do arquivo ZIP na seguinte pasta: **C:\Users\seu usuário\AppData\Roaming\Blender Foundation\Blender\3.6\scripts\addons**, ou, de forma global, em **C:\Program Files\Blender Foundation\Blender 3.6\3.6\scripts\addons**.
