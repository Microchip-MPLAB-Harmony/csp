<#assign pgxPCIPolaritySelectOptions = ["NON_INVERTED","INVERTED"]>
<#assign pgxMDCSELOptions = ["PGxDC","MDC"]>
<#assign pgxMPERSELOptions = ["PGxPER","MPER"]>
<#assign pgxMPHSELOptions = ["PGxPHASE","MPHASE"]>
<#assign pgxMSTENOptions = ["DISABLED","ENABLED"]>
<#assign pgxPWMDataRegisterUpdateModeOptions  = ["SOC","IMMEDIATE","CLIENT_SOC","CLIENT_IMMEDIATE"]>
<#assign pgxtriggerModeSelectionOptions  = ["SINGLE_TRIGGER_MODE","RETRIGGRERABLE_MODE"]>
<#assign pgxPWMStartofCycleSelectionbitOptions  = ["LOCAL_EOC","TRIG_OP_BY_PG1_OR_PG5","TRIG_OP_BY_PG2_OR_PG6","TRIG_OP_BY_PG3_OR_PG7","TRIG_OP_BY_PG4_OR_PG8","RESERVED","RESERVED","RESERVED","RESERVED","RESERVED","RESERVED","RESERVED","RESERVED","RESERVED","RESERVED","TRIG_BIT_OR_PCI_SYNC_FN_ONLY"]>
<#assign pgxPWMCLKSELbitOptions = ["NO_CLOCK", "MASTER_CLOCK_BY_MCLKSEL", "MASTER_CLOCK_DIVIDER", "MASTER_CLOCK_FREQ_SCALING"]>
<#assign pgxPWMMODSELbitOptions = ["INDEPENDENT_EDGE","VARIABLE_PHASE","INDEPENDENT_EDGE_DUAL_OUTPUT","RESERVED","CENTER_ALIGNED","DOUBLE_UPDATE_CENTER_ALIGNED","DUALEDGE_CA_ONE_UPDATE_CYCLE","DUALEDGE_CA_TWO_UPDATE_CYCLE"]>
<#assign pgxPWMPMODbitOptions = ["COMPLEMENTARY_MODE","INDEPENDENT_MODE","PUSH_PULL_MODE","RESERVED"]>
<#assign pgxPWMPOLHOptions = ["ACTIVE_HIGH","ACTIVE_LOW"]>
<#assign pgxPWMPOLLOptions = ["ACTIVE_HIGH","ACTIVE_LOW"]>
<#assign pgxPWMSWAPOptions = ["NORMAL_MAPPING","SWAPPED"]>
<#assign pgxPWMOVRENHOptions = ["PWM_GENERATOR","OVRDAT_1"]>
<#assign pgxPWMOVRENLOptions = ["PWM_GENERATOR","OVRDAT_0"]>
<#assign pgxPWMOSYNCOptions = ["SYNC_TO_LOCAL_PWM_TIMEBASE", "SYNC_IMMEDIATE", "SYNC_TO_UPDMOD", "SYNC_TO_DATA_BUFFER_UPDATE"]>
<#assign pgxADTR2EN3Options = ["DISABLED","ENABLED"]>
<#assign pgxADTR2EN2Options = ["DISABLED","ENABLED"]>
<#assign pgxADTR2EN1Options = ["DISABLED","ENABLED"]>
<#assign pgxADTR1EN3Options = ["DISABLED","ENABLED"]>
<#assign pgxADTR1EN2Options = ["DISABLED","ENABLED"]>
<#assign pgxADTR1EN1Options = ["DISABLED","ENABLED"]>
<#assign pgxPWMPCIOptions = ["PWM_GENERATOR_1","PWM_GENERATOR_2","PWM_GENERATOR_3","PWM_GENERATOR_4"]>
<#assign pgxUPDTRGOptions = ["MANUAL","PGxDC","PGxPHASE","PGxTRIGA"]>
<#assign pgxPGTRGSELOptions = ["EOC","TRIGA_COMPARE","TRIGB_COMPARE","TRIGC_COMPARE","RESERVED","RESERVED","RESERVED","RESERVED"]>
<#assign PWMClockDividerSelectionOptions  = ["1_2","1_4","1_8","1_16"]>
<#assign PWMMasterClockSelectionOptions = ["UPB_CLOCK","CLOCK_GEN_"+clkSrcGenNumber]>
/*******************************************************************************
  ${moduleNameUpperCase} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${fileNameLowerCase}.c

  Summary:
    ${moduleNameUpperCase} PLIB Source File

  Description:
    None

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

// Section: Included Files


#include "plib_${moduleNameLowerCase}.h"
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#list 1..MAX_GENERATOR_COUNT as i>
<#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
<#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
//PWM Generator x PCI Termination Polarity options
<#list pgxPCIPolaritySelectOptions as options>
    <#lt>#define PG${i}FPCI_PPS_${options}          ((uint32_t)(_PG${i}FPCI_PPS_MASK & ((uint32_t)(${options_index}) << _PG${i}FPCI_PPS_POSITION))) 
</#list>

//PGxCON MDCSEL bit
<#list pgxMDCSELOptions as options>
    <#lt>#define PG${i}CON_MDCSEL_${options}          ((uint32_t)(_PG${i}CON_MDCSEL_MASK & ((uint32_t)(${options_index}) << _PG${i}CON_MDCSEL_POSITION)))
</#list>

//PGxCON MPERSEL bit
<#list pgxMPERSELOptions as options>
    <#lt>#define PG${i}CON_MPERSEL_${options}          ((uint32_t)(_PG${i}CON_MPERSEL_MASK & ((uint32_t)(${options_index}) << _PG${i}CON_MPERSEL_POSITION)))
</#list>

//PGxCON MPHSEL bit
<#list pgxMPHSELOptions as options>
    <#lt>#define PG${i}CON_MPHSEL_${options}          ((uint32_t)(_PG${i}CON_MPHSEL_MASK & ((uint32_t)(${options_index}) << _PG${i}CON_MPHSEL_POSITION)))
</#list>

//PGxCON MSTEN bit
<#list pgxMSTENOptions as options>
    <#lt>#define PG${i}CON_MSTEN_${options}          ((uint32_t)(_PG${i}CON_MSTEN_MASK & ((uint32_t)(${options_index}) << _PG${i}CON_MSTEN_POSITION)))
</#list>

//PWM Generator x Trigger Mode Selection options
<#list pgxtriggerModeSelectionOptions as options>
    <#lt>#define PG${i}CON_TRGMOD_${options}            ((uint32_t)(_PG${i}CON_TRGMOD_MASK & ((uint32_t)(${options_index}) << _PG${i}CON_TRGMOD_POSITION))) 
</#list>

//PWM Generator x Data Register Update Modes
<#list pgxPWMDataRegisterUpdateModeOptions as options>
    <#lt>#define PG${i}CON_UPDMOD_${options}            ((uint32_t)(_PG${i}CON_UPDMOD_MASK & ((uint32_t)(${options_index}) << _PG${i}CON_UPDMOD_POSITION))) 
</#list>

//PWM Generator x Start-of-Cycle Selection bits
<#list pgxPWMStartofCycleSelectionbitOptions as options>
    <#if options != "RESERVED">
        <#lt>#define PG${i}CON_SOCS_${options}            ((uint32_t)(_PG${i}CON_SOCS_MASK & ((uint32_t)(${options_index}) << _PG${i}CON_SOCS_POSITION)))
    </#if>
</#list>

//PWM Generator x CLKSEL bits
<#list pgxPWMCLKSELbitOptions as options>
    <#lt>#define PG${i}CON_CLKSEL_${options}          ((uint32_t)(_PG${i}CON_CLKSEL_MASK & ((uint32_t)(${options_index}) << _PG${i}CON_CLKSEL_POSITION)))
</#list>

<#list pgxPWMMODSELbitOptions as options>
    <#if options != "RESERVED">
        <#lt>#define PG${i}CON_MODSEL_${options}          ((uint32_t)(_PG${i}CON_MODSEL_MASK & ((uint32_t)(${options_index}) << _PG${i}CON_MODSEL_POSITION)))
    </#if>
</#list>

//PWM Generator x PMOD bits
<#list pgxPWMPMODbitOptions as options>
    <#lt>#define PG${i}IOCON_PMOD_${options}          ((uint32_t)(_PG${i}IOCON_PMOD_MASK & ((uint32_t)(${options_index}) << _PG${i}IOCON_PMOD_POSITION)))
</#list>

//PWM Generator x POLH bit
<#list pgxPWMPOLHOptions as options>
    <#lt>#define PG${i}IOCON_POLH_${options}          ((uint32_t)(_PG${i}IOCON_POLH_MASK & ((uint32_t)(${options_index}) << _PG${i}IOCON_POLH_POSITION)))
</#list>

//PWM Generator x POLL bit
<#list pgxPWMPOLLOptions as options>
    <#lt>#define PG${i}IOCON_POLL_${options}          ((uint32_t)(_PG${i}IOCON_POLL_MASK & ((uint32_t)(${options_index}) << _PG${i}IOCON_POLL_POSITION)))
</#list>

//PWM Generator x SWAP bit
<#list pgxPWMSWAPOptions as options>
    <#lt>#define PG${i}IOCON_SWAP_${options}          ((uint32_t)(_PG${i}IOCON_SWAP_MASK & ((uint32_t)(${options_index}) << _PG${i}IOCON_SWAP_POSITION)))
</#list>

<#list pgxPWMOVRENHOptions as options>
    <#lt>#define PG${i}IOCON_OVRENH_${options}          ((uint32_t)(_PG${i}IOCON_OVRENH_MASK & ((uint32_t)(${options_index}) << _PG${i}IOCON_OVRENH_POSITION)))
</#list>

//PWM Generator x OVRENL bit
<#list pgxPWMOVRENLOptions as options>
    <#lt>#define PG${i}IOCON_OVRENL_${options}          ((uint32_t)(_PG${i}IOCON_OVRENL_MASK & ((uint32_t)(${options_index}) << _PG${i}IOCON_OVRENL_POSITION)))
</#list>

//PWM Generator x OSYNC[1:0] bits
<#list pgxPWMOSYNCOptions as options>
    <#lt>#define PG${i}IOCON_OSYNC_${options}          ((uint32_t)(_PG${i}IOCON_OSYNC_MASK & ((uint32_t)(${options_index}) << _PG${i}IOCON_OSYNC_POSITION)))
</#list>

//PGxEVT ADTR2EN3 bit
<#list pgxADTR2EN3Options as options>
    <#lt>#define PG${i}EVT_ADTR2EN3_${options}          ((uint32_t)(_PG${i}EVT_ADTR2EN3_MASK & ((uint32_t)(${options_index}) << _PG${i}EVT_ADTR2EN3_POSITION)))
</#list>

//PGxEVT ADTR2EN2 bit
<#list pgxADTR2EN2Options as options>
    <#lt>#define PG${i}EVT_ADTR2EN2_${options}          ((uint32_t)(_PG${i}EVT_ADTR2EN2_MASK & ((uint32_t)(${options_index}) << _PG${i}EVT_ADTR2EN2_POSITION)))
</#list>

//PGxEVT ADTR2EN1 bit
<#list pgxADTR2EN1Options as options>
    <#lt>#define PG${i}EVT_ADTR2EN1_${options}          ((uint32_t)(_PG${i}EVT_ADTR2EN1_MASK & ((uint32_t)(${options_index}) << _PG${i}EVT_ADTR2EN1_POSITION)))
</#list>

//PGxEVT ADTR1EN3 bit
<#list pgxADTR1EN3Options as options>
    <#lt>#define PG${i}EVT_ADTR1EN3_${options}          ((uint32_t)(_PG${i}EVT_ADTR1EN3_MASK & ((uint32_t)(${options_index}) << _PG${i}EVT_ADTR1EN3_POSITION)))
</#list>

//PGxEVT ADTR1EN2 bit
<#list pgxADTR1EN2Options as options>
    <#lt>#define PG${i}EVT_ADTR1EN2_${options}          ((uint32_t)(_PG${i}EVT_ADTR1EN2_MASK & ((uint32_t)(${options_index}) << _PG${i}EVT_ADTR1EN2_POSITION)))
</#list>

//PGxEVT ADTR1EN1 bit
<#list pgxADTR1EN1Options as options>
    <#lt>#define PG${i}EVT_ADTR1EN1_${options}          ((uint32_t)(_PG${i}EVT_ADTR1EN1_MASK & ((uint32_t)(${options_index}) << _PG${i}EVT_ADTR1EN1_POSITION)))
</#list>

//PGxEVT PWMPCI[2:0] bits
<#list pgxPWMPCIOptions as options>
    <#lt>#define PG${i}EVT_PWMPCI_${options}          ((uint32_t)(_PG${i}EVT_PWMPCI_MASK & ((uint32_t)(${options_index}) << _PG${i}EVT_PWMPCI_POSITION)))
</#list>

//PGxEVT UPDTRG[1:0] bits
<#list pgxUPDTRGOptions as options>
    <#lt>#define PG${i}EVT_UPDTRG_${options}          ((uint32_t)(_PG${i}EVT_UPDTRG_MASK & ((uint32_t)(${options_index}) << _PG${i}EVT_UPDTRG_POSITION)))
</#list>

//PGxEVT PGTRGSEL[2:0] bits
<#list pgxPGTRGSELOptions as options>
    <#if options != "RESERVED">
        <#lt>#define PG${i}EVT_PGTRGSEL_${options}          ((uint32_t)(_PG${i}EVT_PGTRGSEL_MASK & ((uint32_t)(${options_index}) << _PG${i}EVT_PGTRGSEL_POSITION)))
    </#if>
</#list>
        
    </#if>
</#list>

//PWM Clock Divider Selection options
<#list PWMClockDividerSelectionOptions as options>
    <#lt>#define PCLKCON_DIVSEL_${options}          ((uint32_t)(_PCLKCON_DIVSEL_MASK & ((uint32_t)(${options_index}) << _PCLKCON_DIVSEL_POSITION))) 
</#list>

//PWM Master Clock Selection options
<#list PWMMasterClockSelectionOptions as options>
    <#lt>#define PCLKCON_MCLKSEL_${options}           ((uint32_t)(_PCLKCON_MCLKSEL_MASK & ((uint32_t)(${options_index}) << _PCLKCON_MCLKSEL_POSITION))) 
</#list>

// Section: File specific functions

<#list 1..MAX_GENERATOR_COUNT as i>
    <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#assign PWM_GEN_INT_ENABLE = "PG" + i + "_intEnabled">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true && .vars[PWM_GEN_INT_ENABLE]?has_content && .vars[PWM_GEN_INT_ENABLE] == true>
        <#lt>volatile static PWM_GEN_EOC_EVENT_CALLBACK_OBJ pwmGen${i}CbObj;
    </#if>
</#list>

// Section: ${moduleNameUpperCase} Module APIs

void ${moduleNameUpperCase}_Initialize (void)
{
<#list 1..MAX_GENERATOR_COUNT as i>
    <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
    PG${i}CON = (PG${i}CON_MDCSEL_${pgxMDCSELOptions[.vars["PG"+i+"_PG_CON__MDCSEL"]?number]}
            |PG${i}CON_MPERSEL_${pgxMPERSELOptions[.vars["PG"+i+"_PG_CON__MPERSEL"]?number]}
            |PG${i}CON_MPHSEL_${pgxMPHSELOptions[.vars["PG"+i+"_PG_CON__MPHSEL"]?number]}
            |PG${i}CON_MSTEN_${pgxMSTENOptions[.vars["PG"+i+"_PG_CON__MSTEN"]?number]}
            |PG${i}CON_UPDMOD_${pgxPWMDataRegisterUpdateModeOptions[.vars["PG"+i+"_PG_CON__UPDMOD"]?number]}
            |PG${i}CON_TRGMOD_${pgxtriggerModeSelectionOptions[.vars["PG"+i+"_PG_CON__TRGMOD"]?number]}
            |PG${i}CON_SOCS_${pgxPWMStartofCycleSelectionbitOptions[.vars["PG"+i+"_PG_CON__SOCS"]?number]}
            |PG${i}CON_CLKSEL_${pgxPWMCLKSELbitOptions[.vars["PG"+i+"_PG_CON__CLKSEL"]?number]}
            |PG${i}CON_MODSEL_${pgxPWMMODSELbitOptions[.vars["PG"+i+"_PG_CON__MODSEL"]?number]});
    
    PG${i}IOCON = (PG${i}IOCON_PMOD_${pgxPWMPMODbitOptions[.vars["PG"+i+"_PG_IOCON__PMOD"]?number]}<#if .vars["PG"+i+"_PG_IOCON__PPSEN"]?number == 1>
            |_PG${i}IOCON_PPSEN_MASK</#if><#if .vars["PG"+i+"_PG_IOCON__PENH"]?number == 1>
            |_PG${i}IOCON_PENH_MASK</#if><#if .vars["PG"+i+"_PG_IOCON__PENL"]?number == 1>
            |_PG${i}IOCON_PENL_MASK</#if>
            |PG${i}IOCON_POLH_${pgxPWMPOLHOptions[.vars["PG"+i+"_PG_IOCON__POLH"]?number]}
            |PG${i}IOCON_POLL_${pgxPWMPOLLOptions[.vars["PG"+i+"_PG_IOCON__POLL"]?number]}
            |PG${i}IOCON_SWAP_${pgxPWMSWAPOptions[.vars["PG"+i+"_PG_IOCON__SWAP"]?number]}
            |PG${i}IOCON_OVRENH_${pgxPWMOVRENHOptions[.vars["PG"+i+"_PG_IOCON__OVRENH"]?number]}
            |PG${i}IOCON_OVRENL_${pgxPWMOVRENLOptions[.vars["PG"+i+"_PG_IOCON__OVRENL"]?number]}
            |(uint32_t)0x${.vars["PG"+i+"_PG_IOCON__OVRDAT"]} << _PG${i}IOCON_OVRDAT_POSITION
            |PG${i}IOCON_OSYNC_${pgxPWMOSYNCOptions[.vars["PG"+i+"_PG_IOCON__OSYNC"]?number]}
            |(uint32_t)0x${.vars["PG"+i+"_PG_IOCON__FLTDAT"]} << _PG${i}IOCON_FLTDAT_POSITION);
            
    PG${i}EVT = (PG${i}EVT_ADTR2EN3_${pgxADTR2EN3Options[.vars["PG"+i+"_PG_EVT__ADTR2EN3"]?number]}
            |PG${i}EVT_ADTR2EN2_${pgxADTR2EN2Options[.vars["PG"+i+"_PG_EVT__ADTR2EN2"]?number]}
            |PG${i}EVT_ADTR2EN1_${pgxADTR2EN1Options[.vars["PG"+i+"_PG_EVT__ADTR2EN1"]?number]}
            |(uint32_t)0x${.vars["PG"+i+"_ADTR1OFS"]} << _PG${i}EVT_ADTR1OFS_POSITION
            |(uint32_t)0x${.vars["PG"+i+"_ADTR1PS"]} << _PG${i}EVT_ADTR1PS_POSITION
            |PG${i}EVT_ADTR1EN3_${pgxADTR1EN3Options[.vars["PG"+i+"_PG_EVT__ADTR1EN3"]?number]}
            |PG${i}EVT_ADTR1EN2_${pgxADTR1EN2Options[.vars["PG"+i+"_PG_EVT__ADTR1EN2"]?number]}
            |PG${i}EVT_ADTR1EN1_${pgxADTR1EN1Options[.vars["PG"+i+"_PG_EVT__ADTR1EN1"]?number]}
            |PG${i}EVT_PWMPCI_${pgxPWMPCIOptions[.vars["PG"+i+"_PG_EVT__PWMPCI"]?number]}
            |PG${i}EVT_UPDTRG_${pgxUPDTRGOptions[.vars["PG"+i+"_PG_EVT__UPDTRG"]?number]}
            |PG${i}EVT_PGTRGSEL_${pgxPGTRGSELOptions[.vars["PG"+i+"_PG_EVT__PGTRGSEL"]?number]});
            
    PG${i}DC = 0x${.vars["PG"+i+"_PRIMARY_DC_REG_VAL"]}UL;
    
    PG${i}PER = 0x${.vars["PG"+i+"_PERIOD"]}UL;
    
    PG${i}PHASE = 0x${.vars["PG"+i+"_PRIMARY_PHASE_REG_VAL"]}UL;
    
    PG${i}DT = 0x${.vars["PG"+i+"_PG_DT"]}UL;
    
    PG${i}FPCI = PG${i}FPCI_PPS_${pgxPCIPolaritySelectOptions[.vars["PG"+i+"_PG_FPCI__PPS"]?number]} | (uint32_t)0x${.vars["PG"+i+"_PG_FPCI__PSS_HEX"]} << _PG${i}FPCI_PSS_POSITION;
    
    PG${i}TRIGA = 0x${.vars["PG"+i+"_PG_TRIGA"]}UL;
    
    PG${i}TRIGB = 0x${.vars["PG"+i+"_PG_TRIGB"]}UL;
    
    PG${i}TRIGC = 0x${.vars["PG"+i+"_PG_TRIGC"]}UL;
    
    </#if>
</#list>
    MDC = 0x${.vars["MASTER_PRIMARY_DC_REG_VAL"]}UL;
    
    MPER = 0x${.vars["MASTER_PERIOD"]}UL;

    MPHASE = 0x${.vars["MASTER_PHASE_REG_VAL"]}UL;

    PCLKCON = (PCLKCON_DIVSEL_${PWMClockDividerSelectionOptions[.vars["PCLKCON_PCLKCON__DIVSEL"]?number]}
            |PCLKCON_MCLKSEL_${PWMMasterClockSelectionOptions[.vars["PCLKCON_PCLKCON__MCLKSEL"]?number]});
    
<#list 1..MAX_GENERATOR_COUNT as i>
    <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#assign PWM_GEN_INT_ENABLE = "PG" + i + "_intEnabled">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true && .vars[PWM_GEN_INT_ENABLE]?has_content && .vars[PWM_GEN_INT_ENABLE] == true>
            <#lt>    /* Initialize PWM Generator ${i} EOC Event callback object */
            <#lt>    pwmGen${i}CbObj.callback = NULL;
    </#if>
