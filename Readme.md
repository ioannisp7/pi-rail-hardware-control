# Pi Rail Hardware Control

A modular and reusable hardware control system for model railways, based on Raspberry Pi and Raspberry Pi Pico.

## Overview

Pi Rail Hardware Control provides a software interface for controlling physical model railway hardware, including independently powered track sections, turnouts, relays and motor drivers.

The system separates high-level application logic from low-level hardware execution. A Raspberry Pi communicates with a Raspberry Pi Pico through a USB serial connection, while the Pico executes hardware operations using its GPIO and PWM capabilities.

The project is designed to operate independently of any specific railway automation, computer vision or traffic management application.

## Objectives

- Provide a reusable hardware control interface for model railway applications.
- Separate application-level decisions from physical hardware execution.
- Support independently controlled track sections and turnouts.
- Support GPIO and PWM-based hardware control.
- Provide low-overhead communication between the Raspberry Pi and Raspberry Pi Pico.
- Allow hardware configuration without modifying external application logic.
- Support future hardware and communication extensions.

## Architecture

The system consists of two main software components:

### Raspberry Pi

The host-side software is responsible for:

- Providing a public Python interface.
- Receiving hardware operation requests from external applications.
- Constructing hardware control commands.
- Managing USB serial communication.
- Handling communication and configuration errors.

### Raspberry Pi Pico

The microcontroller firmware is responsible for:

- Receiving and interpreting hardware commands.
- Controlling GPIO outputs.
- Generating PWM signals.
- Operating connected railway hardware.
- Managing local hardware configuration and safety mechanisms.

## Technologies

- Raspberry Pi
- Raspberry Pi Pico
- Python
- MicroPython
- PySerial
- USB serial communication
- GPIO
- PWM

## Software Prerequisites

### Raspberry Pi

- Raspberry Pi OS
- Python 3
- PySerial

Install PySerial using:

```bash
sudo apt update
sudo apt install python3-serial
```

Verify the installation:

```bash
python3 -c "import serial; print(serial.__version__)"
```

### Raspberry Pi Pico

- MicroPython firmware compatible with the target microcontroller.

The initial development and communication experiments were successfully performed using MicroPython v1.29.0 on the original Raspberry Pi Pico (RP2040).

### Development and Firmware Deployment

The following tools are required for firmware development and deployment but are not required for normal runtime operation:

- pipx
- mpremote

Install the development tools on the Raspberry Pi:

```bash
sudo apt install pipx
pipx install mpremote
pipx ensurepath
```

The Raspberry Pi Pico must be connected to the Raspberry Pi using a USB data cable.

## Repository Structure

```text
pi-rail-hardware-control/
├── docs/
├── src/
│   ├── pi/
│   └── pico/
├── tests/
├── .gitignore
└── README.md
```

- `docs/`: Architecture and technical documentation.
- `src/pi/`: Python software executed on the Raspberry Pi.
- `src/pico/`: MicroPython firmware executed on the Raspberry Pi Pico.
- `tests/`: Unit tests and hardware communication experiments.

## Documentation

For additional information about the system design, see [Architecture](docs/architecture.md).