# Uso de apache kafka para extração de dados no twitter em near-real-time

## Executando o projeto

**1° passo: Clone o repositorio com o comando ```git clone https://github.com/Izaiasjun1Dev/kafka_and_python.git```**

**2° passo: com o comando ```cd kafka_and_python``` entre no repositorio do projeto**

**3° passo: com o docker instalado na sua maquina e dentro do repositorio do projeto corra o seguinte comando em seu cmd/terminal ```docker-compose up -d```**

**Com isto você terá em sua maquina um server para teste kafka e seu orquestrador e um pequena interface rodando no endereço http://localhost:19000/**

## Depois disso ainda em seu cmd/terminal no nivel da pasta raiz do projeto vc pode executar o comando ```python src/service/consumer.py && python src/service/producer.py``` aguarde alguns minutos enquanto o cluster kafka é executado!

# And voilá o projeto vai ser iniciado!


# A e não se esquece de dar uma passada na plataforma do twitter para pegar suas proprias chaves de acesso!
