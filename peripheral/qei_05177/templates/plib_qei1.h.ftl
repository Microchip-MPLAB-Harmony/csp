/*******************************************************************************
  ${moduleName?lower_case} PLIB
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_${moduleName?lower_case}.h
 
  Summary:
    ${moduleName?lower_case} PLIB Header File
 
  Description:
    This file has prototype of all the interfaces provided for particular
    ${moduleName?lower_case} peripheral.
 
*******************************************************************************/
 
/*******************************************************************************
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_QEI1_H
#define PLIB_QEI1_H

// /cond IGNORE_THIS   ----> DOM will ignore these comments
/* Provide C++ Compatibility */
#ifdef __cplusplus
 
    extern "C" {
 
#endif
// /endcond

// Section: Included Files

#include <xc.h>
#include <stdbool.h>
#include <stdint.h>


// Section: Data Type Definitions

/**
* @brief    Defines the QEI operating mode
*/
typedef enum
{ 
    QEI_MODE_FREE_RUNNING = 0,   /**< Index input event does not affect position counter */
    QEI_MODE_RESET_ON_INDEX = 1, /**< Every index input event resets the position counter */
    QEI_MODE_MODULO_COUNT = 6    /**< Modulo Count mode for position counter */
}QEI_MODE;

/**
 * @brief    Defines the QEI Index Match Value states
*/
typedef enum
{
    QEI_IMV_STATE_A0B0 = 0, /**< Index Match Value State : QEA = 0 and QEB = 0 */
    QEI_IMV_STATE_A1B0 = 1, /**< Index Match Value State : QEA = 1 and QEB = 0 */
    QEI_IMV_STATE_A0B1 = 2, /**< Index Match Value State : QEA = 0 and QEB = 1 */
    QEI_IMV_STATE_A1B1 = 3, /**< Index Match Value State : QEA = 1 and QEB = 1 */
    QEI_MAX_IMV_STATE       /**< Maximum configurable Index Match Value State  */
}QEI_IMV_STATE;

// Section: QEI1 peripheral APIs

/**
 * @brief    This inline function disables the QEI1 peripheral
 *
 * @details  This function disables the instance of the QEI peripheral by clearing the
 * enable bit in the QEI1CON register.
 *
 * @pre      QEI peripheral should be initialized and enabled properly
 *
 * @param    None
 *
 * @return   None
 *
 * @b Example 
 * @code
 * QEI1_Initialize();
 * QEI1_Enable();
 * Perform QEI1 operations here
 * QEI1_Disable();
 *
 * @remarks  Stops the execution of the QEI1 peripheral
 */
inline static void ${moduleName}_Disable(void)
{
    ${moduleName}CONbits.ON = 0;        
}
    
/**
 * @brief    This inline function enables the QEI1 peripheral
 *
 * @details  This function enables the instance of the QEI peripheral by setting the
 * enable bit in the QEI1CON register. Starts the execution of the QEI1 peripheral
 *
 * @pre      QEI peripheral should be initialized properly
 *
 * @param    None
 *
 * @return   None 
 * 
 * @b Example
 * @code
 * QEI1_Initialize();
 * QEI1_Enable();
 * Perform QEI1 operations here
 *
 * @remarks  None
 */
inline static void  ${moduleName}_Enable(void)
{
    ${moduleName}CONbits.ON = 1;        
}

/**
 * @brief    This inline function reads the position count value
 *
 * @details  This function reads the position count value from the POS1CNT register
 *
 * @pre      QEI peripheral should be initialized and enabled properly
 *
 * @param    None
 *
 * @return   None  
 *
 * @b Example
 * @code
 * QEI1_Initialize();
 * QEI1_Enable();
 * QEI1_PositionCountRead();
 *
 * @remarks  None
 */
inline static uint32_t ${moduleName}_PositionCountRead(void)
{
    return POS1CNT;
}

/**
 * @brief    This inline function returns the 16-bit position count value
 *
 * @details  This function reads the 16 LSB value from the POS1CNT register
 *
 * @pre      QEI peripheral should be initialized and enabled properly 
 *
 * @param    none
 *
 * @return   Returns the LSB 16 bits of the QEI1 position 
 *           count register.
 *
 * @b Example 
 * @code
 * QEI1_Initialize();
 * QEI1_Enable();
 * QEI1_PositionCount16bitRead();
 *
 * @remarks None
 */
inline static uint16_t ${moduleName}_PositionCount16bitRead(void)
{
    return (uint16_t)POS1CNT;
}

/**
 * @brief      This inline function sets the QEI1 position count value
 *
 * @details    This inline function writes to the POS1CNT register of the QEI1 peripheral
 *
 * @pre        QEI peripheral should be initialized and enabled properly
 *
 * @param[in]  positionCount - 32-bit position count value 
 *
 * @return     None 
 * @b Example
 * @code
 * QEI1_Initialize();
 * QEI1_Enable(); 
 * QEI1_PositionCountWrite();
 *
 * @remarks    None
 */
inline static void ${moduleName}_PositionCountWrite(uint32_t positionCount)
{
    POS1CNT = positionCount; 
}

/**
 * @brief      This inline function sets the 32bit modulo count value
 *
 * @details    This function sets the 32 bit modulo count value when QEI1 is configured to
 * operate in 'Modulo Count' mode. The lower bound controlled by the QEILEC register is set to 0.
 *
 * @pre        QEI peripheral should be initialized and enabled properly
 *
 * @param[in]  countsPerRevolution - Modulus number of counts per wraparound  
 *
 * @return     None 
 *
 * @b Example
 * @code
 * QEI1_Initialize();
 * QEI1_Enable();
 * QEI1_ModuloRangeSet(0xA);
 *
 * @remarks    QEI1 should be operating in Modulo Count mode. 
 */
inline static void ${moduleName}_ModuloRangeSet(uint32_t countsPerRevolution)
{
    uint32_t maxCount = countsPerRevolution - (uint32_t)1;
    ${moduleName}LEC = 0;
    ${moduleName}GEC = maxCount;
}

/**
 * @brief    This inline function gets the status of QEI input phase swap configuration
 *
 * @details  This function returns true if the QEA and QEB inputs were swapped before
 * decoder logic and false otherwise
 *
 * @pre      QEI peripheral should be initialized and enabled properly
 *
 * @param    None
 *
 * @return   true   - Phase inputs are swapped
 * @return   false  - Phase inputs are not swapped
 *
 * @b Example
 * @code
 * QEI1_Initialize();
 * QEI1_Enable();
 * QEI1_PhaseInputSwappedGet();
 *
 * @remarks  None
 */
inline static bool ${moduleName}_PhaseInputSwappedGet(void)
{
    return (bool)${moduleName}IOCbits.SWPAB;
}

/**
 * @brief      This inline function sets whether the QEA and QEB pins are swapped
 *
 * @details    This function enables swapping of QEA and QEB input pins before entering 
 * decoder logic 
 *
 * @pre        QEI peripheral should be initialized and enabled properly
 *
 * @param[in]  swapEnabled - specifies whether QEA and QEB pins need 
 * to be swapped prior to quadrature decoder logic  
 *
 * @return     None
 *
 * @b Example
 * @code
 * QEI1_Initialize();
 * QEI1_Enable();
 * QEI1_PhaseInputSwappedSet(true);
 *
 * @remarks    None 
 */
inline static void ${moduleName}_PhaseInputSwappedSet(bool swapEnabled)
{

    if (swapEnabled)
    {
        ${moduleName}IOCbits.SWPAB = 1;
    }
    else
    {
        ${moduleName}IOCbits.SWPAB = 0;   
    }  
}

/**
 * @brief    This inline function sets the QEI position counter input capture 
 *
 * @details  This inline function sets the QCAPEN bit of the QEI1IOC register. Enabling this
 * stores the value of POS1CNT upon an index match event.
 *
 * @pre      QEI peripheral should be initialized and enabled properly
 *
 * @param    None
 *
 * @return   None  
 *
 * @b Example
 * @code
 * QEI1_Initialize();
 * QEI1_Enable();
 * QEI1_PositionCaptureEnable();
 *
 * @remarks  None
 */
inline static void ${moduleName}_PositionCaptureEnable(void)
{
    ${moduleName}IOCbits.QCAPEN = 1;
}
/**
 * @brief    This inline function deasserts the QEI position counter input capture 
 *
 * @details  This inline function clears the QCAPEN bit of the QEI1IOC register. Disabling this
 * will not store the value of POS1CNT upon an index match event.
 *
 * @pre      QEI peripheral should be initialized and enabled properly
 *
 * @param    None
 *
 * @return   None 
 * 
 * @b Example
 * @code
 * QEI1_Initialize();
 * QEI1_Enable();
 * QEI1_PositionCaptureDisable();
 *
 * @remarks  None
 */
inline static void ${moduleName}_PositionCaptureDisable(void)
{
    ${moduleName}IOCbits.QCAPEN = 0;
}

/**
 * @brief    This inline function reads the 32-bit position capture value.
 *
 * @details  This inline function reads the 32-bit position capture value from the
 * QEI1GEC 32 bit register.
 *
 * @pre      QEI peripheral should be initialized and enabled properly
 *
 * @param    None
 *
 * @return   Returns position capture value
 *
 * @b Example
 * @code
 * QEI1_Initialize();
 * QEI1_Enable();
 * QEI1_PositionCaptureGet();
 *
 * @remarks  None
 */
inline static uint32_t ${moduleName}_PositionCaptureGet(void)
{
    return ${moduleName}GEC;
}

/**
 * @brief    This inline function returns the 16-bit position capture value
 *
 * @details  This inline function returns the 16-bit position capture value
 * from QEI1GEC position count capture register
 *
 * @pre      QEI peripheral should be initialized and enabled properly
 *
 * @param    None
 *
 * @return   Returns the LSB 16 bits of position capture value
 *
 * @b Example
 * @code
 * QEI1_Initialize();
 * QEI1_Enable();
 * QEI1_PositionCapture16bitGet();
 *
 * @remarks  None
 */
inline static uint16_t ${moduleName}_PositionCapture16bitGet(void)
{
    return (uint16_t)${moduleName}GEC;
}

/**
 * @brief      This inline function initializes the 32 bit position capture register value
 *
 * @details    This inline function writes to the 32 bit QEI1GEC register
 *
 * @pre        QEI peripheral should be initialized and enabled properly
 *
 * @param[in]  initValue - 32 bit position capture register value  
 *
 * @return     None 
 *
 * @b Example
 * @code
 * QEI1_Initialize();
 * QEI1_Enable();
 * QEI1_PositionCaptureSet();
 *
 * @remarks    None 
 */
inline static void ${moduleName}_PositionCaptureSet(uint32_t initValue)
{
    ${moduleName}GEC = initValue;
}

/**
 * @brief      This inline function sets the QEI Counter mode
 *
 * @details    This inline function sets one of the following counter modes:
 * 1. Free Running Mode
 * 2. Reset Mode
 * 3. Modulo Count Mode
 *
 * @pre        QEI peripheral should be initialized and enabled properly
 *
 * @param[in]  mode - Sets the QEI counter mode 
 *
 * @return     None  
 *
 * @b Example
 * @code
 * QEI1_Initialize();
 * QEI1_Enable();
 * QEI1_CounterModeSet(QEI_MODE_FREE_RUNNING);
 *
 * @remarks    None
 */
inline static void ${moduleName}_CounterModeSet(QEI_MODE mode)
{
    ${moduleName}CONbits.PIMOD = (uint8_t)mode;
}

/**
 * @brief      This inline function sets the QEI Index Match Value Configuration
 *
 * @details    This inline function sets on which configuration of QEA and QEB
 * an index match event will occur. The configuration options to choose from are
 * 00: QEA and QEB are both 0
 * 01: QEA is 1 and QEB is 0
 * 10: QEA is 0 and QEb is 1
 * 11: QEA and QEB are both 1
 *
 * @pre        QEI peripheral should be initialized and enabled properly
 *
 * @param[in]  mode - Sets the QEI Index Match Value
 *
 * @return     None
 *
 * @b Example
 * @code
 * QEI1_Initialize();
 * QEI1_Enable();
 * QEI1_IMVGatedValueSet(QEI_IMV_STATE_A0B0);
 *
 * @remarks    None 
 */
inline static void ${moduleName}_IMVGatedValueSet(QEI_IMV_STATE state)
{
    ${moduleName}CONbits.IMV = (uint8_t)state;
}

/** 
 * @brief           Initializes QEI peripheral
 *
 * @details         This function initializes QEI1 peripheral as configured
 * by the user from the MHC.
 *
 * @pre             None
 *
 * @param           None
 *
 * @return          None
 *
 * @b Example
 * @code
 * QEI1_Initialize();
 *
 * @remarks         Stops the QEI if it was already running and reinitializes it
 */
void ${moduleName}_Initialize(void);

/** 
 * @brief           De-initializes QEI peripheral
 *
 * @details         This function resets the used registers to POR values
 * configured by the user from the MHC.
 *
 * @pre             None
 *
 * @param           None
 *
 * @return          None
 * 
 * @b Example
 * @code
 * QEI1_Initialize();
 * QEI1_Enable();
 * Perform QEI1 operations here
 * QEI1_Deinitialize();
 *
 * @remarks        None
 */
void ${moduleName}_Deinitialize(void);

/* Provide C++ Compatibility */
#ifdef __cplusplus
 
    }
 
#endif
// /endcond
#endif // PLIB_QEI1_H

/**
 End of File
*/
