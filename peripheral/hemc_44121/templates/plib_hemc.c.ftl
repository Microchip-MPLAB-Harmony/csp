/*****************************************************************************
  Company:
    Microchip Technology Inc.

  File Name:
    plib_${HEMC_INSTANCE_NAME?lower_case}.c

  Summary:
    HEMC PLIB Source file

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
#include <string.h>
#include "device.h"
#include "plib_${HEMC_INSTANCE_NAME?lower_case}.h"


// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

<#if HECC_INTERRUPT_MODE == true>
static HEMC_OBJ ${HEMC_INSTANCE_NAME?lower_case}Obj;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: HEMC Implementation
// *****************************************************************************
// *****************************************************************************

<#if USE_HSDRAM>
void SW_DelayUs(uint32_t delay)
{
    uint32_t i, count;

    /* delay * (CPU_FREQ/1000000) / 6 */
    count = delay *  (${HSDRAMC_CPU_CLK_FREQ}/1000000)/6;

    /* 6 CPU cycles per iteration */
    for (i = 0; i < count; i++)
        __NOP();
}


void ${HSDRAMC_INSTANCE_NAME}_Initialize( void )
{
    uint8_t i;
    uint16_t *pSdramBaseAddress = (uint16_t *)0x${SDRAMC_START_ADDRESS};

    /* Step 1:
     * Configure SDRAM features and timing parameters */
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_CR = HSDRAMC_CR_NC_${HSDRAMC_CR__NC} | HSDRAMC_CR_NR_${HSDRAMC_CR__NR} | HSDRAMC_CR_NB_${HSDRAMC_CR__NB}<#if HSDRAMC_CR_DBW == "16-bits"> | HSDRAMC_CR_DBW_Msk </#if><#if HSDRAMC_RMW> | HSDRAMC_CR_RMW_Msk </#if>\
                                                | HSDRAMC_CR_CAS(${HSDRAMC_CR_CAS}) ;

    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_SDR = HSDRAMC_SDR_TRAS(${HSDRAMC_SDR_TRAS}) |  HSDRAMC_SDR_TRP(${HSDRAMC_SDR_TRP}) |  HSDRAMC_SDR_TRC_TRFC(${HSDRAMC_SDR_TRC_TRFC}) \
                                                | HSDRAMC_SDR_TRCD(${HSDRAMC_SDR_TRCD}) | HSDRAMC_SDR_TWR(${HSDRAMC_SDR_TWR}) | HSDRAMC_SDR_TXSR(${HSDRAMC_SDR_TXSR});
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_CFR1= HSDRAMC_CFR1_TMRD(${HSDRAMC_CFR1_TMRD});

    /* Step 2:
     * A pause of at least 200 us must be observed before a signal toggle */
    SW_DelayUs(200);

    /* Step 3:
     * Issue a NOP command to the SDRAM device by writing to the Mode Register.
     * Read back the Mode Register and add a memory barrier assembly instruction just after the read.
     * Write to any SDRAM address to acknowledge this command. Now the clock which drives SDRAM device is enabled */

    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR = HSDRAMC_MR_MODE_NOP;
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR;
    __DMB();
    *pSdramBaseAddress = 0x0;

    /* Step 4:
     * Issue an All banks precharge command by writing to the Mode Register.
     * Read back the Mode Register and add a memory barrier assembly instruction just after the read.
     * Write to any SDRAM address to acknowledge this command. */

    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR = HSDRAMC_MR_MODE_ALLBANKS_PRECHARGE;
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR;
    __DMB();
    *pSdramBaseAddress = 0x0;

    /* Step 5:
     * Issue 8 Auto Refresh(CBR) cycles by writing to the Mode Register.
     * Read back the Mode Register and add a memory barrier assembly instruction just after the read.
     * Perform a write access to any SDRAM address 8 times. */
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR = HSDRAMC_MR_MODE_AUTO_REFRESH;
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR;
    __DMB();
    for (i = 0; i < 8; i++)
    {
        *pSdramBaseAddress = i;
    }

    /* Step 6:
     * Issue Mode Register Set(MRS) to program the parameters of the SDRAM device, in particular CAS latency and burst length */
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR = HSDRAMC_MR_MODE_LOAD_MODEREG;
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR;
    __DMB();
    *((uint16_t *)(pSdramBaseAddress + 0x${HSDRAMC_MRS_VALUE})) = 0;

    /* Step 7:
     * Transition the SDRAM to NORMAL mode. Read back the Mode
     * Register and add a memory barrier assembly instruction just after the
     * read. Perform a write access to any SDRAM address. */
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR = HSDRAMC_MR_MODE_NORMAL;
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR;
    __DMB();
    *pSdramBaseAddress = 0x0;

    /* Step 8:
     * Configure the Refresh Timer Register. */
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_TR = ${HSDRAMC_TR_COUNT};

    <#if HSDRAMC_WRITE_PROTECTION>
    /* Enable Write Protection */
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_WPMR = (HSDRAMC_WPMR_WPKEY_PASSWD | HSDRAMC_WPMR_WPEN_Msk);
    </#if>

}
</#if>

