# myBlockchain
This project is a simple implementation of a blockchain using Python. It demonstrates the basic concepts of a blockchain, including blocks and hashing. It will give youa brief idea of how blockchain works and how blocks are added to a blockchain.

## Features
- Creates a simple blockchain with blocks containing data current hash and previous block's hash.
- Uses SHA-256 hashing algorithm from the hashlib library.
- Has a genesis block (first block of any blockchain).

## Requirements
- Python 3.6 or higher

## Usage
1. Clone the repository:

    ```
    git clone https://github.com/harshupanghal/myBlockchain.git
    ```

2. Navigate to the project directory:

    ```
    cd myBlockchain
    ```

3. Run the Python program:

    ```
    python Blockchain.py
    ```

4. Follow the instructions in the terminal to interact with the blockchain.


## Implementation Details
- The blockchain consists of blocks, where each block contains data, current hash and previous block's hash.
- The hash of each block is calculated using the SHA-256 hashing algorithm from the hashlib library.
- When a new block is added to the blockchain, its hash is computed based on the previous block's hash and the new block's data.
- The blockchain also has a genesis block.


## You can further add more features in it like
- Take input of data from user.
- Validate every hash.
- Try out some more features and functionalities.
