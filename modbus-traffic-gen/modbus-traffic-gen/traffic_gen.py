import time
from pymodbus.client.tcp import ModbusTcpClient

client = ModbusTcpClient("modbus-server", port=5020)

if not client.connect():
    raise Exception("Unable to connect to Modbus server")

try:
    while True:
        coils = client.read_coils(address=0, count=100)
        discrete_inputs = client.read_discrete_inputs(address=0, count=100)
        holding_registers = client.read_holding_registers(address=0, count=100)
        input_registers = client.read_input_registers(address=0, count=100)

        if coils.isError():
            print(f"Error getting coils: {coils}")
        else:
            print("Coils:", coils.bits)

        if not discrete_inputs.isError():
            print("Discrete Inputs:", discrete_inputs.bits)

        if not holding_registers.isError():
            print("Holding Registers:", holding_registers.registers)

        if not input_registers.isError():
            print("Input Registers:", input_registers.registers)

        print("-" * 40)

        time.sleep(2)  # poll every 2 seconds

finally:
    client.close()