void ${HSMC_INSTANCE_NAME}_Initialize( void )
{
<#list 0..(HSMC_CHIP_SELECT_COUNT - 1) as i>
    <#assign HSMC_IN_USE = "USE_HSMC_" + i>
    <#assign HSMC_CHIP_SELECT = "HSMC_CHIP_SELECT" + i>
    <#assign HSMC_DATA_BUS_CS = "HSMC_DATA_BUS_CS" + i>
    <#assign HSMC_NWE_SETUP_CS = "HSMC_NWE_SETUP_CS" + i>
    <#assign HSMC_NCS_WR_SETUP_CS = "HSMC_NCS_WR_SETUP_CS" + i>
    <#assign HSMC_NRD_SETUP_CS = "HSMC_NRD_SETUP_CS" + i>
    <#assign HSMC_NCS_RD_SETUP_CS = "HSMC_NCS_RD_SETUP_CS" + i>
    <#assign HSMC_NWE_PULSE_CS = "HSMC_NWE_PULSE_CS" + i>
    <#assign HSMC_NCS_WR_PULSE_CS = "HSMC_NCS_WR_PULSE_CS" + i>
    <#assign HSMC_NRD_PULSE_CS = "HSMC_NRD_PULSE_CS" + i>
    <#assign HSMC_NCS_RD_PULSE_CS = "HSMC_NCS_RD_PULSE_CS" +i>
    <#assign HSMC_NWE_CYCLE_CS = "HSMC_NWE_CYCLE_CS" + i>
    <#assign HSMC_NRD_CYCLE_CS = "HSMC_NRD_CYCLE_CS" + i>
    <#assign HSMC_NWAIT_MODE_CS = "HSMC_NWAIT_MODE_CS" +i>
    <#assign HSMC_WRITE_MODE_CS = "HSMC_WRITE_ENABLE_MODE_CS" + i>
    <#assign HSMC_READ_MODE_CS = "HSMC_READ_ENABLE_MODE_CS" + i>
    <#assign HSMC_RMW = "HSMC_MODE_RMW" + i>
    <#if .vars[HSMC_IN_USE]>
    <#if .vars[HSMC_CHIP_SELECT]?has_content>

    <#if (.vars[HSMC_CHIP_SELECT] != false)>

    /* Chip Select CS${i} Timings */
    /* Setup HSMC SETUP register */
    ${HSMC_INSTANCE_NAME}_REGS->HSMC_SETUP${i}= HSMC_SETUP${i}_NWE_SETUP(${.vars[HSMC_NWE_SETUP_CS]}) | HSMC_SETUP${i}_NCS_WR_SETUP(${.vars[HSMC_NCS_WR_SETUP_CS]}) | HSMC_SETUP${i}_NRD_SETUP(${.vars[HSMC_NRD_SETUP_CS]}) | HSMC_SETUP${i}_NCS_RD_SETUP(${.vars[HSMC_NCS_RD_SETUP_CS]});

    /* Setup HSMC CYCLE register */
    ${HSMC_INSTANCE_NAME}_REGS->HSMC_CYCLE${i}= HSMC_CYCLE${i}_NWE_CYCLE(${.vars[HSMC_NWE_CYCLE_CS]}) | HSMC_CYCLE${i}_NRD_CYCLE(${.vars[HSMC_NRD_CYCLE_CS]});

    /* Setup HSMC_PULSE register */
    ${HSMC_INSTANCE_NAME}_REGS->HSMC_PULSE${i}= HSMC_PULSE${i}_NWE_PULSE(${.vars[HSMC_NWE_PULSE_CS]}) | HSMC_PULSE${i}_NCS_WR_PULSE(${.vars[HSMC_NCS_WR_PULSE_CS]}) | HSMC_PULSE${i}_NRD_PULSE(${.vars[HSMC_NRD_PULSE_CS]}) | HSMC_PULSE${i}_NCS_RD_PULSE(${.vars[HSMC_NCS_RD_PULSE_CS]});

    /* Setup HSMC MODE register */
    ${HSMC_INSTANCE_NAME}_REGS->HSMC_MODE${i}= HSMC_MODE${i}_EXNW_MODE(${.vars[HSMC_NWAIT_MODE_CS]}) | HSMC_MODE${i}_DBW(${.vars[HSMC_DATA_BUS_CS]}) <#if (.vars[HSMC_WRITE_MODE_CS] == true)>| HSMC_MODE${i}_WRITE_MODE_Msk</#if> <#if (.vars[HSMC_READ_MODE_CS] == true)>| HSMC_MODE${i}_READ_MODE_Msk</#if> <#if (.vars[HSMC_RMW] == true)>| HSMC_MODE${i}_RMW_ENABLE_Msk</#if>;
    </#if>
    </#if>
    </#if>
</#list>

<#if HSMC_WRITE_PROTECTION>
    /* Enable Write Protection */
    ${HSMC_INSTANCE_NAME}_REGS->HSMC_WPMR = (HSMC_WPMR_WPKEY_PASSWD | HSMC_WPMR_WPEN_Msk);
</#if>
}
void ${HEMC_INSTANCE_NAME}_Initialize( void )
{
<#assign HEMC_NCS0_WRITE_CONF = "CS_0_WRITE_ECC_CONF" >
<#if (.vars[HEMC_NCS0_WRITE_CONF] == false) >
    /* Read NCS0 Pin configuration for HECC */
    uint8_t eccEnableDefault = ( (${HEMC_INSTANCE_NAME}_REGS->HEMC_HECC_CR0 & HEMC_HECC_CR0_ENABLE_Msk) >> HEMC_HECC_CR0_ENABLE_Pos);
    uint8_t eccAlgoDefault = ( (${HEMC_INSTANCE_NAME}_REGS->HEMC_HECC_CR0 & HEMC_HECC_CR0_ECC12_ENABLE_Msk) >> HEMC_HECC_CR0_ECC12_ENABLE_Pos);
</#if>

    /* Enable NCS0 configuration modification through registers */
    ${HEMC_INSTANCE_NAME}_REGS->HEMC_CR_NCS0 |= HEMC_CR_NCS0_WRITE_ECC_CONF(1);

  <#list 0..5 as i>
  <#assign HEMC_TYPE = "CS_" + i + "_MEMORY_TYPE" >
  <#assign HEMC_BANK =  "CS_" + i + "_MEMORY_BANK_SIZE">
  <#assign HEMC_ADDRESS = "CS_" + i + "_MEMORY_BASE" >
  <#assign HEMC_ECC_ENABLE = "CS_" + i + "_HECC_ENABLE" >
  <#assign HEMC_ECC_BCH = "CS_" + i + "_HECC_BCH_ENABLE" >
  <#assign NUM_SPACE_MULTILINE = "${HEMC_INSTANCE_NAME}_REGS->HEMC_CR_NCS${i}"?length >
    <#if (i == 0) && (.vars[HEMC_NCS0_WRITE_CONF] == false) >
    ${HEMC_INSTANCE_NAME}_REGS->HEMC_CR_NCS${i} = HEMC_CR_NCS${i}_TYPE(${.vars[HEMC_TYPE]}) |
    <#list 1..NUM_SPACE_MULTILINE as j> </#list>   HEMC_CR_NCS${i}_ADDBASE(0x${.vars[HEMC_ADDRESS]}) |
    <#list 1..NUM_SPACE_MULTILINE as j> </#list>   HEMC_CR_NCS${i}_BANKSIZE(${.vars[HEMC_BANK]}) |
    <#list 1..NUM_SPACE_MULTILINE as j> </#list>   HEMC_CR_NCS${i}_WRITE_ECC_CONF(1) |
    <#list 1..NUM_SPACE_MULTILINE as j> </#list>   HEMC_CR_NCS${i}_ECC_ENABLE(eccEnableDefault) |
    <#list 1..NUM_SPACE_MULTILINE as j> </#list>   HEMC_CR_NCS${i}_ECC12_ENABLE(eccAlgoDefault);

    <#else>
    <#if (.vars[HEMC_ADDRESS] != "3ffff") || (i == 0) >
    ${HEMC_INSTANCE_NAME}_REGS->HEMC_CR_NCS${i} = HEMC_CR_NCS${i}_TYPE(${.vars[HEMC_TYPE]}) |
    <#list 1..NUM_SPACE_MULTILINE as j> </#list>   HEMC_CR_NCS${i}_ADDBASE(0x${.vars[HEMC_ADDRESS]}) |
    <#list 1..NUM_SPACE_MULTILINE as j> </#list>   HEMC_CR_NCS${i}_BANKSIZE(${.vars[HEMC_BANK]})<#if (i == 0)> |
    <#list 1..NUM_SPACE_MULTILINE as j> </#list>   HEMC_CR_NCS${i}_WRITE_ECC_CONF(1)</#if><#if .vars[HEMC_ECC_ENABLE]> |
    <#list 1..NUM_SPACE_MULTILINE as j> </#list>   HEMC_CR_NCS${i}_ECC_ENABLE(1)</#if><#if .vars[HEMC_ECC_BCH]> |
    <#list 1..NUM_SPACE_MULTILINE as j> </#list>   HEMC_CR_NCS${i}_ECC12_ENABLE(1)</#if>;
    </#if>
    </#if>
  </#list>
  <#if USE_HSDRAM>
    ${HSDRAMC_INSTANCE_NAME}_Initialize();
  </#if>
    ${HSMC_INSTANCE_NAME}_Initialize();

<#assign IS_RAM_INIT = false >
<#list 0..5 as i>
<#assign HEMC_ADDRESS = "CS_" + i + "_START_ADDRESS" >
<#assign HEMC_ECC_ENABLE = "CS_" + i + "_HECC_ENABLE" >
<#assign HEMC_RAM_CHECK_BIT_INIT = "CS_" + i + "_RAM_CHECK_BIT_INIT" >
<#assign HEMC_RAM_CHECK_BIT_INIT_SIZE = "CS_" + i + "_RAM_CHECK_BIT_INIT_SIZE" >
<#if (.vars[HEMC_ECC_ENABLE] == true) && (.vars[HEMC_RAM_CHECK_BIT_INIT] == true)>
    /* For RAM memories on NCS${i}, perform memory initialization of ECC check bit */
    memset((void*)(${.vars[HEMC_ADDRESS]}), 0x00, 0x${.vars[HEMC_RAM_CHECK_BIT_INIT_SIZE]});
    if (DATA_CACHE_IS_ENABLED())
    {
        DCACHE_CLEAN_INVALIDATE_BY_ADDR((void*)(${.vars[HEMC_ADDRESS]}), 0x${.vars[HEMC_RAM_CHECK_BIT_INIT_SIZE]});
    }
    <#if IS_RAM_INIT == false>
       <#assign IS_RAM_INIT = true >
    </#if>
</#if>
</#list>

<#if IS_RAM_INIT == true>
    /* Wait all memory is zeroized and clear previous interrupts when memory ECC wasn't initialized */
    __DSB();
    __ISB();
    HEMC_HECC_STATUS dummyStatus = HEMC_HeccGetStatus();
    /* Ignore the warning */
    (void)dummyStatus;
</#if>

<#if HECC_INTERRUPT_MODE == true>
    // Enable interrupts
    ${HEMC_INSTANCE_NAME}_REGS->HEMC_HECC_IER = (HEMC_HECC_IER_MEM_FIX_Msk | HEMC_HECC_IER_MEM_NOFIX_Msk);
</#if>

} /* ${HEMC_INSTANCE_NAME}_Initialize */

