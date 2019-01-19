/*******************************************************************************
  GPIO PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_gpio.h

  Summary:
    GPIO PLIB Header File

  Description:
    This library provides an interface to control and interact with Parallel
    Input/Output controller (GPIO) module.

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*******************************************************************************/

#ifndef PLIB_GPIO_H
#define PLIB_GPIO_H

#include <device.h>
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data types and constants
// *****************************************************************************
// *****************************************************************************



// *****************************************************************************
/* GPIO Port

  Summary:
    Identifies the available GPIO Ports.

  Description:
    This enumeration identifies the available GPIO Ports.

  Remarks:
    The caller should not rely on the specific numbers assigned to any of
    these values as they may change from one processor to the next.

    Not all ports are available on all devices.  Refer to the specific
    device data sheet to determine which ports are supported.
*/

typedef enum
{
    GPIO_PORT_A = 0,
    GPIO_PORT_B = 1,
    GPIO_PORT_C = 2,
    GPIO_PORT_D = 3,
    GPIO_PORT_E = 4,
    GPIO_PORT_F = 5,
    GPIO_PORT_G = 6,
    GPIO_PORT_H = 7,
    GPIO_PORT_J = 8,
    GPIO_PORT_K = 9,
} GPIO_PORT;

// *****************************************************************************
/* GPIO Port Pins

  Summary:
    Identifies the available GPIO port pins.

  Description:
    This enumeration identifies the available GPIO port pins.

  Remarks:
    The caller should not rely on the specific numbers assigned to any of
    these values as they may change from one processor to the next.

    Not all pins are available on all devices.  Refer to the specific
    device data sheet to determine which pins are supported.
*/

typedef enum
{
    GPIO_PIN_RA0 = 0,
    GPIO_PIN_RA1 = 1,
    GPIO_PIN_RA2 = 2,
    GPIO_PIN_RA3 = 3,
    GPIO_PIN_RA4 = 4,
    GPIO_PIN_RA5 = 5,
    GPIO_PIN_RA6 = 6,
    GPIO_PIN_RA7 = 7,
    GPIO_PIN_RA9 = 9,
    GPIO_PIN_RA10 = 10,
    GPIO_PIN_RA14 = 14,
    GPIO_PIN_RA15 = 15,
    GPIO_PIN_RB0 = 32,
    GPIO_PIN_RB1 = 33,
    GPIO_PIN_RB2 = 34,
    GPIO_PIN_RB3 = 35,
    GPIO_PIN_RB4 = 36,
    GPIO_PIN_RB5 = 37,
    GPIO_PIN_RB6 = 38,
    GPIO_PIN_RB7 = 39,
    GPIO_PIN_RB8 = 40,
    GPIO_PIN_RB9 = 41,
    GPIO_PIN_RB10 = 42,
    GPIO_PIN_RB11 = 43,
    GPIO_PIN_RB12 = 44,
    GPIO_PIN_RB13 = 45,
    GPIO_PIN_RB14 = 46,
    GPIO_PIN_RB15 = 47,
    GPIO_PIN_RC1 = 65,
    GPIO_PIN_RC2 = 66,
    GPIO_PIN_RC3 = 67,
    GPIO_PIN_RC4 = 68,
    GPIO_PIN_RC12 = 76,
    GPIO_PIN_RC13 = 77,
    GPIO_PIN_RC14 = 78,
    GPIO_PIN_RC15 = 79,
    GPIO_PIN_RD0 = 96,
    GPIO_PIN_RD1 = 97,
    GPIO_PIN_RD2 = 98,
    GPIO_PIN_RD3 = 99,
    GPIO_PIN_RD4 = 100,
    GPIO_PIN_RD5 = 101,
    GPIO_PIN_RD6 = 102,
    GPIO_PIN_RD7 = 103,
    GPIO_PIN_RD9 = 105,
    GPIO_PIN_RD10 = 106,
    GPIO_PIN_RD11 = 107,
    GPIO_PIN_RD12 = 108,
    GPIO_PIN_RD13 = 109,
    GPIO_PIN_RD14 = 110,
    GPIO_PIN_RD15 = 111,
    GPIO_PIN_RE0 = 128,
    GPIO_PIN_RE1 = 129,
    GPIO_PIN_RE2 = 130,
    GPIO_PIN_RE3 = 131,
    GPIO_PIN_RE4 = 132,
    GPIO_PIN_RE5 = 133,
    GPIO_PIN_RE6 = 134,
    GPIO_PIN_RE7 = 135,
    GPIO_PIN_RE8 = 136,
    GPIO_PIN_RE9 = 137,
    GPIO_PIN_RF0 = 160,
    GPIO_PIN_RF1 = 161,
    GPIO_PIN_RF2 = 162,
    GPIO_PIN_RF3 = 163,
    GPIO_PIN_RF4 = 164,
    GPIO_PIN_RF5 = 165,
    GPIO_PIN_RF8 = 168,
    GPIO_PIN_RF12 = 172,
    GPIO_PIN_RF13 = 173,
    GPIO_PIN_RG0 = 192,
    GPIO_PIN_RG1 = 193,
    GPIO_PIN_RG6 = 198,
    GPIO_PIN_RG7 = 199,
    GPIO_PIN_RG8 = 200,
    GPIO_PIN_RG9 = 201,
    GPIO_PIN_RG12 = 204,
    GPIO_PIN_RG13 = 205,
    GPIO_PIN_RG14 = 206,
    GPIO_PIN_RG15 = 207,
    GPIO_PIN_RH0 = 224,
    GPIO_PIN_RH1 = 225,
    GPIO_PIN_RH2 = 226,
    GPIO_PIN_RH3 = 227,
    GPIO_PIN_RH4 = 228,
    GPIO_PIN_RH5 = 229,
    GPIO_PIN_RH6 = 230,
    GPIO_PIN_RH7 = 231,
    GPIO_PIN_RH8 = 232,
    GPIO_PIN_RH9 = 233,
    GPIO_PIN_RH10 = 234,
    GPIO_PIN_RH11 = 235,
    GPIO_PIN_RH12 = 236,
    GPIO_PIN_RH13 = 237,
    GPIO_PIN_RH14 = 238,
    GPIO_PIN_RH15 = 239,
    GPIO_PIN_RJ0 = 256,
    GPIO_PIN_RJ1 = 257,
    GPIO_PIN_RJ2 = 258,
    GPIO_PIN_RJ3 = 259,
    GPIO_PIN_RJ4 = 260,
    GPIO_PIN_RJ5 = 261,
    GPIO_PIN_RJ6 = 262,
    GPIO_PIN_RJ7 = 263,
    GPIO_PIN_RJ8 = 264,
    GPIO_PIN_RJ9 = 265,
    GPIO_PIN_RJ10 = 266,
    GPIO_PIN_RJ11 = 267,
    GPIO_PIN_RJ12 = 268,
    GPIO_PIN_RJ13 = 269,
    GPIO_PIN_RJ14 = 270,
    GPIO_PIN_RJ15 = 271,
    GPIO_PIN_RK0 = 288,
    GPIO_PIN_RK1 = 289,
    GPIO_PIN_RK2 = 290,
    GPIO_PIN_RK3 = 291,
    GPIO_PIN_RK4 = 292,
    GPIO_PIN_RK5 = 293,
    GPIO_PIN_RK6 = 294,
    GPIO_PIN_RK7 = 295,

    /* This element should not be used in any of the GPIO APIs.
       It will be used by other modules or application to denote that none of the GPIO Pin is used */
    GPIO_PIN_NONE = -1

} GPIO_PIN;