</#list>

<#list 1..MAX_GENERATOR_COUNT as i>
    <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#assign PWM_GEN_INT_ENABLE = "PG" + i + "_intEnabled">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true && .vars[PWM_GEN_INT_ENABLE]?has_content && .vars[PWM_GEN_INT_ENABLE] == true>
        <#lt>    ${.vars["pg"+i+"intFlagBit"]} = 0U;
        <#lt>    ${.vars["pg"+i+"intEnableBit"]} = 1U;
    </#if>
</#list>

    
<#list 1..MAX_GENERATOR_COUNT as i>
    <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars["PG"+i+"_PG_CON__ON"]?number == 1>
        PG${i}CONbits.ON = 1U;
    </#if>
</#list>
}

void ${moduleNameUpperCase}_Deinitialize (void)
{
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
    <#lt>    PG${i}CONbits.ON = 0U;
    </#if>
</#list>

<#list 1..MAX_GENERATOR_COUNT as i>
    <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#assign PWM_GEN_INT_ENABLE = "PG" + i + "_intEnabled">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true && .vars[PWM_GEN_INT_ENABLE]?has_content && .vars[PWM_GEN_INT_ENABLE] == true>
        <#lt>    ${.vars["pg"+i+"intFlagBit"]} = 0U;
        <#lt>    ${.vars["pg"+i+"intEnableBit"]} = 0U;
    </#if>
</#list>

${regPorSet}
    
}

