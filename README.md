# Projeto para disciplina de Computação Gráfica - 2024.1

**Estudantes:** Geisianny Bernardo e Nicoly Lana

## 🚀 Descrição do Projeto: Pêndulo

Este projeto é uma simulação visual de um pêndulo, desenvolvida utilizando **OpenGL** e **Pygame**. O pêndulo é representado por uma esfera suspensa por uma linha, que se movimenta de acordo com as leis da física, simulando o movimento de oscilação. A estrutura de suporte do pêndulo é composta por cilindros, proporcionando uma visualização 3D detalhada.

### 🎨 Funcionalidades

- **Movimentação do Pêndulo:** A simulação considera a gravidade, o comprimento do pêndulo, a velocidade angular e o amortecimento.
- **Texturização:** Texturas são aplicadas à base e à esfera do pêndulo, enriquecendo a experiência visual.
- **Iluminação:** A cena conta com múltiplas fontes de luz, melhorando o realismo e a percepção de profundidade.
- **Movimentação da Câmera:** Permite ao usuário explorar a cena sob diferentes ângulos e distâncias.
- **Controle de Velocidade:** O usuário pode aumentar ou diminuir a velocidade do movimento do pêndulo utilizando teclas específicas.

### ⚙️ Tecnologias Utilizadas

- **Python**
- **Pygame** para manipulação de gráficos e eventos
- **OpenGL** para renderização 3D

### 📦 Instalação

Siga os passos abaixo para configurar o projeto:

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```
   
2. **Navegue até o diretório do projeto:**
    ```bash
    cd <NOME_DA_PASTA>
    ```

3. **Instale as dependências necessárias:**
    ```bash
    pip install pygame PyOpenGL numpy
    ```

4. **Execute o projeto:**
    ```bash
    python nome_do_arquivo.py
    ```

## 🎮 Controles

- **Setas direcionais:** Rotacionar a câmera.
- **Tecla W:** Aproximar a câmera.
- **Tecla S:** Afastar a câmera.
- **Tecla + (igual):** Aumentar o ângulo do movimento do pêndulo para a direita (frente).
- **Tecla - (menos):** Diminuir o ângulo do movimento do pêndulo para a esquerda(atrás).
- **Tecla Esc:** Sair da simulação.

