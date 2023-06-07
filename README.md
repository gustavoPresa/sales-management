# Sistema de gerenciamento - Papelaria

### Serviços criados

Para este projeto dois serviços foram criados:

- API Rest para realizar o CRUD de clientes, vendedores, produtos e vendas.
- Aplicação front-end que utiliza os endpoints expostos pela API.

#### API para CRUD de uma papelaria

Endereço: [http://localhost:8000/api/](http://localhost:8000/api/)

#### Dashboard (Aplicação com front-end)

Endereço: [http://localhost:3000/](http://localhost:3000/)

### Endpoints

#### **client/**

- **POST**: Cria um novo cliente.
  `http://localhost:8000/api/client/`

#### **client/{client_id}**

- **GET**: Retorna um cliente.
- **PUT**: Atualiza os dados de um cliente.
- **DELETE**: Remove um cliente.
  `http://localhost:8000/api/client/{client_id}`

#### **commission_report/{from_date}/{to_date}**

- **GET**: Retorna um relatório de comissão por data.
  `http://localhost:8000/api/commission_report/{from_date}/{to_date}`

#### **product/**

- **POST**: Cria um novo produto.
  `http://localhost:8000/api/product/`

#### **product/{product_id}**

- **GET**: Retorna um produto.
- **PUT**: Atualiza os dados de um produto.
- **DELETE**: Remove um produto.
  `http://localhost:8000/api/product/{product_id}`

#### **sale/**

- **POST**: Cria uma nova venda.
  `http://localhost:8000/api/sale/`

#### **sale/{sale_id}**

- **GET**: Retorna uma venda.
- **PUT**: Atualiza os dados de uma venda.
- **DELETE**: Remove uma venda.
  `http://localhost:8000/api/sale/{sale_id}`

#### **seller/**

- **POST**: Cria um novo vendedor.
  `http://localhost:8000/api/seller/`

#### **seller/{seller_id}**

- **GET**: Retorna um vendedor.
- **PUT**: Atualiza os dados de um vendedor.
- **DELETE**: Remove um vendedor.
  `http://localhost:8000/api/seller/{seller_id}`