// *****************************************************************************
/* Function:
    void ${HEMC_INSTANCE_NAME}_HeccGetStatus(void)

   Summary:
    Get the HECC status of the ${HEMC_INSTANCE_NAME} peripheral.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    Current status of the ${HEMC_INSTANCE_NAME} peripheral.
*/
HEMC_HECC_STATUS ${HEMC_INSTANCE_NAME}_HeccGetStatus(void)
{
    return HEMC_REGS->HEMC_HECC_SR;
}

// *****************************************************************************
/* Function:
    void ${HEMC_INSTANCE_NAME}_HeccGetFailAddress(void)

   Summary:
    Get the last fail address were ECC error occurs in a HEMC memory.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    Fail address were fixable or unfixable error occured in a HEMC memory.
*/
uint32_t ${HEMC_INSTANCE_NAME}_HeccGetFailAddress(void)
{
    return HEMC_REGS->HEMC_HECC_FAILAR;
}

// *****************************************************************************
/* Function:
    void ${HEMC_INSTANCE_NAME}_HeccResetCounters(void)

   Summary:
    Reset Fix and NoFix error counters of the ${HEMC_INSTANCE_NAME} peripheral.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None
*/
void ${HEMC_INSTANCE_NAME}_HeccResetCounters(void)
{
    HEMC_REGS->HEMC_HECC_CR0 |= (HEMC_HECC_CR0_RST_FIX_CPT_Msk | HEMC_HECC_CR0_RST_NOFIX_CPT_Msk);
    HEMC_REGS->HEMC_HECC_CR1 |= (HEMC_HECC_CR1_RST_FIX_CPT_Msk | HEMC_HECC_CR1_RST_NOFIX_CPT_Msk);
    HEMC_REGS->HEMC_HECC_CR2 |= (HEMC_HECC_CR2_RST_FIX_CPT_Msk | HEMC_HECC_CR2_RST_NOFIX_CPT_Msk);
}

