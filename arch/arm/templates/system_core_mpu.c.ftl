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
	mpu_configure();
	mpu_enable();
}
