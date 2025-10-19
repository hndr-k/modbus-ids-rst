import logging
from pymodbus.server import StartTcpServer
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusDeviceContext,
    ModbusServerContext,
)

logging.basicConfig(level=logging.INFO)

def run():

    device = ModbusDeviceContext(
        di=ModbusSequentialDataBlock(0, [0] * 100),  # discrete
        co=ModbusSequentialDataBlock(0, [0] * 100),  # coils
        ir=ModbusSequentialDataBlock(0, [0] * 100),  # input reg
        hr=ModbusSequentialDataBlock(0, [0] * 100),  # holding reg
    )

    #
    context = ModbusServerContext(devices=device, single=True)

    host, port = "0.0.0.0", 5020  
    logging.info("Starting Modbus TCP server on %s:%s ...", host, port)
    StartTcpServer(context, address=(host, port))

if __name__ == "__main__":
    run()