<#if HECC_INTERRUPT_MODE == true>
// *****************************************************************************
/* Function:
    void ${HEMC_INSTANCE_NAME}_FixCallbackRegister(HEMC_CALLBACK callback,
                                                              uintptr_t context)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given HEMC's ECC Fixable Error interrupt events occur.

  Description:
    This function sets the pointer to a client function to be called "back" when
    the given HEMC's interrupt events occur. It also passes a context value
    (usually a pointer to a context structure) that is passed into the function
    when it is called. The specified callback function will be called from the
    peripheral interrupt context.

  Precondition:
    ${HEMC_INSTANCE_NAME}_Initialize must have been called for the associated
    HEMC instance.

  Parameters:
    callback      - A pointer to a function with a calling signature defined by
                    the HEMC_CALLBACK data type. Setting this to NULL
                    disables the callback feature.

    contextHandle - A value (usually a pointer) passed (unused) into the
                    function identified by the callback parameter.

  Returns:
    None.

  Example:
    <code>
        // Refer to the description of the HEMC_CALLBACK data type for
        // example usage.
    </code>

  Remarks:
    None.
*/
void ${HEMC_INSTANCE_NAME}_FixCallbackRegister(HEMC_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback == NULL)
    {
        return;
    }

    ${HEMC_INSTANCE_NAME?lower_case}Obj.fix_callback = callback;
    ${HEMC_INSTANCE_NAME?lower_case}Obj.fix_context = contextHandle;
}

