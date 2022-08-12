
## Sarah Gilbert

Sarah Gilbert is an app to create Customers, Orders and Products

## Run Locally

Clone the project

```bash
  git clone git@github.com:thaisbighetti/construdelas.git
```

Run Web

```bash
  docker compose up web
```

Run Tests
```bash
  docker compose run tests
```
## API Reference

#### Orders

```http
  GET/LIST /order/
  POST /order/
  GET/DELETE /order/{id}

```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `string` | `order id`|

#### Products

```http
  GET/LIST /product/
  POST /product/
  GET/PATCH /product/{id}

```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `string` | `product id`|


####  Order Detail
```http
  GET/LIST /order-detail/
  GET/RETRIEVE /order-detail/{id}

```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `string` | `order detail id`|

#### Customer

```http
  GET/LIST /customer/
  POST /customer/
  GET/PATCH /customer/{id}

```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `string` | `customer id`|