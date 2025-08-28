# 🚗 AutoPrime Dashboard - Análise de Dados de Aluguel de Carros

Este projeto consiste em um dashboard interativo de Business Intelligence desenvolvido para a **AutoPrime**, uma locadora de veículos. O objetivo principal é fornecer insights acionáveis sobre as operações da empresa, com foco especial na análise de descontos e na performance geral da frota e dos clientes.

## ✨ Funcionalidades e Destaques

-   **Visão Geral de KPIs:** Indicadores chave de performance como total de aluguéis, receita total, clientes com desconto, estados atendidos, clientes únicos e taxa de pagamento.
-   **Análise Aprofundada de Descontos:** Seções dedicadas à visualização da distribuição de ofertas de desconto, uma matriz de clientes por tipo de desconto e o impacto financeiro desses programas.
-   **Insights Estratégicos:** Apresentação de conclusões importantes derivadas dos dados, como a distribuição equilibrada dos planos de aluguel, a alta taxa de fidelização de clientes e a manutenção da receita.
-   **Design Moderno e Minimalista:** Interface de usuário com tema escuro, tipografia limpa (Inter), cards com efeitos de glassmorphism e animações sutis, proporcionando uma experiência visual profissional e elegante.
-   **Responsividade:** O dashboard é adaptado para visualização em diferentes tamanhos de tela, desde desktops até dispositivos móveis.

## 🚀 Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando uma combinação de tecnologias para processamento de dados, backend e frontend:
    **SQLite:** Liguagem usada para a extração de Dados do Banco 
-   **Python:** Linguagem principal para a lógica de backend e análise de dados.
    -   `pandas`: Para manipulação e análise de dados.
    -   `matplotlib` e `seaborn`: Para geração de gráficos e visualizações.
    -   `Flask`: Framework web para o desenvolvimento do backend da aplicação, servindo os dados e o frontend.
-   **HTML5:** Estrutura do dashboard.
-   **CSS3:** Estilização e design responsivo, incluindo efeitos modernos como glassmorphism.
-   **JavaScript:** Para interatividade no frontend e consumo da API de dados.

## 💡 O Papel da Inteligência Artificial (Manus)
Para otimizar e acelerar o desenvolvimento deste dashboard, utilizei um Agente de IA (Manus) como a principal ferramenta de desenvolvimento. Após a fase inicial de tratamento de dados com SQL, o Manus foi fundamental e atuou como um co-piloto para:

Criação do Dashboard: O agente de IA gerou toda a estrutura de código em HTML, a estilização em CSS e o JavaScript necessário para a interatividade e para o consumo da API de dados.

Desenvolvimento Frontend: Contribuiu para a implementação do design moderno e responsivo, incluindo a aplicação de estilos e animações.

Otimização de Código: Ajudou a refinar o código para melhor performance e legibilidade, garantindo um resultado final polido e profissional.

Essa colaboração com a IA me permitiu focar mais na estratégia e nos insights de negócio, enquanto o agente cuidava da execução de tarefas complexas de codificação e design, resultando em um processo de desenvolvimento muito mais eficiente e inovador

## 📁 Estrutura do Projeto

```
autoprime_dashboard/
├── src/
│   ├── static/             # Arquivos estáticos (CSS, JS, imagens, gráficos)
│   │   ├── analise_descontos.png
│   │   ├── matriz_clientes_descontos.png
│   │   ├── favicon.ico
│   │   └── index.html      # Frontend do dashboard
│   ├── routes/             # Rotas da API Flask
│   │   └── stats.py        # Endpoint para dados estatísticos
│   └── main.py             # Ponto de entrada da aplicação Flask
├── autprime_data.csv       # Dados de exemplo (anonimizados)
├── create_discount_analysis.py # Script para gerar gráficos de desconto
├── process_data.py         # Script para processar dados brutos
├── README.md               # Este arquivo
└── requirements.txt        # Dependências do Python
```

## ▶️ Como Rodar o Projeto Localmente

Siga os passos abaixo para configurar e executar o dashboard em sua máquina local:

1.  **Clone o Repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd autoprime_dashboard
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: .\venv\Scripts\activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Prepare os Dados:**
    Certifique-se de que o arquivo `autprime_data.csv` esteja na raiz do projeto. Se você tiver o arquivo original `.xlsx`, pode usar o script `process_data.py` para convertê-lo:
    ```bash
    python3 process_data.py
    ```

5.  **Gere os Gráficos (Opcional, se não estiverem presentes):**
    Os gráficos são gerados como imagens PNG. Se eles não estiverem no diretório `src/static/`, execute:
    ```bash
    python3 create_discount_analysis.py
    ```
    E copie-os para `src/static/`:
    ```bash
    cp *.png src/static/
    ```

6.  **Execute a Aplicação Flask:**
    ```bash
    python3 src/main.py
    ```

7.  **Acesse o Dashboard:**
    Abra seu navegador e acesse `http://localhost:5000`.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias, correção de bugs ou novas funcionalidades.

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

