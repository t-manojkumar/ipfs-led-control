# IoT LED Control with Raspberry Pi and IPFS

This project demonstrates how to control an LED connected to a Raspberry Pi using IPFS pub-sub for decentralized messaging. 

## Features
- Remote control of LEDs using IPFS.
- Uses Raspberry Pi GPIO for hardware interaction.
- Fully open-source and beginner-friendly.

## Requirements
- Raspberry Pi Zero 2 W (or any Raspberry Pi model with GPIO pins).
- LED.
- Internet connection.
- Python 3.x.

## Setup Instructions
1. Clone this repository:
   ```
   git clone https://github.com/t-manojkumar/ipfs-led-control.git
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Start IPFS daemon:
   ```
   ipfs daemon --enable-pubsub-experiment
   ```

4. Run the script:
   ```
   python main.py
   ```

5. Control the LED:
   - To turn the LED ON:
     ```
     echo ON | ipfs pubsub pub led-control
     ```
   - To turn the LED OFF:
     ```
     echo OFF | ipfs pubsub pub led-control
     ```

## Contributing
Feel free to submit pull requests or open issues for improvements and bug fixes.

## License
This project is licensed under the MIT License. See `LICENSE` for details.
```
