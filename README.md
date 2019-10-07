# Prime factors - Challenge

## Challenge

> Todo número inteiro positivo pode ser representado pelo produto de potências de números primos (os chamados fatores primos).
> Por exemplo o número 6 pode ser representado pelo produto do números primos 2 x 3.
> Outros exemplos:


    5 = 5 (números primos só tem um fator primo - ele mesmo)

    100 = 2 x 2 x 5 x 5

    198 = 2 x 3 x 3 x 11

    276 = 2 x 2 x 3 x 23


> Desenvolva um programa que dado um número inteiro positivo, retorne os seus fatores primos em uma lista


## How Run

Follow this simple steps:

1. `git clone https://github.com/vinimmelo/prime-factors-challenge.git`
2. `cd prime-factors-challenge`
3. `python3 -m virtualenv venv`
4. `source venv/bin/activate` [May change in Windows environment]
5. `pip install -r requirements.txt`
6. `python main.py <number>` Example: `python main.py 100`

## Unit Test

if you wan't to test all the expected cases, just run:

- `pytest unit_test`


## Author

- **Vinícius Melo**

## License

Project based under the terms of the license MIT, see the file [LICENSE.md](https://github.com/vinimmelo/prime-factors-challenge/blob/master/LICENSE) to more details.