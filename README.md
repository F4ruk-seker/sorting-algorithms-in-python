
# Algorith TestCases and Results

```
Algorithm run (BubbleSort)
| TEST-CASE:|  [33, 97, 37, 70, 91, 23, 42, 38, 35, 76, 46, 20, 30, 67, 4, 45, 54, 36, 39, 88, 72, 92, 17, 84, 38]
|   RESULT: |  [4, 17, 20, 23, 30, 33, 35, 36, 37, 38, 38, 39, 42, 45, 46, 54, 67, 70, 72, 76, 84, 88, 91, 92, 97]
.................................................................................................................................
Algorithm run (SelectionSort)
| TEST-CASE:|  [140, 41, 21, 158, 93, 102, 95, 135, 122, 120, 85, 56, 78, 11, 12, 44, 190, 107, 44, 131, 54, 32, 178, 122, 139]
|   RESULT: |  [11, 12, 21, 32, 41, 44, 44, 54, 56, 78, 85, 93, 95, 102, 107, 120, 122, 122, 131, 135, 139, 140, 158, 178, 190]
.................................................................................................................................
Algorithm run (InsertionSort)
| TEST-CASE:|  [184, 33, 82, 124, 138, 53, 135, 97, 97, 144, 200, 71, 84, 0, 63, 132, 139, 58, 187, 122, 158, 80, 173, 120, 76]
|   RESULT: |  [200, 187, 184, 173, 158, 144, 139, 138, 135, 132, 124, 122, 120, 97, 97, 84, 82, 80, 76, 71, 63, 58, 53, 33, 0]
.................................................................................................................................
```

# Algorithm Performance Results

| Algorithm      | Test Param Count | Time (seconds) | Memory Used (MB) |
|----------------|------------------|----------------|-------------------|
| BubbleSort     | 1,000            | 0.09           | 0.43              |
| SelectionSort  | 1,000            | 0.02           | 0.0               |
| InsertionSort  | 1,000            | 0.02           | 0.0               |
|----------------|------------------|----------------|-------------------|
| BubbleSort     | 10,000           | 9.52           | 0.75              |
| SelectionSort  | 10,000           | 2.09           | 0.07              |
| InsertionSort  | 10,000           | 1.82           | 0.0               |

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/F4ruk-seker/sorting-algorithms-in-python.git
   cd sorting-algorithms-in-python
   
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Usage 
   ```bash
   python main.py
   ```