<#if intEnabled == true>
bool ${moduleNameUpperCase}_EOCEventCallbackRegister(
    PWM_GENERATOR genNum,
    const PWM_GEN_EOC_EVENT_CALLBACK callback,
    uintptr_t context
)
{
    bool status = true;
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
    <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#assign PWM_GEN_INT_ENABLE = "PG" + i + "_intEnabled">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true && .vars[PWM_GEN_INT_ENABLE]?has_content && .vars[PWM_GEN_INT_ENABLE] == true>
        case PWM_GENERATOR_${i}:
            pwmGen${i}CbObj.callback = callback;
            pwmGen${i}CbObj.context  = context;
            break;
    </#if>
</#list>
        default:
            status = false;
            break;
        }

    return status;
}

<#list 1..MAX_GENERATOR_COUNT as i>
    <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#assign PWM_GEN_INT_ENABLE = "PG" + i + "_intEnabled">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true && .vars[PWM_GEN_INT_ENABLE]?has_content && .vars[PWM_GEN_INT_ENABLE] == true>
/**
 @brief    Interrupt Handler for PWM Generator ${i}.

 @Note     It is an internal function called from ISR, user should not call it directly.
 */
void __attribute__((used)) PWM${i}_InterruptHandler(void)
{
    PWM_GENERATOR intGen = PWM_GENERATOR_${i};
    uintptr_t context_var;
    if(pwmGen${i}CbObj.callback != NULL)
    {
        context_var = pwmGen${i}CbObj.context;
        pwmGen${i}CbObj.callback (intGen, context_var);
    }
    
    ${.vars["pg"+i+"intFlagBit"]} = 0U;
}

    </#if>
</#list>
</#if>

/**
 End of File
*/
