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
<#if CONFIG_PWP?has_content>
#pragma config PWP =        ${CONFIG_PWP}
</#if>
<#if CONFIG_BWP?has_content>
#pragma config BWP =        ${CONFIG_BWP}
</#if>
<#if CONFIG_CP?has_content>
#pragma config CP =         ${CONFIG_CP}
</#if>
<#if CONFIG_SMCLR?has_content>
#pragma config SMCLR =      ${CONFIG_SMCLR}
</#if>


/*** DEVCFG1 ***/
<#if CONFIG_FNOSC?has_content>
#pragma config FNOSC =      ${CONFIG_FNOSC}
</#if>
<#if CONFIG_FPBDIV?has_content>
#pragma config FPBDIV =     ${CONFIG_FPBDIV}
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


/*** DEVCFG2 ***/
<#if CONFIG_BOREN?has_content>
#pragma config BOREN =    ${CONFIG_BOREN}
</#if>
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
<#if CONFIG_UPLLIDIV?has_content>
#pragma config UPLLIDIV =   ${CONFIG_UPLLIDIV}
</#if>

/*** DEVCFG3 ***/
<#if CONFIG_AI2C1?has_content>
#pragma config AI2C1 =      ${CONFIG_AI2C1}
</#if>
<#if CONFIG_AI2C2?has_content>
#pragma config AI2C2 =      ${CONFIG_AI2C2}
</#if>
<#if CONFIG_FSRSSEL?has_content>
#pragma config FSRSSEL =    ${CONFIG_FSRSSEL}
</#if>
<#if CONFIG_FVBUSONIO?has_content>
#pragma config FVBUSONIO =  ${CONFIG_FVBUSONIO}
</#if>
<#if CONFIG_USERID?has_content>
#pragma config USERID =     0x${CONFIG_USERID}
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



