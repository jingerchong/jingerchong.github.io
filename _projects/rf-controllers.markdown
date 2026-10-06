---
title: Wireless Controllers for a Robotics Class
tier: unlisted
order: 240
year: 2020
context: 16.632 Intro to Autonomous Machines
summary: Twenty-five Arduino-based wireless controllers, soldered, assembled, and tested for a sophomore robotics class.
tldr: >-
  Twenty-five handheld wireless controllers were soldered, assembled, debugged, and delivered
  for the students of a NEET sophomore robotics class to drive the robots they built.
image: /assets/images/rf-controllers/cover.webp
---

I built 25 wireless controllers for the NEET Autonomous Machines sophomore project class, 2.S007 Design and Manufacturing I (of Robotic Systems). The design follows a tutorial by [How to Mechatronics](https://howtomechatronics.com/projects/diy-arduino-rc-transmitter/){: target="_blank" rel="noopener noreferrer" }. Each controller carries an Arduino Pro Mini, two joysticks, two toggle switches, two potentiometers, six push buttons, an MPU6050 IMU, and an NRF24L01 radio, along with capacitors, jumpers, and a voltage regulator. Two rechargeable 3.7 V Li-ion batteries power it, and two laser-cut acrylic plates enclose it.

Starting from custom PCBs and a finished reference controller, I set up the workstation, soldered the IMUs, headers, and Arduinos, and worked around a board-version mismatch that needed extra wiring. I then laser-cut the covers, assembled all 25 controllers, and tested and debugged each one.

{% include gallery.html dir="gallery" title="Controllers" %}
