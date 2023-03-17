## FlightSim Blender glTF 2.0 Importador e Exportador + Bloom

Este repositório contém uma versão modificada do Microsoft Flight Simulator Blender Import/Export, baseada na versão 1.3.0 do plugin oficial da Asobo, com algumas pequenas modificações e traduções para o Português do Brasil.

Link do Plugin Oficial:
https://github.com/AsoboStudio/glTF-Blender-IO-MSFS

Este plugin desbloqueia o recurso **Emissive Color** resposável por gerar Light Bloom ou Glow ao qual reproduz os efeitos de iluminação do mundo real. O efeito bloom funciona aplicando um filtro na imagem que aumenta o brilho das partes mais claras e cria um borrão nas bordas. Isso faz com que a luz pareça mais intensa e difusa, como acontece na vida real quando olhamos para uma fonte de luz muito forte

# Como utilizar o efeito Bloom ao gear o gLTF para a SDK

Em "MSFS Material Params" como na imagem abaixo, selecione "Emissive Color" e aumente seu valor para 1, esse é o valor máximo de emissão, observe que agora o objeto passa a emitir a iluminação brilhando no escuro, mas ele ainda não emite o Bloom.

https://github.com/git-exahost/glTF-Blender-IO-MSFS/blob/main/misc/EmissionStrength.jpg

Para adicionar o efeito Bloom, procure por "Emission Strength" nos parametores de superficie, clique em cima e procure por "vincular", clique em "desconectar" veja que agora é possível adicionar valores ao "Emission Strength" como demostrado na imagem abaixo, os valores adicionados a este item geram o efeito Bloom, fique a vontade para testar diversos valores.

https://github.com/git-exahost/glTF-Blender-IO-MSFS/blob/main/misc/MSFSMaterialParams.jpg

Para ver o resultado do efeito Bloom no blender sem ter que compilar e gerar o gLTF, va em "Pender Propiets" e marque o item "Reluzir" como na imagem abaixo:

https://github.com/git-exahost/glTF-Blender-IO-MSFS/blob/main/misc/Reluzir.jpg

#### Para instalar o plugin do Blender, siga estes passos simples:

Esta versão é compatível com o **Blender 3.4**. Instale o **Blender 3.3.3** utilizando o link abaixo:<br>
https://www.blender.org/download/releases/3-4/

### Instalação

1. Feche o Blender;<br>
2. Baixe o arquivo **glTF-Blender-IO-MSFS** clicando em **Releases** em seguida clicando em **glTF-Blender-IO-MSFS.zip**;
3. Descompact o Zip baixado na pasta **C:\Users\seu usuario\AppData\Roaming\Blender Foundation\Blender\3.0\scripts\addons** ou globalmente em **C:\Program Files\Blender Foundation\Blender 3.3\3.3\scripts\addons**; pode subistituir todos os arquivos do  **io_scene_gltf2**.

  Depois de concluir o processo descrito acima, inicie o Blender e, em seguida, ative o plugin. A ativação é feita a partir das Preferências do Blender.

**NOTA**: Talvez seja necessário reiniciar o Blender novamente depois de ativar o plug-in para que todas as opções fiquem visíveis no IDE.
