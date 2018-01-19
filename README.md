# Python RSA

Barebones Python implementation of the RSA algorithm for public key cryptography with related functionality like key-generation

## Getting Started

In order to get startet clone this Repository or just download main.py. Then start a python3 live session and import main.

```
import main
```

### Prerequisites

Python3 + random library

## Usage

In order to generate a Private and a Public Key simply use auto_key or the key_generator:

```
Private, Public=auto_key(1024)
```

or

```
Private, Public = key_generator(13,17)
```

Messages are created as lists of numbers, the crypt function takes a string with a key and turns it into an encrypted list of numbers:

```
encoded_message=crypt(Public,'Message')
```

if a list of numbers is given a decoded string is instead being created:

```
decoded_message=crypt(Private,encoded_message)
```

### Example
```
Key=[14213, 2203]
encoded_message=[1703, 2461, 11878, 7626, 14147, 13263, 573, 14107, 5026, 5819, 5122, 440, 5917, 1406, 5866, 4771, 13630, 11711, 3439, 13581, 11793, 1787]
crypt(Key,encoded_message,16)
```

## Please consider

This Project was made by one Person in one day, who is not very good at programming, as a fun exercise. Best practices for Key-generation like choosing Prime numbers far appart enough or public keys small enough though not to small have not yet been implemented and may never be. If anyone however would like to do so please feel free to do with this code whatever you'd like to :)