// *****************************************************************************
/* Function:
    void ${HEMC_INSTANCE_NAME}_NoFixCallbackRegister(HEMC_CALLBACK callback,
                                                              uintptr_t context)

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given HEMC's ECC Not Fixable Error interrupt events occur.

  Description:
    This function sets the pointer to a client function to be called "back" when
    the given HEMC's interrupt events occur. It also passes a context value
    (usually a pointer to a context structure) that is passed into the function
    when it is called. The specified callback function will be called from the
    peripheral interrupt context.

  Precondition:
    ${HEMC_INSTANCE_NAME}_Initialize must have been called for the associated
    HEMC instance.

  Parameters:
    callback      - A pointer to a function with a calling signature defined by
                    the HEMC_CALLBACK data type. Setting this to NULL
                    disables the callback feature.

    contextHandle - A value (usually a pointer) passed (unused) into the
                    function identified by the callback parameter.

  Returns:
    None.

  Example:
    <code>
        // Refer to the description of the HEMC_CALLBACK data type for
        // example usage.
    </code>

  Remarks:
    None.
*/
void ${HEMC_INSTANCE_NAME}_NoFixCallbackRegister(HEMC_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback == NULL)
    {
        return;
    }

    ${HEMC_INSTANCE_NAME?lower_case}Obj.nofix_callback = callback;
    ${HEMC_INSTANCE_NAME?lower_case}Obj.nofix_context = contextHandle;
}


