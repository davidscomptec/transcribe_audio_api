
# API - Transcricao

API de transcrição de áudio protegida por autenticação JWT via **AuthAPI** (serviço externo de autenticação).

Esta aplicação é responsável exclusivamente pelo processamento de transcrição, delegando autenticação e autorização para um serviço dedicado.

Api não está em produção, pois, para ser hospedada precisaria de um servidor virtual ou dedicado.

----------

# Arquitetura

A aplicação segue arquitetura em camadas:

API-Transcricao/  
│  
├── config/                # Configurações e variáveis de ambiente  
│   └── env.py  
│  
├── models/                # Modelos de domínio  
│   ├── auth.py  
│   └── transcribe.py  
│  
├── router/                # Camada HTTP (controllers)  
│   └── transcribe_controller.py  
│  
├── service/               # Regras de negócio  
│   ├── auth_service.py  
│   └── transcricao_service.py  
│  
├── app.py  
├── requirements.txt  
├── vercel.json  
└── .env

----------

# Integração com AuthAPI

Esta API:

-   Recebe o JWT no header `Authorization`
    
-   Permite acesso somente a usuários autenticados
    

Exemplo de header:

Authorization: Bearer <seu_token_jwt>

A autenticação não é feita localmente — o token deve ser emitido previamente pela AuthAPI.

----------

# Getting Started

## 1. Requisitos

-   Python 3.11
    
-   pip
    
-   virtualenv (recomendado)
    

----------

## 2. Ambiente Virtual

python -m venv venv  
venv\Scripts\activate

----------

## 3. Instalar Dependências

pip install -r requirements.txt

----------

## 4. Variáveis de Ambiente

Crie um `.env` na raiz:

AUTH_API_URL=https://api-scomptec-auth.vercel.app/

----------

## Como Rodar

uvicorn app:app --reload

Disponível em:

http://127.0.0.1:8000

----------

# Documentação Automática

-   Swagger:
    
    http://127.0.0.1:8000/
    
-   ReDoc:
    
    http://127.0.0.1:8000/redoc
    

----------

# Fluxo de Autorização

1.  Cliente autentica na **AuthAPI**
    
2.  Recebe JWT válido
    
3.  Envia requisição para `/transcribe`
    
4.  API valida o token, chamando a própria AuthAPI
    
5.  Se válido → processa transcrição
    
6.  Se inválido → retorna `401 Unauthorized`
    

----------

# Deploy (Vercel)  
  
O projeto inclui configuração `vercel.json`.  
  
Basta subir em um repositório privado/público do GitHub, fazer login com o GitHub na plataforma Vercel adicionar novo projeto e selecionar o repo. O Deploy é refeito automaticamente a cada push no repositório remoto.  
  
### ⚠ Observações Importantes  
  
- A Vercel executa Python como **Serverless Functions**  
  - Não há suporte a processos persistentes (ex: schedulers contínuos)  
      
- Variáveis de ambiente devem ser configuradas no painel da Vercel

----------

# Segurança

-   Autenticação baseada em JWT
    
-   Validação de assinatura
    
-   Isolamento de responsabilidades (Auth separado da Transcrição)
    
-   Uso de variáveis de ambiente
    

----------

# A fazer (sugestões)

-   Controle de permissões por role
    
-   Rate limiting
    
-   Logs estruturados
    
-   Testes automatizados
    
-   Docker support
    
-   Cache de validação de token