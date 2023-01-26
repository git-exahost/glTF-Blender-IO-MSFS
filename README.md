## FlightSim Blender glTF 2.0 Importador e Exportador + Bloom

Este repositório contém uma versão modificada do Microsoft Flight Simulator Blender Import/Export.

Esta versão baseada na versão 1.3.0 do plugin oficial da Asobo com algumas pequenas modificações

Em MSFS Material Params agora é possicel adicionar valores acima de 1 em Emissive Color, podendo ir no item V até 1000.0 gerando o Bloom na iluminação.

Para que este recuso funcione é necessário atualizar o plugin **glTF 2.0 format** utilizando o link abaixo:
<br>
https://github.com/git-exahost/io_scene_gltf2


### Instalação

Para instalar o plugin do Blender, siga estes passos simples:

Esta versão 1.3.x é compatível com o Blender 3.3.x e inferior. Isso não funcionará com o Blender 3.4 e superior.

1. Feche o Blender se você o tiver aberto;<br>
2. Baixe o arquivo **glTF-Blender-IO-MSFS** clicando no icone **<> Code** em seguida clicando em **Download ZIP**;
3. Abra o Zip baixado e selecione todos os arquivos, em seguida, copie-a para a área de transferência ;
4. Agora navegue até a pasta **%AppData%\Blender Foundation\Blender\3.3\scripts\addons**, crie a pasta **io_scene_gltf2_msfs** e cole todos os arquivos nesta pasta;

  Depois de concluir o processo descrito acima, você precisará iniciar o Blender e, em seguida, ativar o plugin. A ativação é feita a partir das Preferências do Blender.

**NOTA**: Talvez seja necessário reiniciar o Blender novamente depois de ativar o plug-in para que todas as opções fiquem visíveis no IDE.
