import random
import logging
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
from pymodbus.server.async_io import StartTcpServer

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

coils = ModbusSequentialDataBlock(1, [False] * 100)
discrete_inputs = ModbusSequentialDataBlock(1, [False] * 100)
h_reg = ModbusSequentialDataBlock(1, [0] * 100)
in_reg = ModbusSequentialDataBlock(1, [0] * 100)

temperature_values = [random.randint(4, 15) for _ in range(7)]
h_reg.setValues(1, temperature_values)
print("temperature_values:", temperature_values)


slave_context = ModbusSlaveContext(
    di=discrete_inputs,
    co=coils,
    hr=h_reg,
    ir=in_reg
)


server_context = ModbusServerContext(slaves=slave_context, single=True)


StartTcpServer(context=server_context, address=("0.0.0.0", 5020))