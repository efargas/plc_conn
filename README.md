# plc_conn gesgt

plc_conn is a Python library tailored to provide an intuitive interface for controlling Mitsubishi (e.g., MEL_FX5U) and Siemens PLCs.

## Installation

```bash
pip install plc_conn
```

(Note: This will work once the package is published to PyPI. For local installation from the built package, you can use `pip install path/to/your_package_wheel.whl` or `pip install .` from the project root after building).

# Features

- Multiple PLC Support: Connect seamlessly to a wide range of Mitsubishi and Siemens PLCs.
- Read Operations: Extract boolean values, 16-bit, and 32-bit integers from PLCs.
- Write Operations: Relay boolean, 16-bit, and 32-bit integers to PLCs.
- Flexible Logging: Optional logging capability for enhanced debugging and tracking.

## Basic Usage

```python
from plc_conn import PLC

# Initialize the PLC object
# Replace with your PLC's actual IP address, port, and type
plc_instance = PLC(ip_address='192.168.1.10', port=502, plc_type='MEL_FX5U', log=True)

if plc_instance.connected:
    print(f"Successfully connected to PLC at {plc_instance.ip_address}")

    # Example: Read a boolean value from register M100
    bool_value = plc_instance.read_bool('M100')
    if bool_value is not None:
        print(f"Value of M100: {bool_value}")
    else:
        print("Failed to read M100")

    # Example: Write a boolean value to register M101
    write_status = plc_instance.write_bool('M101', True)
    print(f"Write status for M101: {write_status}")

    # Example: Read an integer value from register D100
    int_value = plc_instance.read_int16('D100')
    if int_value is not None:
        print(f"Value of D100: {int_value}")
    else:
        print("Failed to read D100")

else:
    print(f"Failed to connect to PLC at {plc_instance.ip_address}")

```

# Supported PLC Types
Mitsubishi:
- "MEL_FX5U" - Mitsubishi FX5U
- "MEL_QSER" - Mitsubishi Qseries
- "MEL_FX3U" - Mitsubishi FX3U
  
Siemens:
- "SMN_S300" - SIEMENS S300
- "SMN_S1200" - SIEMENS S1200
- "SMN_S1500" - SIEMENS S1500
- "SMN_S200" - SIEMENS S200 smart
For any other PLC type you may open an issue, I will try my best to add the functionality.

# License
This project adopts the MIT License. Kindly check the LICENSE.md file for comprehensive details.
