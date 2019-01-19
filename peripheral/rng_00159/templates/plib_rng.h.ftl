/*******************************************************************************
  Random Number Generator (${RNG_INSTANCE_NAME}) Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${RNG_INSTANCE_NAME}.h

  Summary:
    ${RNG_INSTANCE_NAME} PLIB Header File

  Description:
    None

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

#ifndef _PLIB_${RNG_INSTANCE_NAME}_H
#define _PLIB_${RNG_INSTANCE_NAME}_H

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END


// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

/*************************** ${RNG_INSTANCE_NAME} API ******************************************/
// *****************************************************************************
/* Function:
   void ${RNG_INSTANCE_NAME}_Initialize (void)

  Summary:
    Initialization function for the ${RNG_INSTANCE_NAME} peripheral

  Description:
    This function initializes the ${RNG_INSTANCE_NAME} peripheral with user input 
	from the configurator.

  Parameters:
    void

  Returns:
    void
*/
void ${RNG_INSTANCE_NAME}_Initialize (void);

// *****************************************************************************
/* Function:
   void ${RNG_INSTANCE_NAME}_LoadSet (void)

  Summary:
    LoadSet function for the ${RNG_INSTANCE_NAME} peripheral

  Description:
    This function will write the Load bit of the ${RNG_INSTANCE_NAME}CON register.

  Parameters:
    void

  Returns:
    void
*/
void ${RNG_INSTANCE_NAME}_LoadSet (void);

// *****************************************************************************
/* Function:
   bool ${RNG_INSTANCE_NAME}_LoadGet (void)

  Summary:
    LoadGet function for the ${RNG_INSTANCE_NAME} peripheral

  Description:
    This function will read the Load value of the ${RNG_INSTANCE_NAME}CON register.

  Parameters:
    void

  Returns:
    bool
*/
bool ${RNG_INSTANCE_NAME}_LoadGet (void);

// *****************************************************************************
/* Function:
   void ${RNG_INSTANCE_NAME}_Poly1Set (uint32_t poly)

  Summary:
    Poly1Set function for the ${RNG_INSTANCE_NAME} peripheral

  Description:
    This function will set the  value of the ${RNG_INSTANCE_NAME} Polynomial 1 register.

  Parameters:
    uint32_t

  Returns:
    void
*/
void ${RNG_INSTANCE_NAME}_Poly1Set (uint32_t poly);

// *****************************************************************************
/* Function:
   void ${RNG_INSTANCE_NAME}_Poly2Set (uint32_t poly)

  Summary:
    Poly2Set function for the ${RNG_INSTANCE_NAME} peripheral

  Description:
    This function will set the  value of the ${RNG_INSTANCE_NAME} Polynomial 2 register.

  Parameters:
    uint32_t

  Returns:
    void
*/
void ${RNG_INSTANCE_NAME}_Poly2Set (uint32_t poly);

// *****************************************************************************
/* Function:
   uint32_t ${RNG_INSTANCE_NAME}_Poly1Get (void)

  Summary:
    Poly1Get function for the ${RNG_INSTANCE_NAME} peripheral

  Description:
    This function will get the value of the ${RNG_INSTANCE_NAME} Polynomial 1 register.

  Parameters:
    void

  Returns:
    uint32_t
*/
uint32_t ${RNG_INSTANCE_NAME}_Poly1Get (void);

// *****************************************************************************
/* Function:
   uint32_t ${RNG_INSTANCE_NAME}_Poly2Get (void)

  Summary:
    Poly2Get function for the ${RNG_INSTANCE_NAME} peripheral

  Description:
    This function will get the value of the ${RNG_INSTANCE_NAME} Polynomial 2 register.

  Parameters:
    void

  Returns:
    uint32_t
*/
uint32_t ${RNG_INSTANCE_NAME}_Poly2Get (void);

// *****************************************************************************
/* Function:
   void ${RNG_INSTANCE_NAME}_NumGen1Set (uint32_t numgen)

  Summary:
    NumGen1Set function for the ${RNG_INSTANCE_NAME} peripheral

  Description:
    This function will set the value of the ${RNG_INSTANCE_NAME} Number Generator 1 register.

  Parameters:
    uint32_t

  Returns:
    void
*/
void ${RNG_INSTANCE_NAME}_NumGen1Set (uint32_t numgen);

// *****************************************************************************
/* Function:
   void ${RNG_INSTANCE_NAME}_NumGen2Set (uint32_t poly)

  Summary:
    NumGen1Set function for the ${RNG_INSTANCE_NAME} peripheral

  Description:
    This function will set the value of the ${RNG_INSTANCE_NAME} Number Generator 2 register.

  Parameters:
    uint32_t

  Returns:
    void
*/
void ${RNG_INSTANCE_NAME}_NumGen2Set (uint32_t poly);

// *****************************************************************************
/* Function:
   void ${RNG_INSTANCE_NAME}_NumGen1Get (uint32_t numgen)

  Summary:
    NumGen1Get function for the ${RNG_INSTANCE_NAME} peripheral

  Description:
    This function will get the value of the ${RNG_INSTANCE_NAME} Number Generator 1 register.

  Parameters:
    uint32_t

  Returns:
    void
*/
uint32_t ${RNG_INSTANCE_NAME}_NumGen1Get (void);

// *****************************************************************************
/* Function:
   void ${RNG_INSTANCE_NAME}_NumGen2Get (uint32_t poly)

  Summary:
    NumGen1Get function for the ${RNG_INSTANCE_NAME} peripheral

  Description:
    This function will get the value of the ${RNG_INSTANCE_NAME} Number Generator 2 register.

  Parameters:
    uint32_t

  Returns:
    void
*/
uint32_t ${RNG_INSTANCE_NAME}_NumGen2Get (void);

// *****************************************************************************
/* Function:
   uint32_t ${RNG_INSTANCE_NAME}_Seed1Get (void)

  Summary:
    Seed1Get function for the ${RNG_INSTANCE_NAME} peripheral

  Description:
    This function will get the value of the ${RNG_INSTANCE_NAME} Seed 1 register.

  Parameters:
    void

  Returns:
    uint32_t
*/
uint32_t ${RNG_INSTANCE_NAME}_Seed1Get (void);

// *****************************************************************************
/* Function:
   uint32_t ${RNG_INSTANCE_NAME}_Seed2Get (void)

  Summary:
    Seed1Get function for the ${RNG_INSTANCE_NAME} peripheral

  Description:
    This function will get the value of the ${RNG_INSTANCE_NAME} Seed 2 register.

  Parameters:
    void

  Returns:
    uint32_t
*/
uint32_t ${RNG_INSTANCE_NAME}_Seed2Get (void);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif

// DOM-IGNORE-END
#endif // _PLIB_${RNG_INSTANCE_NAME}_H
