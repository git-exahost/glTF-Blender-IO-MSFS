## FlightSim Blender glTF 2.0 Importador e Exportador + Bloom

Este repositório apresenta uma versão aprimorada do plugin de importação/exportação do Microsoft Flight Simulator para o Blender, baseada na versão 1.3.2 do plugin oficial da Asobo. Foram realizadas algumas modificações e traduções para o Português do Brasil.

Link para o Plugin Oficial:
[https://github.com/AsoboStudio/glTF-Blender-IO-MSFS](https://github.com/AsoboStudio/glTF-Blender-IO-MSFS)

Este plugin desbloqueia a funcionalidade **Emissive Color**, responsável por gerar o efeito Light Bloom ou Glow, reproduzindo os efeitos de iluminação do mundo real. O efeito Bloom trabalha aplicando um filtro na imagem, aumentando o brilho das áreas mais claras e criando um borrão nas bordas. Isso resulta em uma luz mais intensa e difusa, semelhante ao que ocorre na vida real ao olhar para uma fonte de luz muito forte.

#### Como utilizar o efeito Bloom ao gear o gLTF para a SDK

No painel **MSFS Material Params**, conforme ilustrado na imagem abaixo, selecione a opção **Emissive Color** e ajuste o seu valor para **1**. Este representa o valor máximo de emissão. Observe que o objeto agora emite iluminação, brilhando no escuro, embora o efeito Bloom ainda não esteja ativo.

![MSFS Material Params](https://github.com/git-exahost/glTF-Blender-IO-MSFS/blob/main/misc/MSFSMaterialParams.jpg)

Para incorporar o efeito Bloom, navegue até **General Parameters** e ajuste o parâmetro **Emissive Scale**, adicionando valores acima de 1. Quanto maior o valor, mais intensa será a emissão luminosa. Os valores adicionados serão multiplicados pelo **Emissive Color** definido, resultando no efeito Bloom desejado. Sinta-se à vontade para experimentar diferentes valores.

![Emission Strengths](https://github.com/git-exahost/glTF-Blender-IO-MSFS/blob/main/misc/GeneralParameters.jpg)

Para visualizar o resultado do efeito Bloom no Blender sem a necessidade de compilar ou gerar o gLTF, vá até **Render Properties** e marque a opção **Reluzir**, conforme apresentado na imagem abaixo:

![Reluzir](https://raw.githubusercontent.com/git-exahost/glTF-Blender-IO-MSFS/main/misc/Reluzir.jpg) 

#### Guia de Instalação do Plugin Blender

Esta versão é projetada para compatibilidade com o **Blender 3.6.4** e o **Blender 4.0**. Certifique-se de ter o **Blender 3.6.4** ou **Blender 4.0** instalado, utilizando o link abaixo:<br>
[Download Blender 3.6.4](https://www.blender.org/download/lts/3-6/)
[Download Blender 4.0](https://www.blender.org/download/lts/4.0/)

### Instruções de Instalação

1. Certifique-se de que o Blender está fechado.
2. Faça o download do arquivo **glTF-Blender-IO-MSFS** clicando em **Releases** e, em seguida, clique em **glTF-Blender-IO-MSFS.zip**.
3. Extraia o conteúdo do arquivo ZIP na seguinte pasta: **C:\Users\seu usuário\AppData\Roaming\Blender Foundation\Blender\3.6\scripts\addons**, ou, de forma global, em **C:\Program Files\Blender Foundation\Blender 3.6\3.6\scripts\addons**.
