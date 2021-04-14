<#if LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION?has_content>
<@mhc_expand_list list=LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION/>
</#if>
/*** FDEVOPT ***/
<#if CONFIG_SOSCHP?has_content>
#pragma config SOSCHP =      ${CONFIG_SOSCHP}
</#if>
<#if CONFIG_ALTI2C?has_content>
#pragma config ALTI2C =      ${CONFIG_ALTI2C}
</#if>
<#if CONFIG_FUSBIDIO?has_content>
#pragma config FUSBIDIO =   ${CONFIG_FUSBIDIO}
</#if>
<#if CONFIG_FVBUSIO?has_content>
#pragma config FVBUSIO =  ${CONFIG_FVBUSIO}
</#if>
<#if CONFIG_USERID?has_content>
#pragma config USERID =     0x${CONFIG_USERID}
</#if>

/*** FICD ***/
<#if CONFIG_JTAGEN?has_content>
#pragma config JTAGEN =     ${CONFIG_JTAGEN}
</#if>
<#if CONFIG_ICS?has_content>
#pragma config ICS =     ${CONFIG_ICS}
</#if>

/*** FPOR ***/
<#if CONFIG_BOREN?has_content>
#pragma config BOREN =    ${CONFIG_BOREN}
</#if>
<#if CONFIG_RETVR?has_content>
#pragma config RETVR =    ${CONFIG_RETVR}
</#if>
<#if CONFIG_LPBOREN?has_content>
#pragma config LPBOREN =    ${CONFIG_LPBOREN}
</#if>


/*** FWDT ***/
<#if CONFIG_SWDTPS?has_content>
#pragma config SWDTPS =      ${CONFIG_SWDTPS}
</#if>
<#if CONFIG_FWDTWINSZ?has_content>
#pragma config FWDTWINSZ =  ${CONFIG_FWDTWINSZ}
</#if>
<#if CONFIG_WINDIS?has_content>
#pragma config WINDIS =     ${CONFIG_WINDIS}
</#if>
<#if CONFIG_RWDTPS?has_content>
#pragma config RWDTPS =      ${CONFIG_RWDTPS}
</#if>
<#if CONFIG_RCLKSEL?has_content>
#pragma config RCLKSEL =     ${CONFIG_RCLKSEL}
</#if>
<#if CONFIG_FWDTEN?has_content>
#pragma config FWDTEN =     ${CONFIG_FWDTEN}
</#if>

/*** FOSCSEL ***/
<#if CONFIG_FNOSC?has_content>
#pragma config FNOSC =      ${CONFIG_FNOSC}
</#if>
<#if CONFIG_PLLSRC?has_content>
#pragma config PLLSRC =     ${CONFIG_PLLSRC}
</#if>
<#if CONFIG_SOSCEN?has_content>
#pragma config SOSCEN =    ${CONFIG_SOSCEN}
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
<#if CONFIG_SOSCSEL?has_content>
#pragma config SOSCSEL =     ${CONFIG_SOSCSEL}
</#if>
<#if CONFIG_FCKSM?has_content>
#pragma config FCKSM =      ${CONFIG_FCKSM}
</#if>

/*** FSEC ***/
<#if CONFIG_CP?has_content>
#pragma config CP =         ${CONFIG_CP}
</#if>
