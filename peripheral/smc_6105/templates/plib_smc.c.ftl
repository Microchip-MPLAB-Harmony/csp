/*******************************************************************************
  Company:
    Microchip Technology Inc.
    Memory System Service - SMC Initialization File

  File Name:
    plib_${SMC_INSTANCE_NAME?lower_case}.c

  Summary:
    Static Memory Controller, SMC.
    This file contains the source code to initialize the SMC_6498 controller

  Description:
    SMC configuration interface
    The SMC System Memory interface provides a simple interface to manage 8-bit
    and 16-bit parallel devices.

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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
#include "plib_${SMC_INSTANCE_NAME?lower_case}.h"
#include "device.h"
#include <stddef.h>         // NULL

<#if SMC_SRIER_SRIE == true>
    <#lt>typedef struct
    <#lt>{
    <#lt>    SMC_CALLBACK        callback; 
    <#lt>    uintptr_t           context;
    <#lt>} SMC_CALLBACK_OBJECT;
    
</#if>
<#if PMECC_IER_ERRIE == true>
    <#lt>typedef struct
    <#lt>{
    <#lt>    PMECC_CALLBACK      callback; 
    <#lt>    uintptr_t           context;
    <#lt>} PMECC_CALLBACK_OBJECT;
    
</#if>
<#if PMERRLOC_ELIER_DONE == true>
    <#lt>typedef struct
    <#lt>{
    <#lt>    PMERRLOC_CALLBACK   callback; 
    <#lt>    uintptr_t           context;
    <#lt>} PMERRLOC_CALLBACK_OBJECT;
    
</#if>
static void ${PMECC_INSTANCE_NAME}_Initialize( void );
static void ${PMERRLOC_INSTANCE_NAME}_Initialize( void );

// SMC =========================================================================
<#if SMC_SRIER_SRIE == true>
    <#lt>SMC_CALLBACK_OBJECT ${SMC_INSTANCE_NAME?lower_case}CallbackObj;
        
    <#lt>void ${SMC_INSTANCE_NAME}_CallbackRegister( SMC_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    ${SMC_INSTANCE_NAME?lower_case}CallbackObj.callback = callback;
    <#lt>    ${SMC_INSTANCE_NAME?lower_case}CallbackObj.context =  context;
    <#lt>}

    <#lt>void ${SMC_INSTANCE_NAME}_InterruptHandler( void )
    <#lt>{
    <#lt>    // Capture and clear interrupt status
    <#lt>    uint32_t interruptStatus = ${SMC_INSTANCE_NAME}_REGS->SMC_WPSR;

    <#lt>    if( interruptStatus && (${SMC_INSTANCE_NAME?lower_case}CallbackObj.callback != NULL) )
    <#lt>    {
    <#lt>        ${SMC_INSTANCE_NAME?lower_case}CallbackObj.callback( ${SMC_INSTANCE_NAME?lower_case}CallbackObj.context, interruptStatus );
    <#lt>    }
    <#lt>}

</#if>
/*  Function:
        void ${SMC_INSTANCE_NAME}_Initialize( void )

    Summary:
        Initializes hardware and data for the given instance of the SMC module.

    Description:
        This function initializes the SMC timings according to the external
        parallel device requirements.

    Returns:
        None
*/
void ${SMC_INSTANCE_NAME}_Initialize( void )
{
    // Write protection disable
    ${SMC_INSTANCE_NAME}_REGS->SMC_WPMR = SMC_WPMR_WPKEY_PASSWD;

    <#assign INDENT = ""?right_pad(38)>
    <#list 0..(SMC_CS_COUNT - 1) as ii>
        <#assign SMC_CS_ENABLE =        "SMC_CS_ENABLE_" + ii>
        <#assign SMC_MODE_DBW =         "SMC_MODE_DBW_" + ii>
        <#assign SMC_NWE_SETUP =        "SMC_NWE_SETUP_" + ii>
        <#assign SMC_NCS_WR_SETUP =     "SMC_NCS_WR_SETUP_" + ii>
        <#assign SMC_NRD_SETUP =        "SMC_NRD_SETUP_" + ii>
        <#assign SMC_NCS_RD_SETUP =     "SMC_NCS_RD_SETUP_" + ii>
        <#assign SMC_NWE_PULSE =        "SMC_NWE_PULSE_" + ii>
        <#assign SMC_NCS_WR_PULSE =     "SMC_NCS_WR_PULSE_" + ii>
        <#assign SMC_NRD_PULSE =        "SMC_NRD_PULSE_" + ii>
        <#assign SMC_NCS_RD_PULSE =     "SMC_NCS_RD_PULSE_" + ii>
        <#assign SMC_NWE_CYCLE =        "SMC_NWE_CYCLE_" + ii>
        <#assign SMC_NRD_CYCLE =        "SMC_NRD_CYCLE_" + ii>
        <#assign SMC_MODE_PS =          "SMC_MODE_PS_" + ii>
        <#assign SMC_MODE_TDF_MODE =    "SMC_MODE_TDF_MODE_" + ii>
        <#assign SMC_MODE_TDF_CYCLES =  "SMC_MODE_TDF_CYCLES_" + ii>
        <#assign SMC_MODE_EXNW_MODE =   "SMC_MODE_EXNW_MODE_" + ii>
        <#assign SMC_MODE_PMEN =        "SMC_MODE_PMEN_" + ii>
        <#assign SMC_OCMS_CSSE_MASK =   "SMC_OCMS_" + ii>
        <#assign SMC_MODE_WRITE_MODE =  "SMC_MODE_WRITE_MODE_" + ii>
        <#assign SMC_MODE_READ_MODE =   "SMC_MODE_READ_MODE_" + ii>
        <#assign SMC_MODE_BAT =         "SMC_MODE_BAT_" + ii>
        <#if .vars[SMC_CS_ENABLE]?has_content>
            <#lt><#if (.vars[SMC_CS_ENABLE] != false)>
                <#lt>    // Chip Select ${ii} --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 
                <#lt>    // Configure SETUP register
                <#lt>    ${SMC_INSTANCE_NAME}_REGS->SMC_CS_NUMBER[ ${ii} ].SMC_SETUP = SMC_SETUP_NWE_SETUP( ${.vars[SMC_NWE_SETUP]} ) 
                <#lt>    ${INDENT}| SMC_SETUP_NCS_WR_SETUP( ${.vars[SMC_NCS_WR_SETUP]} ) 
                <#lt>    ${INDENT}| SMC_SETUP_NRD_SETUP( ${.vars[SMC_NRD_SETUP]} ) 
                <#lt>    ${INDENT}| SMC_SETUP_NCS_RD_SETUP( ${.vars[SMC_NCS_RD_SETUP]} )
                <#lt>    ${INDENT};
                <#lt>    // Configure CYCLE register
                <#lt>    ${SMC_INSTANCE_NAME}_REGS->SMC_CS_NUMBER[ ${ii} ].SMC_CYCLE = SMC_CYCLE_NWE_CYCLE( ${.vars[SMC_NWE_CYCLE]} ) 
                <#lt>    ${INDENT}| SMC_CYCLE_NRD_CYCLE( ${.vars[SMC_NRD_CYCLE]} )
                <#lt>    ${INDENT};
                <#lt>    // Configure PULSE register
                <#lt>    ${SMC_INSTANCE_NAME}_REGS->SMC_CS_NUMBER[ ${ii} ].SMC_PULSE = SMC_PULSE_NWE_PULSE( ${.vars[SMC_NWE_PULSE]} ) 
                <#lt>    ${INDENT}| SMC_PULSE_NCS_WR_PULSE( ${.vars[SMC_NCS_WR_PULSE]} ) 
                <#lt>    ${INDENT}| SMC_PULSE_NRD_PULSE( ${.vars[SMC_NRD_PULSE]} ) 
                <#lt>    ${INDENT}| SMC_PULSE_NCS_RD_PULSE( ${.vars[SMC_NCS_RD_PULSE]} )
                <#lt>    ${INDENT};
                <#lt>    // Configure MODE register
                <#lt>    ${SMC_INSTANCE_NAME}_REGS->SMC_CS_NUMBER[ ${ii} ].SMC_MODE = ${.vars[SMC_MODE_EXNW_MODE]}
                <#lt><#if .vars[SMC_MODE_PMEN] == true>
                    <#lt>    ${INDENT}| ${.vars[SMC_MODE_PS]}
                    <#lt>    ${INDENT}| SMC_MODE_PMEN_Msk
                <#lt></#if> 
                <#lt><#if .vars[SMC_MODE_TDF_MODE] == true>
                    <#lt>    ${INDENT}| SMC_MODE_TDF_MODE_Msk 
                    <#lt>    ${INDENT}| SMC_MODE_TDF_CYCLES( ${.vars[SMC_MODE_TDF_CYCLES]} )
                <#lt></#if>
                <#lt>    ${INDENT}| ${.vars[SMC_MODE_DBW]} 
                <#lt>    ${INDENT}| ${.vars[SMC_MODE_BAT]}
                <#lt>    ${INDENT}| ${.vars[SMC_MODE_WRITE_MODE]}
                <#lt>    ${INDENT}| ${.vars[SMC_MODE_READ_MODE]}
                <#lt>    ${INDENT};
            <#lt></#if>
        </#if>
    </#list>
    <#lt>    //- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 
    <#compress>
        <#assign SMC_OCMS_CSxSE = "">
        <#list 0..(SMC_OCMS_CSxSE_COUNT - 1) as ii>
            <#assign ENABLE = "SMC_OCMS_CS" + ii + "SE">
            <#if .vars[ENABLE] == true>
                <#if SMC_OCMS_CSxSE != "">
                    <#assign SMC_OCMS_CSxSE = SMC_OCMS_CSxSE + " | " + ENABLE + "_Msk">
                <#else>
                    <#assign SMC_OCMS_CSxSE = ENABLE + "_Msk">
                </#if>
            </#if>
        </#list>
    </#compress>
    <#assign INDENT = ""?right_pad(20)>
    <#if SMC_OCMS_CSxSE != "">
        <#lt>    // Configure scrambling key and enable scrambling
        <#lt>    ${SMC_INSTANCE_NAME}_REGS->SMC_KEY1 = 0x${SMC_KEY1};
        <#lt>    ${SMC_INSTANCE_NAME}_REGS->SMC_KEY2 = 0x${SMC_KEY2};
        <#lt>    ${SMC_INSTANCE_NAME}_REGS->SMC_OCMS = ${SMC_OCMS_CSxSE}
        <#lt>    ${INDENT}| SMC_OCMS_SMSE_Msk
        <#lt>    ${INDENT};
    </#if>
    <#if SMC_OCMS_TAMPCLR == true>
        <#lt>    // Tampering will clear the keys even if off chip scrambling is not enabled
        <#lt>    ${SMC_INSTANCE_NAME}_REGS->SMC_OCMS |= SMC_OCMS_TAMPCLR_Msk;
    <#else>
        <#lt>    // Tampering does not clear keys
    </#if>
    <#if SMC_SRIER_SRIE == true>
        <#lt>    // Clear then enable safety report interrupt
        <#lt>    (void) ${SMC_INSTANCE_NAME}_REGS->SMC_WPSR;
        <#lt>    ${SMC_INSTANCE_NAME}_REGS->SMC_SRIER = SMC_SRIER_SRIE_Msk;
    <#else>
        <#lt>    // Disable safety report interrupt
        <#lt>    ${SMC_INSTANCE_NAME}_REGS->SMC_SRIER &= ~SMC_SRIER_SRIE_Msk;
    </#if>
    <#if SMC_WPMR_WPEN>
        <#lt>    // Write protection enable 
        <#lt>    ${SMC_INSTANCE_NAME}_REGS->SMC_WPMR = SMC_WPMR_WPKEY_PASSWD 
        <#lt>    ${INDENT}| SMC_WPMR_WPEN_Msk 
        <#lt>    ${INDENT};
    </#if>

    <#lt>    ${PMECC_INSTANCE_NAME}_Initialize();
    <#lt>    ${PMERRLOC_INSTANCE_NAME}_Initialize();
    <#lt>    return;
}

