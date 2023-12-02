# Day 1

## 第一題

### 問題理解

給定 input，input 由很多字串組合而成，並以分行符號分隔。
每個字串的第一個數字乘以 10 加上最後一個數字組合起來會是那一個字串的數字。
將所有數字都加總起來就會是最後的答案。

### 解法

使用雙指針的技巧，從頭跟尾開始索引，並往中間收斂，只要遇到數字就固定指針，直到兩邊的指針都固定，就計算並回傳。

```python
def calculate(line):
    front_idx = 0
    end_idx = len(line) - 1
    front = -1
    end = -1
    while front == -1 or end == -1:
        if line[front_idx].isdigit():
            front = int(line[front_idx])
        else:
            front_idx += 1

        if line[end_idx].isdigit():
            end = int(line[end_idx])
        else:
            end_idx -= 1
    return 10 * front + end
```

## 第二題

### 問題理解

延續第一題，但字串中 1 ~ 9 的英文：像是 "one"、"two"，也應該被視為數字，因此需要多添加一個匹配的機制。

### 解法

針對匹配，先使用正規表達式查看所有可以被轉換成數字的結果，並記錄在一個 dict 中，
鍵是匹配到的字串的開頭索引（如：1），而值是轉換後的結果（如：9）。

只記錄開頭索引是因為，兩個可以轉換成數字的字串是不可能使用同一個開頭索引的。

```python
import re

def str_to_int(line: str):
    find_indexs = {}
    for k, v in mapper.items():
        results = re.finditer(k, line)
        for r in results:
            start, _ = r.span()
            find_indexs[start] = v
    return find_indexs
```

以"nineoneight"這段來說，經轉換後的結果會是 {0: 9, 4: 1, 6: 8}。

之後只要在上一題的基礎上加上判斷就可以了（查看註解 Add this 的部分）

```python
def calculate(line):
    front_idx = 0
    end_idx = len(line) - 1
    front = -1
    end = -1
    # Add this
    find_indexs = str_to_int(line)
    while front == -1 or end == -1:
        # Add this
        if front_idx in find_indexs:
            front = find_indexs[front_idx]
        elif line[front_idx].isdigit():
            front = int(line[front_idx])
        else:
            front_idx += 1

        # Add this
        if end_idx in find_indexs:
            end = find_indexs[end_idx]
        elif line[end_idx].isdigit():
            end = int(line[end_idx])
        else:
            end_idx -= 1
    return 10 * front + end
```
