### LORA MCU
Long range radio communication using LORA module on Node MCU board.

**Initial setup**

- Connected the board via USB to Serial communication to your linux machine.

- Flash Node MCU board with MicroPython

  ````sh
  bash scripts/flash.sh /dev/ttyUSB0
  ````

- Setup alias for development

  ````sh
  source scripts/alias.sh /dev/ttyUSB0
  ````

**Application deployment**

````sh
deploy
````

This will copy all the contents inside `lib`, `src` and `main.py` to your Node MCU board.

----

**Notes:**

- If you want to modify a file and then update it without deploying the whole application simply use: `mcp <path/on/linux/machine> <path/on/mcu/board>` for example:

  ````sh
  ampy put <path/on/linux/machine> <path/on/mcu/board>
  ````

- If you want to execute a file from you linux machine to directly on the board:

  ````sh
  mpy src/app.py
  ````

  Make sure all other dependencies of `app.py` are already copied on the board.
