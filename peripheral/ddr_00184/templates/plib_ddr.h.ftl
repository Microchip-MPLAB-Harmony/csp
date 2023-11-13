/*******************************************************************************
  Memory System Service Settings for DDR Initialization

  Company:
    Microchip Technology Inc.

  File Name:
    plib_ddr.h

  Summary:
    Memory System Service implementation for the DDR controller.

  Description:
    The Memory System Service initializes the DDR Controller and PHY to
    provide access to external DDR2 SDRAM.

  Remarks:
    Static interfaces incorporate the driver instance number within the names
    of the routines, eliminating the need for an object ID or object handle.
    Static single-open interfaces also eliminate the need for the open handle.
*******************************************************************************/

//DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2014 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
//DOM-IGNORE-END

#ifndef PLIB_DDR_H
#define PLIB_DDR_H

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
#include "device.h"

#ifdef __cplusplus  // Provide C++ Compatibility
    extern "C" {
#endif

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

/* Host Commands */
#define DRV_DDR_IDLE_NOP                0x00FFFFFF
#define DRV_DDR_PRECH_ALL_CMD           0x00FFF401
#define DRV_DDR_REF_CMD                 0x00FFF801
#define DRV_DDR_LOAD_MODE_CMD          (0x00FFF001U)
#define DRV_DDR_CKE_LOW                 0x00FFEFFE

/* DDR address decoding */
#define COL_HI_RSHFT            (0U)
#define COL_HI_MASK             (0U)
#define COL_LO_MASK             ((1UL << ${DDR_COL_BITS}) - 1U)

#define BA_RSHFT                ${DDR_COL_BITS}
#define BANK_ADDR_MASK          ((1UL << ${DDR_BANK_BITS}) - 1U)

#define ROW_ADDR_RSHIFT         (BA_RSHFT + ${DDR_BANK_BITS})
#define ROW_ADDR_MASK           ((1UL << ${DDR_ROW_BITS}) - 1U)

//#define CS_ADDR_RSHIFT        (ROW_ADDR_RSHIFT + ${DDR_ROW_BITS})
#define CS_ADDR_RSHIFT          0
#define CS_ADDR_MASK            0

#define CTRL_CLK_PERIOD         (${DDR_CLK_PER}U * 2U)

// *****************************************************************************
// *****************************************************************************
// Section: Function Prototypes
// *****************************************************************************
// *****************************************************************************

typedef enum {

    DDR_TARGET_0 = 0x00,
    DDR_TARGET_1 = 0x01,
    DDR_TARGET_2 = 0x02,
    DDR_TARGET_3 = 0x03,
    DDR_TARGET_4 = 0x04

} DDR_TARGET;

typedef enum {

    // Peripheral Pin Select registers
    DEVCON_PERMISSION_GROUP_REGISTERS = 1,

    // Peripheral Module Disable registers
    DEVCON_PMD_REGISTERS = 2,

    // Permission Group registers
    DEVCON_PPS_REGISTERS = 4,

    // All lockable registers
    DEVCON_ALL_REGISTERS = 7

} DEVCON_REGISTER_SET;

typedef enum {

    POWER_MODULE_DDR2 = 0xDC

} POWER_MODULE;

typedef enum {

    DDR_PHY_SCL_BURST_MODE_4 = 0x00,
    DDR_PHY_SCL_BURST_MODE_8 = 0x01

} DDR_PHY_SCL_BURST_MODE;

typedef enum {

    DDR_PHY_DDR_TYPE_DDR2 = 0x00,
    DDR_PHY_DDR_TYPE_DDR3 = 0x01

} DDR_PHY_DDR_TYPE;


#define     DDR_HOST_CMD_REG_10   (0x00U)
#define     DDR_HOST_CMD_REG_11   (0x01U)
#define     DDR_HOST_CMD_REG_12   (0x02U)
#define     DDR_HOST_CMD_REG_13   (0x03U)
#define     DDR_HOST_CMD_REG_14   (0x04U)
#define     DDR_HOST_CMD_REG_15   (0x05U)
#define     DDR_HOST_CMD_REG_16   (0x06U)
#define     DDR_HOST_CMD_REG_17   (0x07U)
#define     DDR_HOST_CMD_REG_18   (0x08U)
#define     DDR_HOST_CMD_REG_19   (0x09U)
#define     DDR_HOST_CMD_REG_110  (0x0AU)
#define     DDR_HOST_CMD_REG_111  (0x0BU)
#define     DDR_HOST_CMD_REG_112  (0x0CU)
#define     DDR_HOST_CMD_REG_113  (0x0DU)
#define     DDR_HOST_CMD_REG_114  (0x0EU)
#define     DDR_HOST_CMD_REG_115  (0x0FU)
#define     DDR_HOST_CMD_REG_20   (0x10U)
#define     DDR_HOST_CMD_REG_21   (0x11U)
#define     DDR_HOST_CMD_REG_22   (0x12U)
#define     DDR_HOST_CMD_REG_23   (0x13U)
#define     DDR_HOST_CMD_REG_24   (0x14U)
#define     DDR_HOST_CMD_REG_25   (0x15U)
#define     DDR_HOST_CMD_REG_26   (0x16U)
#define     DDR_HOST_CMD_REG_27   (0x17)
#define     DDR_HOST_CMD_REG_28   (0x18U)
#define     DDR_HOST_CMD_REG_29   (0x19U)
#define     DDR_HOST_CMD_REG_210  (0x1AU)
#define     DDR_HOST_CMD_REG_211  (0x1BU)
#define     DDR_HOST_CMD_REG_212  (0x1CU)
#define     DDR_HOST_CMD_REG_213  (0x1DU)
#define     DDR_HOST_CMD_REG_214  (0x1EU)
#define     DDR_HOST_CMD_REG_215  (0x1FU)

typedef uint32_t DDR_HOST_CMD_REG;

//******************************************************************************
/* Function:
    void DDR_Initialize ( void * data)

  Summary:
    Initializes and Enables the DDR External Memory Controller.

  Description:
    This function Enables the external DDR memory controller module.

  Precondition:
    None.

  Parameters:
    data            - Pointer to the data structure containing any data
                      necessary to initialize the hardware. This pointer may
                      be null if no data is required and default
                      initialization is to be used.

  Returns:
    None.

  Example:
  <code>
    DDR_Initialize(NULL);
  </code>

  Remarks:
    This routine must be called before any attempt to access external
    DDR memory.

    Not all features are available on all devices. Refer to the specific
    device data sheet to determine availability.
*/
void DDR_Initialize(void);

#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif

#endif // #ifndef _PLIB_DDR_H

/*******************************************************************************
 End of File
*/