// PMECC =======================================================================
<#if PMECC_IER_ERRIE == true>
    <#lt>PMECC_CALLBACK_OBJECT ${PMECC_INSTANCE_NAME?lower_case}CallbackObj;
        
    <#lt>void ${PMECC_INSTANCE_NAME}_CallbackRegister( PMECC_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    ${PMECC_INSTANCE_NAME?lower_case}CallbackObj.callback = callback;
    <#lt>    ${PMECC_INSTANCE_NAME?lower_case}CallbackObj.context =  context;
    <#lt>}

    <#lt>void ${PMECC_INSTANCE_NAME}_InterruptHandler( void )
    <#lt>{
    <#lt>    // Capture and clear interrupt status
    <#lt>    uint32_t interruptStatus = ${PMECC_INSTANCE_NAME}_REGS->PMECC_ISR;

    <#lt>    if( interruptStatus && (${PMECC_INSTANCE_NAME?lower_case}CallbackObj.callback != NULL) )
    <#lt>    {
    <#lt>        ${PMECC_INSTANCE_NAME?lower_case}CallbackObj.callback( ${PMECC_INSTANCE_NAME?lower_case}CallbackObj.context, interruptStatus );
    <#lt>    }
    <#lt>}

</#if>
void ${PMECC_INSTANCE_NAME}_Initialize( void )
{
    <#assign INDENT = ""?right_pad(20)>
    <#lt>    // Disable then configure the PMECC module
    <#lt>    ${PMECC_INSTANCE_NAME}_REGS->PMECC_CTRL = PMECC_CTRL_DISABLE_Msk    // disable PMECC Module
    <#lt>    ${INDENT}| PMECC_CTRL_RST_Msk
    <#lt>    ${INDENT};
    <#lt>    // PMECC interrupt disable 
    <#lt>    ${PMECC_INSTANCE_NAME}_REGS->PMECC_IDR = PMECC_IDR_ERRID_Msk;
    <#lt>    // Configuration register
    <#lt>    ${PMECC_INSTANCE_NAME}_REGS->PMECC_CFG = ${PMECC_CFG_PAGESIZE}
    <#lt>    ${INDENT}| ${PMECC_CFG_BCH_ERR}
    <#lt><#if PMECC_CFG_AUTO>
        <#lt>    ${INDENT}| PMECC_CFG_AUTO_Msk 
    <#lt></#if>
    <#lt><#if PMECC_CFG_SPAREEN>
        <#lt>    ${INDENT}| PMECC_CFG_SPAREEN_Msk 
    <#lt></#if>
    <#lt><#if PMECC_CFG_NANDWR>
        <#lt>    ${INDENT}| PMECC_CFG_NANDWR_Msk 
    <#lt></#if>
    <#lt><#if PMECC_CFG_SECTORSZ != 0>
        <#lt>    ${INDENT}| PMECC_CFG_SECTORSZ_Msk 
    <#lt></#if>
    <#lt>    ${INDENT};
    <#lt>    // Spare area size register
    <#assign SAREA_SZ_VALUE = PMECC_SAREA_SPARESIZE - 1>
    <#lt>    ${PMECC_INSTANCE_NAME}_REGS->PMECC_SAREA = PMECC_SAREA_SPARESIZE( ${SAREA_SZ_VALUE} ); // ${PMECC_SAREA_SPARESIZE} bytes
    <#lt>    // Start address register
    <#lt>    ${PMECC_INSTANCE_NAME}_REGS->PMECC_SADDR = ${PMECC_SADDR_STARTADDR};
    <#lt>    // End address register
    <#lt>    ${PMECC_INSTANCE_NAME}_REGS->PMECC_EADDR = ${PMECC_EADDR_ENDADDR};
    <#lt>    // Clock register (value in cycles)
    <#lt>    ${PMECC_INSTANCE_NAME}_REGS->PMECC_CLK = ${PMECC_CLK_CLKCTRL};
    <#lt><#if PMECC_IER_ERRIE> <#--  Not enabling interrupt unless the module is enabled as well-->
        <#lt>    // Clear then enable PMECC interrupt
        <#lt>    (void) ${PMECC_INSTANCE_NAME}_REGS->PMECC_ISR;
        <#lt>    ${PMECC_INSTANCE_NAME}_REGS->PMECC_IER = PMECC_IER_ERRIE_Msk;
    <#lt><#else>
        <#lt>    // PMECC interrupt left disabled
    <#lt></#if>
    <#lt><#if PMECC_CTRL_ENABLE>
        <#lt>    // PMECC module enable 
        <#lt>    ${PMECC_INSTANCE_NAME}_REGS->PMECC_CTRL = PMECC_CTRL_ENABLE_Msk;
    <#lt><#else>
        <#lt>    // PMECC module left disabled
    <#lt></#if>
    
    <#lt>    return;
}

