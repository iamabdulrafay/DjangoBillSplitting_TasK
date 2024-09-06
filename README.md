Certainly! Here’s a `README.md` formatted for your Bill Splitting API:

---

# Bill Splitting API

Welcome to the Bill Splitting API! This API provides endpoints to handle various bill splitting scenarios, including even and uneven splits, incorporating tips and taxes, applying discounts, and managing shared items. Below is a comprehensive guide on how to use each endpoint.

## Table of Contents

- [Endpoints](#endpoints)
  - [1. Basic Bill Splitting](#1-basic-bill-splitting)
  - [2. Uneven Bill Splitting](#2-uneven-bill-splitting)
  - [3. Including Tip and Tax](#3-including-tip-and-tax)
  - [4. Handling Discounts](#4-handling-discounts)
  - [5. Advanced Bill Splitting with Shared Items](#5-advanced-bill-splitting-with-shared-items)
- [Usage Examples](#usage-examples)

## Endpoints

### 1. Basic Bill Splitting

**Endpoint:** `/basic-splitting`  
**Method:** `POST`  
**Description:** Splits a bill evenly among a group of users.

**Request Body:**
```json
{
    "user_ids": ["user1", "user2", "user3"],
    "price": 1200
}
```

**Response:**
```json
{
    "split": 400
}
```

### 2. Uneven Bill Splitting

**Endpoint:** `/unevenly-splitting`  
**Method:** `POST`  
**Description:** Splits a bill unevenly based on individual contributions.

**Request Body:**
```json
{
    "details": [
        {
            "name": "Rohan",
            "amount": 1500
        },
        {
            "name": "Aisha",
            "amount": 2000
        }
    ],
    "total_price": 3500
}
```

**Response:**
```json
{
    "Rohan": {
        "unevenly_pay": 1500,
        "due": 250.0
    },
    "Aisha": {
        "unevenly_pay": 2000,
        "payable": 250.0
    },
    "total_price": 3500,
    "evenly_contribution": 1750.0
}
```

### 3. Including Tip and Tax

**Endpoint:** `/split-including-tip-tax`  
**Method:** `POST`  
**Description:** Splits a bill including tip and tax evenly among users.

**Request Body:**
```json
{
    "user_ids": ["user1", "user2", "user3"],
    "total_amount": 1200,
    "tax_percentage": "16%",
    "tip_percentage": "2%"
}
```

**Response:**
```json
{
    "total_amount": 1200,
    "tip_percentage": "2%",
    "tax_percentage": "16%",
    "user1": {
        "net_amount": 400.0,
        "tip": 8.0,
        "tax": 64.0,
        "total_value": 472.0
    },
    "user2": {
        "net_amount": 400.0,
        "tip": 8.0,
        "tax": 64.0,
        "total_value": 472.0
    },
    "user3": {
        "net_amount": 400.0,
        "tip": 8.0,
        "tax": 64.0,
        "total_value": 472.0
    }
}
```

### 4. Handling Discounts

**Endpoint:** `/split-with-discount`  
**Method:** `POST`  
**Description:** Applies a discount to the total bill before splitting it evenly among users.

**Request Body:**
```json
{
    "user_ids": ["user1", "user2", "user3"],
    "total_amount": 1200,
    "discount_percentage": "10%"
}
```

**Response:**
```json
{
    "total_amount": 1200,
    "discount_percentage": "10%",
    "user1": {
        "net_amount": 400.0,
        "discount": 40.0,
        "total_amount": 360.0
    },
    "user2": {
        "net_amount": 400.0,
        "discount": 40.0,
        "total_amount": 360.0
    },
    "user3": {
        "net_amount": 400.0,
        "discount": 40.0,
        "total_amount": 360.0
    }
}
```

### 5. Advanced Bill Splitting with Shared Items

**Endpoint:** `/bill-splitting`  
**Method:** `POST`  
**Description:** Splits a bill where some items are shared among certain users.

**Request Body:**
```json
{
    "user_ids": [
        "user1",
        "user2",
        "user3",
        "user4",
        "user5",
        "user6",
        "user7",
        "user8",
        "user9",
        "user10"
    ],
    "items": [
        {
            "name": "dim_sum",
            "price": 120
        },
        {
            "name": "spring_rolls",
            "price": 80
        },
        {
            "name": "sweet_and_sour_chicken",
            "price": 300
        },
        {
            "name": "kung_pao_chicken",
            "price": 250
        },
        {
            "name": "fried_rice",
            "price": 150
        },
        {
            "name": "noodles",
            "price": 200
        },
        {
            "name": "hot_and_sour_soup",
            "price": 100
        },
        {
            "name": "egg_foo_yung",
            "price": 130
        },
        {
            "name": "beef_broccoli",
            "price": 350
        },
        {
            "name": "mongolian_beef",
            "price": 280
        }
    ],
    "shared_items": {
        "dim_sum": [
            "user1",
            "user2",
            "user3",
            "user4"
        ],
        "spring_rolls": [
            "user2",
            "user5",
            "user6"
        ],
        "sweet_and_sour_chicken": [
            "user3",
            "user7",
            "user8",
            "user9"
        ],
        "kung_pao_chicken": [
            "user4",
            "user5",
            "user6",
            "user10"
        ],
        "fried_rice": [
            "user1",
            "user7",
            "user8"
        ],
        "noodles": [
            "user2",
            "user3",
            "user5",
            "user10"
        ],
        "hot_and_sour_soup": [
            "user6",
            "user7",
            "user9",
            "user10"
        ],
        "egg_foo_yung": [
            "user1",
            "user3",
            "user6"
        ],
        "beef_broccoli": [
            "user8",
            "user9",
            "user10"
        ],
        "mongolian_beef": [
            "user4",
            "user5",
            "user8"
        ]
    }
}
```
**Respone **
```json
{
    "user_ids": [
        "user1",
        "user2",
        "user3",
        "user4",
        "user5",
        "user6",
        "user7",
        "user8",
        "user9",
        "user10"
    ],
    "item": [
        {
            "name": "dim_sum",
            "price": 120
        },
        {
            "name": "spring_rolls",
            "price": 80
        },
        {
            "name": "sweet_and_sour_chicken",
            "price": 300
        },
        {
            "name": "kung_pao_chicken",
            "price": 250
        },
        {
            "name": "fried_rice",
            "price": 150
        },
        {
            "name": "noodles",
            "price": 200
        },
        {
            "name": "hot_and_sour_soup",
            "price": 100
        },
        {
            "name": "egg_foo_yung",
            "price": 130
        },
        {
            "name": "beef_broccoli",
            "price": 350
        },
        {
            "name": "mongolian_beef",
            "price": 280
        }
    ],
    "shared_items": {
        "dim_sum": [
            "user1",
            "user2",
            "user3",
            "user4"
        ],
        "spring_rolls": [
            "user2",
            "user5",
            "user6"
        ],
        "sweet_and_sour_chicken": [
            "user3",
            "user7",
            "user8",
            "user9"
        ],
        "kung_pao_chicken": [
            "user4",
            "user5",
            "user6",
            "user10"
        ],
        "fried_rice": [
            "user1",
            "user7",
            "user8"
        ],
        "noodles": [
            "user2",
            "user3",
            "user5",
            "user10"
        ],
        "hot_and_sour_soup": [
            "user6",
            "user7",
            "user9",
            "user10"
        ],
        "egg_foo_yung": [
            "user1",
            "user3",
            "user6"
        ],
        "beef_broccoli": [
            "user8",
            "user9",
            "user10"
        ],
        "mongolian_beef": [
            "user4",
            "user5",
            "user8"
        ]
    },
    "per_person_bill": {
        "user1": {
            "dim_sum": 30.0,
            "fried_rice": 50.0,
            "egg_foo_yung": 43.333333333333336,
            "discount": 12.333333333333336,
            "tip": 2.466666666666667,
            "total_amount": 133
        },
        "user2": {
            "dim_sum": 30.0,
            "spring_rolls": 26.666666666666668,
            "noodles": 50.0,
            "discount": 10.666666666666668,
            "tip": 2.1333333333333333,
            "total_amount": 115
        },
        "user3": {
            "dim_sum": 30.0,
            "sweet_and_sour_chicken": 75.0,
            "noodles": 50.0,
            "egg_foo_yung": 43.333333333333336,
            "discount": 19.833333333333336,
            "tip": 3.966666666666667,
            "total_amount": 214
        },
        "user4": {
            "dim_sum": 30.0,
            "kung_pao_chicken": 62.5,
            "mongolian_beef": 93.33333333333333,
            "discount": 18.583333333333332,
            "tip": 3.7166666666666663,
            "total_amount": 200
        },
        "user5": {
            "spring_rolls": 26.666666666666668,
            "kung_pao_chicken": 62.5,
            "noodles": 50.0,
            "mongolian_beef": 93.33333333333333,
            "discount": 23.25,
            "tip": 4.65,
            "total_amount": 251
        },
        "user6": {
            "spring_rolls": 26.666666666666668,
            "kung_pao_chicken": 62.5,
            "hot_and_sour_soup": 25.0,
            "egg_foo_yung": 43.333333333333336,
            "discount": 15.75,
            "tip": 3.15,
            "total_amount": 170
        },
        "user7": {
            "sweet_and_sour_chicken": 75.0,
            "fried_rice": 50.0,
            "hot_and_sour_soup": 25.0,
            "discount": 15.0,
            "tip": 3.0,
            "total_amount": 162
        },
        "user8": {
            "sweet_and_sour_chicken": 75.0,
            "fried_rice": 50.0,
            "beef_broccoli": 116.66666666666667,
            "mongolian_beef": 93.33333333333333,
            "discount": 33.5,
            "tip": 6.7,
            "total_amount": 361
        },
        "user9": {
            "sweet_and_sour_chicken": 75.0,
            "hot_and_sour_soup": 25.0,
            "beef_broccoli": 116.66666666666667,
            "discount": 21.66666666666667,
            "tip": 4.333333333333334,
            "total_amount": 234
        },
        "user10": {
            "kung_pao_chicken": 62.5,
            "noodles": 50.0,
            "hot_and_sour_soup": 25.0,
            "beef_broccoli": 116.66666666666667,
            "discount": 25.41666666666667,
            "tip": 5.083333333333334,
            "total_amount": 274
        }
    },
    "net_amount": 1960,
    "discount": "10%",
    "tip": "2%",
    "tax": "16% ",
    "total_amount": 2087
}

```
