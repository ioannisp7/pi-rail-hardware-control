# System Architecture

## 1. Introduction

Pi Rail Hardware Control is a modular hardware control system for model railways.

The system separates application-level railway decisions from physical hardware execution by distributing responsibilities between a Raspberry Pi and a Raspberry Pi Pico.

The project is designed to operate independently of any specific railway automation or computer vision application.

## 2. Architectural Objectives

- Separation of concerns.
- Reusability.
- Low communication overhead.
- Modular hardware control.
- Configurable hardware assignments.
- Maintainability.
- Extensibility.
- Safe hardware operation.

## 3. System Overview

The system consists of three logical layers:

1. External Application.
2. Host-side Hardware Control.
3. Microcontroller-side Hardware Execution.

```text
External Application
        |
        v
Raspberry Pi
+-----------------------------+
| Hardware Controller         |
|                             |
| Track Section Connector     |
| Turnout Connector           |
|                             |
| Serial Communication        |
+-----------------------------+
        |
        | USB Serial
        |
        v
Raspberry Pi Pico
+-----------------------------+
| Command Receiver            |
| Command Interpreter         |
|                             |
| Track Section Control       |
| Turnout Control             |
|                             |
| GPIO / PWM                  |
+-----------------------------+
        |
        v
Physical Railway Hardware
```

The external application determines which hardware operations should be performed. Hardware Control translates these requests into physical hardware operations.

## 4. Host-side Architecture

The host-side software is executed on a Raspberry Pi and is implemented in Python.

### 4.1. Hardware Controller

The Hardware Controller provides a common public interface for external applications.

Its responsibilities include receiving hardware operation requests and delegating them to the appropriate hardware connectors.

### 4.2. Track Section Connector

The Track Section Connector is responsible for translating track section power requests into hardware commands.

A connector may manage multiple independently controlled track sections.

### 4.3. Turnout Connector

The Turnout Connector is responsible for translating turnout position requests into hardware commands.

A connector may manage multiple independently controlled turnouts.

### 4.4. Serial Communication

The Serial Communication component manages communication with the Raspberry Pi Pico.

Its responsibilities include:

- Opening and closing the serial connection.
- Maintaining a persistent connection.
- Transmitting hardware commands.
- Handling communication errors.

Hardware connectors share the same serial communication component.

## 5. Microcontroller-side Architecture

The microcontroller-side firmware is executed on a Raspberry Pi Pico and is implemented in MicroPython.

### 5.1. Command Receiver

The Command Receiver continuously receives commands through the USB serial interface.

### 5.2. Command Interpreter

The Command Interpreter parses and validates incoming commands and delegates valid requests to the appropriate hardware control component.

### 5.3. Track Section Control

The Track Section Control component operates GPIO outputs associated with independently controlled railway track sections.

Depending on the connected hardware, these outputs may control relays, motor drivers or other power switching devices.

### 5.4. Turnout Control

The Turnout Control component operates GPIO outputs associated with railway turnouts.

Hardware-specific electrical and timing requirements are handled locally by the microcontroller.

### 5.5. PWM Control

The Raspberry Pi Pico generates PWM signals locally when required by connected hardware.

This avoids transmitting PWM waveforms over the USB connection and reduces host-side processing requirements.

## 6. Communication Architecture

Communication between the Raspberry Pi and Raspberry Pi Pico uses USB serial communication.

The host-side implementation uses PySerial.

The initial communication protocol will use human-readable, newline-terminated text commands.

A persistent serial connection is maintained during normal operation.

The exact command syntax, supported operations and validation rules will be defined before production implementation.

The initial implementation does not require command acknowledgements or physical hardware state feedback.

## 7. Hardware Configuration

Hardware configuration separates logical railway element identifiers from physical GPIO assignments.

External applications request operations using logical identifiers rather than directly accessing GPIO pins.

Physical GPIO assignments and hardware-specific execution parameters are managed by the microcontroller-side software.

The configuration format and distribution of logical identifiers between the host and microcontroller will be defined during implementation.

## 8. State Management

The project does not maintain an authoritative application-level railway state model.

External applications are responsible for tracking requested railway element states.

The Hardware Control system attempts to execute requested hardware operations.

Successful command transmission does not guarantee successful physical hardware execution.

Communication errors may be reported to the external application without requiring physical hardware feedback.

## 9. Execution Model

The initial host-side implementation uses synchronous operation without additional threads or application-level command queues.

The microcontroller executes a continuous command-processing loop.

Hardware PWM is generated locally by the microcontroller.

Additional concurrency mechanisms may be introduced if demonstrated hardware timing or communication requirements justify them.

## 10. Hardware Safety

Hardware safety considerations include:

- Safe GPIO initialization.
- Prevention of unintended output activation.
- Command validation.
- Electrical compatibility with connected hardware.
- Appropriate hardware power supplies.
- Communication loss handling.
- Safe shutdown behavior.

Detailed safety mechanisms will be established during hardware integration.

## 11. External Application Integration

The project exposes a public Python interface that can be used by external applications.

It may be integrated into pi-railvision-ai as a Git submodule.

The project must not depend on pi-railvision-ai, pi-detection-zones or application-specific railway intelligence classes.

## 12. Development Status

The initial communication experiment has successfully verified:

- USB connectivity between Raspberry Pi 4 and Raspberry Pi Pico.
- MicroPython execution.
- Remote firmware deployment using mpremote.
- Automatic execution of firmware at startup.
- USB serial communication using PySerial.
- Reception and interpretation of text commands.
- GPIO control using the Pico onboard LED.

Production hardware control components and physical railway hardware integration remain under development.

## 13. Future Extensions

Potential future extensions include:

- Additional hardware driver types.
- Multiple microcontroller devices.
- Alternative communication transports.
- RS-485 communication.
- Communication watchdogs.
- Extended motor speed and direction control.
- Optional command acknowledgements.
- Optional hardware state feedback.

These extensions are not requirements of the initial implementation.