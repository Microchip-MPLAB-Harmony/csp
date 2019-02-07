<#if LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION?has_content>
<@mhc_expand_list list=LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION/>
</#if>

/*** DEVCFG0 ***/
<#if CONFIG_DEBUG?has_content>
#pragma config DEBUG =      ${CONFIG_DEBUG}
</#if>
<#if CONFIG_JTAGEN?has_content>
#pragma config JTAGEN =     ${CONFIG_JTAGEN}
</#if>
<#if CONFIG_ICESEL?has_content>
#pragma config ICESEL =     ${CONFIG_ICESEL}
</#if>
<#if CONFIG_TRCEN?has_content>
#pragma config TRCEN =      ${CONFIG_TRCEN}
</#if>
<#if CONFIG_BOOTISA?has_content>
#pragma config BOOTISA =    ${CONFIG_BOOTISA}
</#if>
<#if CONFIG_FSLEEP?has_content>
#pragma config FSLEEP =     ${CONFIG_FSLEEP}
</#if>
<#if CONFIG_DBGPER?has_content>
#pragma config DBGPER =     ${CONFIG_DBGPER}
</#if>
<#if CONFIG_SMCLR?has_content>
#pragma config SMCLR =      ${CONFIG_SMCLR}
</#if>
<#if CONFIG_SOSCGAIN?has_content>
#pragma config SOSCGAIN =   ${CONFIG_SOSCGAIN}
</#if>
<#if CONFIG_SOSCBOOST?has_content>
#pragma config SOSCBOOST =  ${CONFIG_SOSCBOOST}
</#if>
<#if CONFIG_POSCGAIN?has_content>
#pragma config POSCGAIN =   ${CONFIG_POSCGAIN}
</#if>
<#if CONFIG_POSCBOOST?has_content>
#pragma config POSCBOOST =  ${CONFIG_POSCBOOST}
</#if>
<#if CONFIG_EJTAGBEN?has_content>
#pragma config EJTAGBEN =   ${CONFIG_EJTAGBEN}
</#if>
<#if CONFIG_CP?has_content>
#pragma config CP =         ${CONFIG_CP}
</#if>
<#if CONFIG_TDOEN?has_content>
#pragma config TDOEN =         ${CONFIG_TDOEN}
</#if>
<#if CONFIG_TROEN?has_content>
#pragma config TROEN =         ${CONFIG_TROEN}
</#if>
<#if CONFIG_USBSSEN?has_content>
#pragma config USBSSEN =         ${CONFIG_USBSSEN}
</#if>
<#if CONFIG_PGLOCK?has_content>
#pragma config PGLOCK =         ${CONFIG_PGLOCK}
</#if>
<#if CONFIG_PMDLOCK?has_content>
#pragma config PMDLOCK =         ${CONFIG_PMDLOCK}
</#if>
<#if CONFIG_IOLOCK?has_content>
#pragma config IOLOCK =         ${CONFIG_IOLOCK}
</#if>
<#if CONFIG_CFGLOCK?has_content>
#pragma config CFGLOCK =         ${CONFIG_CFGLOCK}
</#if>
<#if CONFIG_OC_ACLK?has_content>
#pragma config OC_ACLK =         ${CONFIG_OC_ACLK}
</#if>
<#if CONFIG_IC_ACLK?has_content>
#pragma config IC_ACLK =         ${CONFIG_IC_ACLK}
</#if>
<#if CONFIG_EPGMCLK?has_content>
#pragma config EPGMCLK =         ${CONFIG_EPGMCLK}
</#if>

/*** DEVCFG1 ***/
<#if CONFIG_FNOSC?has_content>
#pragma config FNOSC =      ${CONFIG_FNOSC}
</#if>
<#if CONFIG_DMTINTV?has_content>
#pragma config DMTINTV =    ${CONFIG_DMTINTV}
</#if>
<#if CONFIG_FSOSCEN?has_content>
#pragma config FSOSCEN =    ${CONFIG_FSOSCEN}
</#if>
<#if CONFIG_IESO?has_content>
#pragma config IESO =       ${CONFIG_IESO}
</#if>
<#if CONFIG_POSCMOD?has_content>
#pragma config POSCMOD =    ${CONFIG_POSCMOD}
</#if>
<#if CONFIG_OSCIOFNC?has_content>
#pragma config OSCIOFNC =   ${CONFIG_OSCIOFNC}
</#if>
<#if CONFIG_FCKSM?has_content>
#pragma config FCKSM =      ${CONFIG_FCKSM}
</#if>
<#if CONFIG_WDTPS?has_content>
#pragma config WDTPS =      ${CONFIG_WDTPS}
</#if>
<#if CONFIG_WDTSPGM?has_content>
#pragma config WDTSPGM =    ${CONFIG_WDTSPGM}
</#if>
<#if CONFIG_FWDTEN?has_content>
#pragma config FWDTEN =     ${CONFIG_FWDTEN}
</#if>
<#if CONFIG_WINDIS?has_content>
#pragma config WINDIS =     ${CONFIG_WINDIS}
</#if>
<#if CONFIG_FWDTWINSZ?has_content>
#pragma config FWDTWINSZ =  ${CONFIG_FWDTWINSZ}
</#if>
<#if CONFIG_DMTCNT?has_content>
#pragma config DMTCNT =     ${CONFIG_DMTCNT}
</#if>
<#if CONFIG_FDMTEN?has_content>
#pragma config FDMTEN =     ${CONFIG_FDMTEN}
</#if>

