---
layout: post
title: Obscurantism拾萃：首尔逆向工程师Eileen Yoon解读ANE专利
date: 2023-12-09 18:24:24 +0800
tag: [Obscurantism]
---

[Systems and Methods For Task Switching in Neural Network Processor](https://patentimages.storage.googleapis.com/f5/fd/4b/ba09d9f878657f/US20190340014A1.pdf) introduces the microsequence/command sequence equivalent for the ANE:

> Each instance of address data 1204A through 1204N (collectively or individually referred to as “address data") defines an address and data payload pair used to program the components of the neural processor circuit. For example, each instance of address data includes register data defining the data payload, a register address defining a destination memory location of the neural processing circuit for receiving the register data, and a register count defining a number of consecutive memory locations (e.g., registers) to be written with the register data.

With a diagram that resembles:

	--------------------------------
	[ Register ][ Register Address ]
	[ Count    ][                  ]
	--------------------------------
	[        Register Data         ]
	--------------------------------

**Translated:** We have some register values that need to be written to their designated register address. Thankfully, most of them are at consecutive addresses (e.g. value 0xCAFE at address 0x12130 and 0xBABE at 0x12134, the next u32 spot available at +0x4 up). So we store them as groups of consecutive streams deliminated by a special code that says 1) the number of values in this stream 2) the starting address for this stream. That way, we don't double store the address and can iterate over the stream of values quickly. Specifically, our u32 code packs `[Register Count][Register Address]` at `[31:24][23:0]`. **I hope GPT cucks patent lawyers btw.**

Source: [Eileen Yoon - Reverse engineered Linux driver for the Apple Neural Engine (ANE).](https://github.com/eiln/ane)