// *****************************************************************************
/* Function:
    void ${HEMC_INSTANCE_NAME}_FIX_InterruptHandler(void)

   Summary:
    ${HEMC_INSTANCE_NAME} Peripheral Interrupt Handler.

   Description:
    This function is ${HEMC_INSTANCE_NAME} Peripheral Interrupt Handler and will
    called on every ${HEMC_INSTANCE_NAME} ECC Fixable error interrupt.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None.

   Remarks:
    The function is called as peripheral instance's interrupt handler if the
    instance interrupt is enabled. If peripheral instance's interrupt is not
    enabled user need to call it from the main while loop of the application.
*/
void ${HEMC_INSTANCE_NAME}_INTFIX_InterruptHandler(void)
{

    if (${HEMC_INSTANCE_NAME?lower_case}Obj.fix_callback != NULL)
    {
        ${HEMC_INSTANCE_NAME?lower_case}Obj.fix_callback(${HEMC_INSTANCE_NAME?lower_case}Obj.fix_context);
    }
}

// *****************************************************************************
/* Function:
    void ${HEMC_INSTANCE_NAME}_NOFIX_InterruptHandler(void)

   Summary:
    ${HEMC_INSTANCE_NAME} Peripheral Interrupt Handler.

   Description:
    This function is ${HEMC_INSTANCE_NAME} Peripheral Interrupt Handler and will
    called on every ${HEMC_INSTANCE_NAME} ECC Not Fixable error interrupt.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None.

   Remarks:
    The function is called as peripheral instance's interrupt handler if the
    instance interrupt is enabled. If peripheral instance's interrupt is not
    enabled user need to call it from the main while loop of the application.
*/
void ${HEMC_INSTANCE_NAME}_INTNOFIX_InterruptHandler(void)
{

    if (${HEMC_INSTANCE_NAME?lower_case}Obj.nofix_callback != NULL)
    {
        ${HEMC_INSTANCE_NAME?lower_case}Obj.nofix_callback(${HEMC_INSTANCE_NAME?lower_case}Obj.nofix_context);
    }
}
</#if>

/*******************************************************************************
 End of File
*/