void GPIO_Initialize(void);

// *****************************************************************************
// *****************************************************************************
// Section: GPIO Functions which operates on multiple pins of a port
// *****************************************************************************
// *****************************************************************************

uint32_t GPIO_PortRead(GPIO_PORT port);

void GPIO_PortWrite(GPIO_PORT port, uint32_t mask, uint32_t value);

uint32_t GPIO_PortLatchRead ( GPIO_PORT port );

void GPIO_PortSet(GPIO_PORT port, uint32_t mask);

void GPIO_PortClear(GPIO_PORT port, uint32_t mask);

void GPIO_PortToggle(GPIO_PORT port, uint32_t mask);

void GPIO_PortInputEnable(GPIO_PORT port, uint32_t mask);

void GPIO_PortOutputEnable(GPIO_PORT port, uint32_t mask);

// *****************************************************************************
// *****************************************************************************
// Section: GPIO Functions which operates on one pin at a time
// *****************************************************************************
// *****************************************************************************

static inline void GPIO_PinWrite(GPIO_PIN pin, bool value)
{
    GPIO_PortWrite(pin>>5, (uint32_t)(0x1) << (pin & 0x1f), (uint32_t)(value) << (pin & 0x1f));
}

static inline bool GPIO_PinRead(GPIO_PIN pin)
{
    return (bool)(((GPIO_PortRead(pin>>5)) >> (pin & 0x1F)) & 0x1);
}

static inline bool GPIO_PinLatchRead(GPIO_PIN pin)
{
    return (bool)((GPIO_PortLatchRead(pin>>5) >> (pin & 0x1F)) & 0x1);
}

static inline void GPIO_PinToggle(GPIO_PIN pin)
{
    GPIO_PortToggle(pin>>5, 0x1 << (pin & 0x1F));
}

static inline void GPIO_PinSet(GPIO_PIN pin)
{
    GPIO_PortSet(pin>>5, 0x1 << (pin & 0x1F));
}

static inline void GPIO_PinClear(GPIO_PIN pin)
{
    GPIO_PortClear(pin>>5, 0x1 << (pin & 0x1F));
}

static inline void GPIO_PinInputEnable(GPIO_PIN pin)
{
    GPIO_PortInputEnable(pin>>5, 0x1 << (pin & 0x1F));
}

static inline void GPIO_PinOutputEnable(GPIO_PIN pin)
{
    GPIO_PortOutputEnable(pin>>5, 0x1 << (pin & 0x1F));
}


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_GPIO_H
