![PYTHON ](https://img.shields.io/badge/-PYTHON-red)
![HTML](https://img.shields.io/badge/-HTML-orange)
![CSS](https://img.shields.io/badge/-CSS-blue)
![JavaScript](https://img.shields.io/badge/-JavaScript-yellow)
![MicroPython](https://img.shields.io/badge/-MicroPython-000000?style=for-the-badge&logo=python)
![ESP32](https://img.shields.io/badge/-ESP32-000000?style=for-the-badge&logo=espressif)
![Telegram API](https://img.shields.io/badge/-Telegram%20API-0088cc?style=for-the-badge&logo=telegram)
![Flask](https://img.shields.io/badge/-Flask-000000?style=for-the-badge&logo=flask)
![CORS](https://img.shields.io/badge/-CORS-ff6600?style=for-the-badge&logo=security)
![Sensor de Presença](https://img.shields.io/badge/-Sensor%20de%20Presen%C3%A7a-0078D4?style=for-the-badge&logo=sensors)






Monitoramento de Presença e Notificações via IoT
Descrição do Projeto
Este projeto tem como objetivo o desenvolvimento de um sistema de monitoramento de presença utilizando a tecnologia de Internet das Coisas (IoT). O sistema utiliza um microcontrolador ESP32 e um sensor de presença PIR para monitorar a presença de pessoas em uma sala específica durante um horário delimitado. Caso não haja movimentação por um período determinado, o sistema envia uma notificação via Telegram para alertar um responsável, facilitando o controle do uso de equipamentos eletrônicos como luzes, ar condicionado e computadores, contribuindo para a eficiência energética.

Funcionalidades
Detecção de Movimento: O sensor PIR detecta a presença de movimento na sala.
Notificação Automática: Se não houver movimento por um determinado tempo (4 minutos), o sistema envia uma mensagem automática via Telegram.
Horário de Funcionamento: O sistema opera entre 18h40 e 23h00 de segunda a sexta-feira.
Controle de Equipamentos: O objetivo é evitar o desperdício de energia ao desligar equipamentos quando não houver pessoas na sala.
Tecnologias Utilizadas
ESP32: Microcontrolador com conectividade Wi-Fi, responsável pelo controle do sensor PIR e comunicação com a API do Telegram.
Sensor PIR: Detecta movimento na sala monitorada.
MicroPython: Linguagem utilizada para programar o ESP32.
Telegram API: Envio de notificações quando não há movimento na sala.
Flask: Framework utilizado para desenvolver o front-end da aplicação.
Bottle: Framework utilizado para exibir informações e interagir com o sistema de forma simples.
NTP: Servidor para ajustar a hora local do ESP32.
Objetivos
Eficiência Energética: Garantir que os equipamentos eletrônicos sejam desligados quando não houver pessoas na sala, ajudando a reduzir o desperdício de energia.
Gestão Inteligente de Recursos: Monitoramento contínuo e remoto dos recursos dentro da instituição.
Automação: O envio automático de mensagens permite uma gestão eficiente sem a necessidade de intervenção manual constante.