// PMERRLOC ====================================================================
<#if PMERRLOC_ELIER_DONE == true>
    <#lt>${PMERRLOC_INSTANCE_NAME}_CALLBACK_OBJECT pmerrlocCallbackObj;

    <#lt>void ${PMERRLOC_INSTANCE_NAME}_CallbackRegister( PMERRLOC_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    pmerrlocCallbackObj.callback = callback;
    <#lt>    pmerrlocCallbackObj.context =  context;
    <#lt>}

    <#lt>void ${PMERRLOC_INSTANCE_NAME}_InterruptHandler( void )
    <#lt>{
    <#lt>    // Capture and clear interrupt status
    <#lt>    uint32_t interruptStatus = ${PMERRLOC_INSTANCE_NAME}_REGS->PMERRLOC_ELISR;

    <#lt>    if( interruptStatus && (pmerrlocCallbackObj.callback != NULL) )
    <#lt>    {
    <#lt>        pmerrlocCallbackObj.callback( pmerrlocCallbackObj.context, interruptStatus );
    <#lt>    }
    <#lt>}

</#if>
void ${PMERRLOC_INSTANCE_NAME}_Initialize( void )
{
    <#assign INDENT = ""?right_pad(20)>
    <#lt>    // Disable then configure the PMERRLOC module
    <#lt>    ${PMERRLOC_INSTANCE_NAME}_REGS->PMERRLOC_ELDIS = PMERRLOC_ELDIS_DIS_Msk;   // disable PMERRLOC Module
    <#lt>    // PMERRLOC interrupt disable 
    <#lt>    ${PMERRLOC_INSTANCE_NAME}_REGS->PMERRLOC_ELIDR = PMERRLOC_ELIDR_DONE_Msk;

    <#lt><#if PMERRLOC_ELCFG_SECTORSZ != 0>
        <#lt>    // Configuration register, sector size
        <#lt>    ${PMERRLOC_INSTANCE_NAME}_REGS->PMERRLOC_ELCFG = PMERRLOC_ELCFG_SECTORSZ_Msk; 
    <#lt></#if>
    <#lt><#if PMERRLOC_ELIER_DONE == true>
        <#lt>    // clear then enable PMERRLOC interrupt
        <#lt>    (void) ${PMERRLOC_INSTANCE_NAME}_REGS->PMERRLOC_ELISR;
        <#lt>    ${PMERRLOC_INSTANCE_NAME}_REGS->PMERRLOC_ELIER = PMERRLOC_ELIER_DONE_Msk;
    <#lt><#else>
        <#lt>    // PMERRLOC interrupt left disabled
    <#lt></#if>
    
    <#lt>    return;
}

/*******************************************************************************
 End of File
*/
