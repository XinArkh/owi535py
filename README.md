# Owi535py - A Python Wrapper for OWI-535

[OWI-535](https://owirobot.com/robotic-arm-edge/) Robotic Arm Edge is a robot arm kit with five degrees of freedom. This project provides a set of basic Python interfaces for controlling OWI-535.

<p align="center">
    <img src="./docs/pic/owi535.jpg">
</p>

## Prerequisites

- [PyUSB](https://pyusb.github.io/pyusb/)

**NOTE**: `PyUSB` requires a manually installed `libusb` backend. See [this doc](./docs/libusb-win32.md) for installation instructions on Windows platform.

## Robot Parameters

- Weight: 658 g
- Lifting Capacity: 100 g
- 9.0" L x 6.3" W x 15.0" H
- Power Source: 4 D Cell Batteries (not included)
- Maximum Vertical Reach: 15"
- Maximum Horizontal Reach: 12.6"
- Wrist Motion Range: 120°
- Elbow Motion Range: 300°
- Base Motion (shoulder) Range: 180°
- Base Rotation Range: 270°

Modeling parameters: see [a-mohsen/Robotic-Arm-Automation](https://github.com/a-mohsen/Robotic-Arm-Automation)

## Message Rules

See [this doc](./docs/rules.md).

## A Resource List

[@sonnyp](https://github.com/sonnyp) has made up a [list](https://github.com/sonnyp/owi-535/wiki/Links) of corresponding resources. However, some of them have already been dead now. Try visit them via [Wayback Machine](https://web.archive.org/).

## References

- [keszegrobert/owi535](https://github.com/keszegrobert/owi535)
- [a-mohsen/Robotic-Arm-Automation](https://github.com/a-mohsen/Robotic-Arm-Automation)