/*** DEVCFG2 ***/
<#if CONFIG_FPLLIDIV?has_content>
#pragma config FPLLIDIV =   ${CONFIG_FPLLIDIV}
</#if>
<#if CONFIG_FPLLRNG?has_content>
#pragma config FPLLRNG =    ${CONFIG_FPLLRNG}
</#if>
<#if CONFIG_FPLLICLK?has_content>
#pragma config FPLLICLK =   ${CONFIG_FPLLICLK}
</#if>
<#if CONFIG_FPLLMULT?has_content>
#pragma config FPLLMULT =   ${CONFIG_FPLLMULT}
</#if>
<#if CONFIG_FPLLMUL?has_content>
#pragma config FPLLMUL =    ${CONFIG_FPLLMUL}
</#if>
<#if CONFIG_FPLLODIV?has_content>
#pragma config FPLLODIV =   ${CONFIG_FPLLODIV}
</#if>
<#if CONFIG_VBATBOREN?has_content>
#pragma config VBATBOREN =  ${CONFIG_VBATBOREN}
</#if>
<#if CONFIG_DSBOREN?has_content>
#pragma config DSBOREN =    ${CONFIG_DSBOREN}
</#if>
<#if CONFIG_DSWDTPS?has_content>
#pragma config DSWDTPS =    ${CONFIG_DSWDTPS}
</#if>
<#if CONFIG_DSWDTOSC?has_content>
#pragma config DSWDTOSC =   ${CONFIG_DSWDTOSC}
</#if>
<#if CONFIG_DSWDTEN?has_content>
#pragma config DSWDTEN =    ${CONFIG_DSWDTEN}
</#if>
<#if CONFIG_FDSEN?has_content>
#pragma config FDSEN =      ${CONFIG_FDSEN}
</#if>
<#if CONFIG_BORSEL?has_content>
#pragma config BORSEL =     ${CONFIG_BORSEL}
</#if>
<#if CONFIG_UPLLEN?has_content>
#pragma config UPLLEN =     ${CONFIG_UPLLEN}
</#if>

/*** DEVCFG3 ***/
<#if CONFIG_USERID?has_content>
#pragma config USERID =     0x${CONFIG_USERID}
</#if>
<#if CONFIG_FUSBIDIO2?has_content>
#pragma config FUSBIDIO2 =   ${CONFIG_FUSBIDIO2}
</#if>
<#if CONFIG_FVBUSIO2?has_content>
#pragma config FVBUSIO2 =  ${CONFIG_FVBUSIO2}
</#if>
<#if CONFIG_PGL1WAY?has_content>
#pragma config PGL1WAY =    ${CONFIG_PGL1WAY}
</#if>
<#if CONFIG_PMDL1WAY?has_content>
#pragma config PMDL1WAY =   ${CONFIG_PMDL1WAY}
</#if>
<#if CONFIG_IOL1WAY?has_content>
#pragma config IOL1WAY =    ${CONFIG_IOL1WAY}
</#if>
<#if CONFIG_FUSBIDIO?has_content>
#pragma config FUSBIDIO =   ${CONFIG_FUSBIDIO}
</#if>
<#if CONFIG_FUSBIDIO1?has_content>
#pragma config FUSBIDIO1 =   ${CONFIG_FUSBIDIO1}
</#if>
<#if CONFIG_FVBUSIO1?has_content>
#pragma config FVBUSIO1 =  ${CONFIG_FVBUSIO1}
</#if>
<#if CONFIG_PWMLOCK?has_content>
#pragma config PWMLOCK =  ${CONFIG_PWMLOCK}
</#if>

<#if CONFIG_TSEQ?has_content>
/*** BF1SEQ ***/
#pragma config TSEQ =       0x${CONFIG_TSEQ}
</#if>
<#if CONFIG_CSEQ?has_content>
#pragma config CSEQ =       0x${CONFIG_CSEQ}
</#if>
<#if CONFIG_BOOTSEL?has_content>
#pragma config BOOTSEL =       ${CONFIG_BOOTSEL}
</#if>

