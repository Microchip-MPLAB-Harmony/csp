/*******************************************************************************
  Systick System Initialization File

  File Name:
    system_core_mpu.c

  Summary:
    This file contains source code necessary to initialize the system.

  Description:
    Initializes the system core memory protection unit (ARM Cortex-M MPU) according to the
    selected configuration.
 *******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

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

#include "arch/arm/device_${__PROCESSOR?lower_case}.h"
#include "arch/arm/arm_cm_mpu.h"

const uint32_t mpu_system_regions[] =
{
    /* ITCM, 0x0-0x400000, 4MB=2^22 */
    MPU_REGION(0, 0x0),
    MPU_REGION_SIZE(21) |
    MPU_RASR_AP(MPU_RASR_AP_READONLY_Val) |
    MPU_ATTR_NORMAL_WB |
    MPU_ATTR_ENABLE,

    /* Internal flash, 0x400000-0x800000, 4MB=2^22 */
    MPU_REGION(1, 0x400000),
    MPU_REGION_SIZE(21) |
    MPU_RASR_AP(MPU_RASR_AP_READONLY_Val) |
    MPU_ATTR_NORMAL_WB |
    MPU_ATTR_ENABLE,

    /* DTCM, 0x20000000-0x20400000, 4MB=2^22 */
    MPU_REGION(2, 0x20000000),
    MPU_REGION_SIZE(21) |
    MPU_RASR_AP(MPU_RASR_AP_READWRITE_Val) |
    MPU_ATTR_NORMAL_WB_WA |
    MPU_ATTR_ENABLE,

    /* SRAM, 0x20400000-0x20C00000, 8MB=2^23 */
    MPU_REGION(3, 0x20400000),
    MPU_REGION_SIZE(22) |
    MPU_RASR_AP(MPU_RASR_AP_READWRITE_Val) |
    MPU_ATTR_NORMAL_WB_WA |
    MPU_ATTR_ENABLE,

    /* Not Cached SRAM, 0x2045F000-0x20460000, 4KB=2^12 */
    MPU_REGION(4, 0x2045F000),
    MPU_REGION_SIZE(11) |
    MPU_RASR_AP(MPU_RASR_AP_READWRITE_Val) |
    MPU_ATTR_NORMAL |
    MPU_ATTR_ENABLE,

    /* Peripherals,  0x40000000, 256MB=2^28 */
    MPU_REGION(5, 0x40000000),
    MPU_REGION_SIZE(27) |
    MPU_RASR_AP(MPU_RASR_AP_READWRITE_Val) |
    MPU_ATTR_DEVICE |
    MPU_ATTR_EXECUTE_NEVER |
    MPU_ATTR_ENABLE,

    /* EBI, 0x60000000, 256MB=2^28 */
    MPU_REGION(6, 0x60000000),
    MPU_REGION_SIZE(27) |
    MPU_RASR_AP(MPU_RASR_AP_READWRITE_Val) |
    MPU_ATTR_STRONGLY_ORDERED |
    MPU_ATTR_EXECUTE_NEVER |
    MPU_ATTR_ENABLE,

    /* SDRAM, 0x70000000, 256MB=2^28 */
    MPU_REGION(7, 0x70000000),
    MPU_REGION_SIZE(27) |
    MPU_RASR_AP(MPU_RASR_AP_READWRITE_Val) |
    MPU_ATTR_NORMAL_WB |
    MPU_ATTR_ENABLE,

    /* QSPI, 0x80000000, 256MB=2^28 */
    MPU_REGION(8, 0x80000000),
    MPU_REGION_SIZE(27) |
    MPU_RASR_AP(MPU_RASR_AP_READWRITE_Val) |
    MPU_ATTR_STRONGLY_ORDERED |
    MPU_ATTR_ENABLE,

    /* USB RAM, 0xA0100000, 1MB=2^20 */
    MPU_REGION(9, 0xA0100000),
    MPU_REGION_SIZE(19) |
    MPU_RASR_AP(MPU_RASR_AP_READWRITE_Val) |
    MPU_ATTR_DEVICE |
    MPU_ATTR_EXECUTE_NEVER |
    MPU_ATTR_ENABLE,

    /* Private Peripheral Bus, 0xE0000000, 1MB=2^20 */
    MPU_REGION(10, 0xE0000000),
    MPU_REGION_SIZE(19) |
    MPU_RASR_AP(MPU_RASR_AP_READWRITE_Val) |
    MPU_ATTR_STRONGLY_ORDERED |
    MPU_ATTR_EXECUTE_NEVER |
    MPU_ATTR_ENABLE,

    /* end marker */
    0, 0
};

const uint32_t mpu_flash_write_region[] =
{
    /* Internal flash, 0x400000-0x800000, 4MB=2^22 */
    MPU_REGION(1, 0x400000),
    MPU_REGION_SIZE(21) |
    MPU_RASR_AP(MPU_RASR_AP_READWRITE_Val) |
    MPU_ATTR_STRONGLY_ORDERED |
    MPU_ATTR_ENABLE,

    /* end marker */
    0, 0
};

const uint32_t mpu_flash_read_region[] =
{
    /* Internal flash, 0x400000-0x800000, 4MB=2^22 */
    MPU_REGION(1, 0x400000),
    MPU_REGION_SIZE(21) |
    MPU_RASR_AP(MPU_RASR_AP_READONLY_Val) |
    MPU_ATTR_NORMAL_WB |
    MPU_ATTR_ENABLE,

    /* end marker */
    0, 0
};

/******************************************************************************
  Function:
    ARCH_CORE_MPU_Initialize(void)

  Summary:
    Initializes Core MPU Service (ARM Cortex-M MPU)

  Description:
    This function initializes the system core Memory Protection Unit (ARM Cortex-M MPU)
    according to the selected configuration.

  Remarks:
    None.
*/
void ARCH_CORE_MPU_Initialize(void)
{
	if (mpu_is_enabled())
		return;

	/* Enable MPU, I-Cache and D-Cache */
	mpu_configure(mpu_system_regions);
	mpu_enable();
}
