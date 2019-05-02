/*******************************************************************
  Company:
    Microchip Technology Inc.
    Memory System Service SMC Initialization File

  File Name:
    plib_${SMC_INSTANCE_NAME?lower_case}.c

  Summary:
    Static Memory Controller (SMC)
    This file contains the source code to initialize the SMC controller

  Description:
    SMC configuration interface
    The SMC System Memory interface provides a simple interface to manage 8-bit and 16-bit
    parallel devices.

  *******************************************************************/

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
#include "plib_${SMC_INSTANCE_NAME?lower_case}.h"
#include "device.h"

/* Function:
    void ${SMC_INSTANCE_NAME}_Initialize( void )

  Summary:
    Initializes hardware and data for the given instance of the SMC module.

  Description:
    This function initializes the SMC timings according to the external parallel 
    device requirements.

  Returns:
    None
 */
<#lt><#assign SMC_REGS = "H" + SMC_INSTANCE_NAME + "_REGS">

void 
${SMC_INSTANCE_NAME}_Initialize( void )
{
    <#lt>   // ------------------------------------------------------------------------
    <#lt>   // Disable Write Protection
    <#lt>   ${SMC_REGS}->HSMC_WPMR = HSMC_WPMR_WPKEY_PASSWD;

    <#lt>   // ------------------------------------------------------------------------
    <#lt>   // NAND Flash Controller (NFC) Configuration
    <#lt>   ${SMC_REGS}->HSMC_CFG = HSMC_CFG_PAGESIZE_${SMC_NFC_PAGE_SIZE}
    <#lt><#if SMC_NFC_WRITE_SPARE>
    <#lt>                           | HSMC_CFG_WSPARE_Msk  
    <#lt></#if>
    <#lt><#if SMC_NFC_READ_SPARE>
    <#lt>                           | HSMC_CFG_RSPARE_Msk  
    <#lt></#if>
    <#lt><#if SMC_NFC_EDGE_DETECT>
    <#lt>                           | HSMC_CFG_EDGECTRL_Msk  
    <#lt></#if>
    <#lt><#if SMC_NFC_READY_BUSY_DETECT>
    <#lt>                           | HSMC_CFG_RBEDGE_Msk  
    <#lt></#if>
    <#lt><#if 0 != SMC_NFC_DATA_TIMEOUT_CYCLE>
    <#lt>                           | HSMC_CFG_DTOCYC( ${SMC_NFC_DATA_TIMEOUT_CYCLE} )
    <#lt>                           | HSMC_CFG_DTOMUL_${SMC_NFC_DATA_TIMEOUT_MULTIPLIER}
    <#lt></#if>
    <#lt><#if 0 != SMC_NFC_SPARE_AREA_SIZE>
    <#lt>                           | HSMC_CFG_NFCSPARESIZE( ${SMC_NFC_SPARE_AREA_SIZE} )
    <#lt></#if>
    <#lt>                           ;
    <#lt><#if SMC_NFC_CONTROLLER_ENABLE>
    <#lt>   // enable NAND Flash controller
    <#lt>   ${SMC_REGS}->HSMC_CTRL = HSMC_CTRL_NFCEN_Msk;
    <#lt><#else>
    <#lt>   // disable NAND Flash controller
    <#lt>   ${SMC_REGS}->HSMC_CTRL = HSMC_CTRL_NFCDIS_Msk;
    <#lt></#if>

    <#lt>   ${SMC_REGS}->HSMC_ADDR = HSMC_ADDR_ADDR_CYCLE0( ${SMC_NFC_ADDRESS_CYCLE_0} ); 
    
    <#lt>   ${SMC_REGS}->HSMC_BANK = ${SMC_NFC_BANK_ADDRESS}; 
    
    <#lt>   // ------------------------------------------------------------------------
    <#lt>   // Programmable Multi-bit Error Correction Code
    <#lt>   ${SMC_REGS}->HSMC_PMECCFG = HSMC_PMECCFG_BCH_ERR_${SMC_PMECC_ERROR_CORRECTION_CAPABILITY}
    <#lt><#if "SECTORSZ1" == SMC_PMECC_SECTOR_SIZE>
        <#lt>                               | HSMC_PMECCFG_SECTORSZ_Msk
    <#lt></#if>
    <#lt>                               | HSMC_PMECCFG_PAGESIZE_${SMC_PMECC_SECTORS_PER_PAGE}
    <#lt><#if SMC_PMECC_NAND_WRITE_ACCESS>
        <#lt>                               | HSMC_PMECCFG_NANDWR_Msk
    <#lt></#if>
    <#lt><#if SMC_PMECC_SPARE_AREA_ENABLE>
        <#lt>                               | HSMC_PMECCFG_SPAREEN_Msk
    <#lt></#if>
    <#lt><#if SMC_PMECC_AUTOMATIC_MODE_ENABLE>
        <#lt>                               | HSMC_PMECCFG_AUTO_Msk
    <#lt></#if>
    <#lt>                               ;
    <#lt>   // PMECC Spare Area Size
    <#lt>   ${SMC_REGS}->HSMC_PMECCSAREA = HSMC_PMECCSAREA_SPARESIZE( ${SMC_PMECC_SPARE_AREA_SIZE} );
    <#lt>   // PMECC Start Address
    <#lt>   ${SMC_REGS}->HSMC_PMECCSADDR = HSMC_PMECCSADDR_STARTADDR( ${SMC_PMECC_START_ADDRESS} );
    <#lt>   // PMECC End Address
    <#lt>   ${SMC_REGS}->HSMC_PMECCEADDR = HSMC_PMECCEADDR_ENDADDR( ${SMC_PMECC_END_ADDRESS} );
    <#lt><#if SMC_PMECC_ENABLE>
        <#lt>   // Enable PMECC
        <#lt>   ${SMC_REGS}->HSMC_PMECCTRL = HSMC_PMECCTRL_ENABLE_Msk;
    <#lt><#else>
        <#lt>   // Disable PMECC
        <#lt>   ${SMC_REGS}->HSMC_PMECCTRL = HSMC_PMECCTRL_DISABLE_Msk;
    <#lt></#if>

    <#lt>   // ------------------------------------------------------------------------
    <#lt>   // PMECC Error Location
    <#lt><#if "SECTORSZ1" == SMC_PMECC_ERROR_LOCATION_SECTOR_SIZE>
        <#lt>   ${SMC_REGS}->HSMC_ELCFG = HSMC_ELCFG_SECTORSZ_Msk;
    <#lt></#if>
    <#lt><#if SMC_PMECC_ERROR_LOCATION_DISABLE>
        <#lt>   ${SMC_REGS}->HSMC_ELDIS = HSMC_ELDIS_Msk;
    <#lt><#else>
        <#lt>   ${SMC_REGS}->HSMC_ELEN = HSMC_ELEN_ENINIT( ${SMC_PMECC_ERROR_LOCATION_ENABLE_CODEWORD} );
    <#lt></#if>

    <#lt>   // ------------------------------------------------------------------------
    <#lt>   // Chip Selection and Settings
    <#lt><#list 0..(SMC_CS_COUNT - 1) as ii>
        <#lt><#assign SMC_CHIP_SELECT_ENABLE =      "SMC_CHIP_SELECT_ENABLE" + ii>
        <#lt><#assign SMC_SETUP_NCS_RD =            "SMC_SETUP_NCS_RD" + ii>
        <#lt><#assign SMC_SETUP_NRD =               "SMC_SETUP_NRD" + ii>
        <#lt><#assign SMC_SETUP_NCS_WR =            "SMC_SETUP_NCS_WR" + ii>
        <#lt><#assign SMC_SETUP_NWE =               "SMC_SETUP_NWE" + ii>
        <#lt><#assign SMC_PULSE_NCS_RD =            "SMC_PULSE_NCS_RD" + ii>
        <#lt><#assign SMC_PULSE_NRD =               "SMC_PULSE_NRD" + ii>
        <#lt><#assign SMC_PULSE_NCS_WR =            "SMC_PULSE_NCS_WR" + ii>
        <#lt><#assign SMC_PULSE_NWE =               "SMC_PULSE_NWE" + ii>
        <#lt><#assign SMC_CYCLE_NRD =               "SMC_CYCLE_NRD" + ii>
        <#lt><#assign SMC_CYCLE_NWE =               "SMC_CYCLE_NWE" + ii>
        <#lt><#assign SMC_TIMINGS_NFSEL =           "SMC_TIMINGS_NFSEL" + ii>
        <#lt><#assign SMC_TIMINGS_TWB =             "SMC_TIMINGS_TWB" + ii>
        <#lt><#assign SMC_TIMINGS_TRR =             "SMC_TIMINGS_TRR" + ii>
        <#lt><#assign SMC_TIMINGS_OCMS =            "SMC_TIMINGS_OCMS" + ii>
        <#lt><#assign SMC_TIMINGS_TAR =             "SMC_TIMINGS_TAR" + ii>
        <#lt><#assign SMC_TIMINGS_TADL =            "SMC_TIMINGS_TADL" + ii>
        <#lt><#assign SMC_TIMINGS_TCLR =            "SMC_TIMINGS_TCLR" + ii>
        <#lt><#assign SMC_MODE_TDF_MODE =           "SMC_MODE_TDF_MODE" + ii>
        <#lt><#assign SMC_MODE_TDF_CYCLES =         "SMC_MODE_TDF_CYCLES" + ii>
        <#lt><#assign SMC_MODE_DBW =                "SMC_MODE_DBW" + ii>
        <#lt><#assign SMC_MODE_BAT =                "SMC_MODE_BAT" + ii>
        <#lt><#assign SMC_MODE_NWAIT =              "SMC_MODE_NWAIT" + ii>
        <#lt><#assign SMC_MODE_WRITE_MODE =         "SMC_MODE_WRITE_MODE" + ii>
        <#lt><#assign SMC_MODE_READ_MODE =          "SMC_MODE_READ_MODE" + ii>
        <#lt>
        <#lt><#if .vars[SMC_CHIP_SELECT_ENABLE]?has_content>
            <#lt><#if (.vars[SMC_CHIP_SELECT_ENABLE] != false)>
                <#lt>   // ***** SMC CS${ii} *****
                <#lt>   // Setup Register
                <#lt>   ${SMC_REGS}->SMC_CS_NUMBER[ ${ii} ].HSMC_SETUP = HSMC_SETUP_NCS_RD_SETUP( ${.vars[SMC_SETUP_NCS_RD]} )
                <#lt>                                           | HSMC_SETUP_NRD_SETUP(     ${.vars[SMC_SETUP_NRD]} )
                <#lt>                                           | HSMC_SETUP_NCS_WR_SETUP(  ${.vars[SMC_SETUP_NCS_WR]} )
                <#lt>                                           | HSMC_SETUP_NWE_SETUP(     ${.vars[SMC_SETUP_NWE]} )
                <#lt>                                           ;
                <#lt>   // Pulse Register
                <#lt>   ${SMC_REGS}->SMC_CS_NUMBER[ ${ii} ].HSMC_PULSE = HSMC_PULSE_NCS_RD_PULSE( ${.vars[SMC_PULSE_NCS_RD]} )
                <#lt>                                           | HSMC_PULSE_NRD_PULSE(     ${.vars[SMC_PULSE_NRD]} )
                <#lt>                                           | HSMC_PULSE_NCS_WR_PULSE(  ${.vars[SMC_PULSE_NCS_WR]} )
                <#lt>                                           | HSMC_PULSE_NWE_PULSE(     ${.vars[SMC_PULSE_NWE]} )
                <#lt>                                           ;
                <#lt>   // Cycle Register
                <#lt>   ${SMC_REGS}->SMC_CS_NUMBER[ ${ii} ].HSMC_CYCLE = HSMC_CYCLE_NRD_CYCLE( ${.vars[SMC_CYCLE_NRD]} )
                <#lt>                                           | HSMC_CYCLE_NWE_CYCLE( ${.vars[SMC_CYCLE_NWE]} )
                <#lt>                                           ;
                <#lt>   // Timings Register
                <#lt><#if .vars[SMC_TIMINGS_NFSEL]>
                <#lt>   ${SMC_REGS}->SMC_CS_NUMBER[ ${ii} ].HSMC_CYCLE = HSMC_TIMINGS_NFSEL_Msk
                <#lt>                                           | HSMC_TIMINGS_TWB(  ${.vars[SMC_TIMINGS_TWB]} )
                <#lt><#else>
                <#lt>   ${SMC_REGS}->SMC_CS_NUMBER[ ${ii} ].HSMC_CYCLE = HSMC_TIMINGS_TWB( ${.vars[SMC_TIMINGS_TWB]} )
                <#lt></#if>
                <#lt>                                           | HSMC_TIMINGS_TRR(  ${.vars[SMC_TIMINGS_TRR]} )
                <#lt><#if .vars[SMC_TIMINGS_OCMS]>
                <#lt>                                           | HSMC_TIMINGS_OCMS_Msk
                <#lt></#if>
                <#lt>                                           | HSMC_TIMINGS_TAR(  ${.vars[SMC_TIMINGS_TAR]} )
                <#lt>                                           | HSMC_TIMINGS_TADL( ${.vars[SMC_TIMINGS_TADL]} )
                <#lt>                                           | HSMC_TIMINGS_TCLR( ${.vars[SMC_TIMINGS_TCLR]} )
                <#lt>                                           ;
                <#lt>   // Mode Register
                <#lt><#if (.vars[SMC_MODE_TDF_MODE] == true)>
                    <#lt>    ${SMC_REGS}->SMC_CS_NUMBER[ ${ii} ].HSMC_MODE = HSMC_MODE_TDF_CYCLES_Msk
                    <#lt>                                           | HSMC_MODE_TDF_CYCLES( ${.vars[SMC_MODE_TDF_CYCLES]} )
                    <#lt>                                           | HSMC_MODE_DBW_${.vars[SMC_MODE_DBW]}
                <#lt><#else>
                    <#lt>    ${SMC_REGS}->SMC_CS_NUMBER[ ${ii} ].HSMC_MODE = HSMC_MODE_DBW_${.vars[SMC_MODE_DBW]}
                <#lt></#if>
                <#lt>                                           | HSMC_MODE_BAT_${.vars[SMC_MODE_BAT]}
                <#lt>                                           | HSMC_MODE_EXNW_MODE_${.vars[SMC_MODE_NWAIT]}
                <#lt><#if (.vars[SMC_MODE_WRITE_MODE] == 'NWE_CTRL')>
                    <#lt>                                           | HSMC_MODE_WRITE_MODE_Msk
                <#lt></#if>
                <#lt><#if (.vars[SMC_MODE_READ_MODE] == 'NRD_CTRL')>
                    <#lt>                                           | HSMC_MODE_READ_MODE_Msk
                <#lt></#if>
                <#lt>                                           ;
            <#lt></#if>
        <#lt></#if>
    <#lt></#list>
    <#lt><#if SMC_OCMS_SCRAMBLING_ENABLE || SMC_OCMS_SRAM_SCRAMBLING_ENABLE>
    
        <#lt>   // ------------------------------------------------------------------------
        <#lt>   // Off Chip Memory Scrambling
        <#lt>   // Note: corresponding OCMS bit in HSMC_TIMINGS register is required
        <#lt>   ${SMC_REGS}->HSMC_OCMS = 0
        <#lt><#if SMC_OCMS_SCRAMBLING_ENABLE>
            <#lt>                           | HSMC_OCMS_SMSE_Msk        // SMC off chip scrambling
        <#lt></#if>
        <#lt><#if SMC_OCMS_SRAM_SCRAMBLING_ENABLE>
            <#lt>                           | HSMC_OCMS_SRSE_Msk        // NFC Internal SRAM scrambling
        <#lt></#if>
        <#lt>                               ;
        <#lt>   ${SMC_REGS}->HSMC_KEY1 = 0x${SMC_KEY1};
        <#lt>   ${SMC_REGS}->HSMC_KEY2 = 0x${SMC_KEY2};
    <#lt></#if>
    <#lt><#if SMC_WRITE_PROTECTION>

        <#lt>   // ------------------------------------------------------------------------
        <#lt>   // Set Write Protection
        <#lt>   ${SMC_REGS}->HSMC_WPMR = (HSMC_WPMR_WPKEY_PASSWD | HSMC_WPMR_WPEN_Msk);
    <#lt></#if>
}

/*******************************************************************************
 End of File
*/
