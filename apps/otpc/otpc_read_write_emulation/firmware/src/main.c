/*******************************************************************************
* Copyright (C) 2020 Microchip Technology Inc. and its subsidiaries.
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

/*******************************************************************************
  Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main.c

  Summary:
    This file contains the "main" function for a project.

  Description:
    This file contains the "main" function for a project.  The
    "main" function calls the "SYS_Initialize" function to initialize the state
    machines of all modules in the system
 *******************************************************************************/

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include "definitions.h"                // SYS function prototypes
#include <string.h>

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    uint16_t packet_addr;
    uint32_t payload = 0xC0C0C0C0;
    OTPC_NEW_PACKET pckt;
    uint16_t size = 0;
    memset(&pckt, 0, sizeof(pckt));
    pckt.type = OTP_PCKT_CUSTOM;
    pckt.size = sizeof(payload);
    
    printf("OTP Emulation mode enabled \r\n");
    
    /* Write packet */
    otpc_error_code_t  error = OTPC_WritePacket(&pckt, &payload, &packet_addr, &size);
    if (error == OTPC_NO_ERROR)
    {
      printf("Packet written to address: %x and size = %d, value = %x\r\n", packet_addr, size, (unsigned int)payload);
    }
    else
    {
      printf("Packet write unsuccessful\r\n");
      while(1);
    }
    
    /* Read packet */
    uint32_t readBuffer;
    uint16_t readSize = 0;
    error = OTPC_ReadPacket(packet_addr, &readBuffer, sizeof(readBuffer), &readSize);
    if (error == OTPC_NO_ERROR)
    {
      printf("Packet read from address: %x, size = %d, value = %x\r\n", (unsigned int)packet_addr, readSize, (unsigned int)readBuffer);
    }
    else
    {
      printf("Packet read unsuccessful\r\n");
      while(1);
    }
    
    /* Update packet */
    payload = 0xCBCBCBCB;
    error = OTPC_UpdatePayload(packet_addr, &payload);
    if (error == OTPC_NO_ERROR)
    {
      printf("Packet at address %x is updated \r\n", (unsigned int)packet_addr);
    }
    else
    {
      printf("Packet update unsuccessful\r\n");
      while(1);
    }
    
    /* Read packet */
    error = OTPC_ReadPacket(packet_addr, &readBuffer, sizeof(readBuffer), &readSize);
    if (error == OTPC_NO_ERROR)
    {
      printf("Packet read from address: %x, size = %d, value = %x\r\n", (unsigned int)packet_addr, readSize, (unsigned int)readBuffer);
    }
    else
    {
      printf("Packet read unsuccessful\r\n");
      while(1);
    }
   
    /* Lock packet */
    error = OTPC_LockPacket(packet_addr);
    if (error == OTPC_NO_ERROR)
    {
      printf("Packet at address %x is locked successfully \r\n", (unsigned int)packet_addr);
    }
    else
    {
      printf("Packet Lock unsuccessful\r\n");
      while(1);
    }
    
    error = OTPC_ReadPacket(packet_addr, &readBuffer, sizeof(readBuffer), &readSize);
    if (error == OTPC_NO_ERROR)
    {
      printf("Packet read from address: %x, size = %d, value = %x\r\n", (unsigned int)packet_addr, readSize, (unsigned int)readBuffer);
    }
    else
    {
      printf("Packet read unsuccessful\r\n");
      while(1);
    }    
  
    /* Hide packet */
    error = OTPC_HidePacket(packet_addr);
    if (error == OTPC_NO_ERROR)
    {
      printf("Packet at address %x is hidden successfully \r\n", packet_addr);
    }
    else
    {
      printf("Packet hide unsuccessful\r\n");
      while(1);
    }
    
    error = OTPC_ReadPacket(packet_addr, &readBuffer, sizeof(readBuffer), &readSize);
    if (error == OTPC_NO_ERROR)
    {
      printf("Packet read from address: %x, size = %d, value = %x\r\n", (unsigned int)packet_addr, readSize, (unsigned int)readBuffer);
    }
    else
    {
      printf("Packet read unsuccessful\r\n");
      while(1);
    }    
     
    /* Invalidate packet */
    error = OTPC_InvalidatePacket(packet_addr);
    if (error == OTPC_NO_ERROR)
    {
      printf("Packet at address %x is invalidated successfully.\r\n", (unsigned int)packet_addr);
    }
    else
    {
      printf("Packet invalidate unsuccessful\r\n");
      while(1);
    }

    error = OTPC_ReadPacket(packet_addr, &readBuffer, sizeof(readBuffer), &readSize);
    if (error == OTPC_ERROR_PACKET_IS_INVALID)
    {
      printf("Packet read from address: %x failed as packet is invalid.\r\n", (unsigned int)packet_addr);
    }
    else
    {
      printf("Read success on invalid packet. This should not happen.\r\n");
      while(1);
    }    
    while ( true )
    {
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks ( );
    }

    /* Execution should not come here during normal operation */
    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

