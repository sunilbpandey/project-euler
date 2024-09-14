# Project Euler

Solutions to [Project Euler](https://projecteuler.net) problems.

![Go](https://github.com/sunilbpandey/project-euler/actions/workflows/go.yml/badge.svg)
![Python](https://github.com/sunilbpandey/project-euler/actions/workflows/python.yml/badge.svg)
![TypeScript](https://github.com/sunilbpandey/project-euler/actions/workflows/typescript.yml/badge.svg)

## Progress

|                |                |                |                |                |                |                |                |                |                 |
| -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | --------------- |
| [1](src/P001)  | [2](src/P002)  | [3](src/P003)  | [4](src/P004)  | [5](src/P005)  | [6](src/P006)  | [7](src/P007)  | [8](src/P008)  | [9](src/P009)  | [10](src/P010)  |
| [11](src/P011) | [12](src/P012) | [13](src/P013) | [14](src/P014) | [15](src/P015) | [16](src/P016) | [17](src/P017) | [18](src/P018) | [19](src/P019) | [20](src/P020)  |
| [21](src/P021) | [22](src/P022) | [23](src/P023) | [24](src/P024) | [25](src/P025) | [26](src/P026) | [27](src/P027) | [28](src/P028) | [29](src/P029) | [30](src/P030)  |
| [31](src/P031) | [32](src/P032) | [33](src/P033) | [34](src/P034) | [35](src/P035) | [36](src/P036) | [37](src/P037) | [38](src/P038) | [39](src/P039) | [40](src/P040)  |
| [41](src/P041) | [42](src/P042) | [43](src/P043) | [44](src/P044) | [45](src/P045) | [46](src/P046) | [47](src/P047) | [48](src/P048) | [49](src/P049) | [50](src/P050)  |
| [51](src/P051) | [52](src/P052) | [53](src/P053) | [54](src/P054) | [55](src/P055) | [56](src/P056) | [57](src/P057) | [58](src/P058) | [59](src/P059) | [60](src/P060)  |
| [61](src/P061) | [62](src/P062) | [63](src/P063) | [64](src/P064) | [65](src/P065) | [66](src/P066) | [67](src/P067) | [68](src/P068) | [69](src/P069) | [70](src/P070)  |
| [71](src/P071) | [72](src/P072) | [73](src/P073) | [74](src/P074) | [75](src/P075) | [76](src/P076) | [77](src/P077) | [78](src/P078) | [79](src/P079) | [80](src/P080)  |
| [81](src/P081) | [82](src/P082) | [83](src/P083) | [84](src/P084) | [85](src/P085) | [86](src/P086) | [87](src/P087) | [88](src/P088) | [89](src/P089) | [90](src/P090)  |
| [91](src/P091) | [92](src/P092) | [93](src/P093) | [94](src/P094) | [95](src/P095) | [96](src/P096) | [97](src/P097) | [98](src/P098) | [99](src/P099) | [100](src/P100) |

|            |                                       |
| ---------- | ------------------------------------- |
| Go         | 🟩🟩🟩🟩🟩🟩⬜️⬜️⬜️⬜️ (60/100)   |
| Haskell    | 🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ (18/100)   |
| Python     | 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 (100/100)        |
| TypeScript | 🟩🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ (25/100) |

## Usage

### Go

#### Run all tests

```
go test -v ./src/tests
```

### Haskell

#### Solve a specific problem

```
runhaskell -isrc src/Main <PROBLEM>
```

### Python

#### [Optional] Create and activate a virtual environment

```
mkdir .venv
python3 -m venv .venv/euler
source .venv/euler/activate
```

#### Install dependencies

```
pip install -r pip_requirements.txt
```

#### Run all tests

```
pytest -v
```

### TypeScript

#### Install dependencies

```
npm install
```

#### Solve a specific problem

```
npm start --silent <PROBLEM>
```

e.g.

```
npm start --silent 12
```

#### Run all tests

```
npm test
```
