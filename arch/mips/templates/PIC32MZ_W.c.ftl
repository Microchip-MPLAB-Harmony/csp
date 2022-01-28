<#if LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION?has_content>
<@mhc_expand_list list=LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION/>
</#if>

<#if FUSE_CONFIG_ENABLE>
/*** FBCFG0 ***/
<#if CONFIG_BUHSWEN?has_content>
#pragma config BUHSWEN =    ${CONFIG_BUHSWEN}
</#if>
<#if CONFIG_PCSCMODE?has_content>
#pragma config PCSCMODE =    ${CONFIG_PCSCMODE}
</#if>
<#if CONFIG_BOOTISA?has_content>
#pragma config BOOTISA =    ${CONFIG_BOOTISA}
</#if>


/*** DEVCFG0 ***/
<#if CONFIG_TDOEN?has_content>
#pragma config TDOEN =      ${CONFIG_TDOEN}
</#if>
<#if CONFIG_TROEN?has_content>
#pragma config TROEN =     ${CONFIG_TROEN}
</#if>
<#if CONFIG_JTAGEN?has_content>
#pragma config JTAGEN =     ${CONFIG_JTAGEN}
</#if>
<#if CONFIG_FCPRI?has_content>
#pragma config FCPRI =      ${CONFIG_FCPRI}
</#if>
<#if CONFIG_DMAPRI?has_content>
#pragma config DMAPRI =    ${CONFIG_DMAPRI}
</#if>
<#if CONFIG_EXLPRI?has_content>
#pragma config EXLPRI =    ${CONFIG_EXLPRI}
</#if>
<#if CONFIG_USBSSEN?has_content>
#pragma config USBSSEN =     ${CONFIG_USBSSEN}
</#if>
<#if CONFIG_PMULOCK?has_content>
#pragma config PMULOCK =     ${CONFIG_PMULOCK}
</#if>
<#if CONFIG_PGLOCK?has_content>
#pragma config PGLOCK =      ${CONFIG_PGLOCK}
</#if>
<#if CONFIG_PMDLOCK?has_content>
#pragma config PMDLOCK =   ${CONFIG_PMDLOCK}
</#if>
<#if CONFIG_IOLOCK?has_content>
#pragma config IOLOCK =  ${CONFIG_IOLOCK}
</#if>
<#if CONFIG_CFGLOCK?has_content>
#pragma config CFGLOCK =   ${CONFIG_CFGLOCK}
</#if>
<#if CONFIG_OC_ACLK?has_content>
#pragma config OC_ACLK =  ${CONFIG_OC_ACLK}
</#if>
<#if CONFIG_IC_ACLK?has_content>
#pragma config IC_ACLK =  ${CONFIG_IC_ACLK}
</#if>
<#if CONFIG_CANFDDIV?has_content>
#pragma config CANFDDIV =  ${CONFIG_CANFDDIV}
</#if>
<#if CONFIG_PCM?has_content>
#pragma config PCM =  ${CONFIG_PCM}
</#if>
<#if CONFIG_UPLLHWMD?has_content>
#pragma config UPLLHWMD =  ${CONFIG_UPLLHWMD}
</#if>
<#if CONFIG_SPLLHWMD?has_content>
#pragma config SPLLHWMD =   ${CONFIG_SPLLHWMD}
</#if>
<#if CONFIG_BTPLLHWMD?has_content>
#pragma config BTPLLHWMD =        ${CONFIG_BTPLLHWMD}
</#if>
<#if CONFIG_ETHPLLHWMD?has_content>
#pragma config ETHPLLHWMD =        ${CONFIG_ETHPLLHWMD}
</#if>
<#if CONFIG_FECCCON?has_content>
#pragma config FECCCON =         ${CONFIG_FECCCON}
</#if>
<#if CONFIG_ETHTPSF?has_content>
#pragma config ETHTPSF =         ${CONFIG_ETHTPSF}
</#if>
<#if CONFIG_EPGMCLK?has_content>
#pragma config EPGMCLK =         ${CONFIG_EPGMCLK}
</#if>


/*** DEVCFG1 ***/
<#if CONFIG_DEBUG?has_content>
#pragma config DEBUG =         ${CONFIG_DEBUG}
</#if>
<#if CONFIG_ICESEL?has_content>
#pragma config ICESEL =         ${CONFIG_ICESEL}
</#if>
<#if CONFIG_TRCEN?has_content>
#pragma config TRCEN =         ${CONFIG_TRCEN}
</#if>
<#if CONFIG_FMIIEN?has_content>
#pragma config FMIIEN =         ${CONFIG_FMIIEN}
</#if>
<#if CONFIG_ETHEXEREF?has_content>
#pragma config ETHEXEREF =         ${CONFIG_ETHEXEREF}
</#if>
<#if CONFIG_CLASSBDIS?has_content>
#pragma config CLASSBDIS =         ${CONFIG_CLASSBDIS}
</#if>
<#if CONFIG_USBIDIO?has_content>
#pragma config USBIDIO =         ${CONFIG_USBIDIO}
</#if>
<#if CONFIG_VBUSIO?has_content>
#pragma config VBUSIO =         ${CONFIG_VBUSIO}
</#if>
<#if CONFIG_HSSPIEN?has_content>
#pragma config HSSPIEN =         ${CONFIG_HSSPIEN}
</#if>
<#if CONFIG_SMCLR?has_content>
#pragma config SMCLR =      ${CONFIG_SMCLR}
</#if>
<#if CONFIG_USBDMTRIM?has_content>
#pragma config USBDMTRIM =      ${CONFIG_USBDMTRIM}
</#if>
<#if CONFIG_USBDPTRIM?has_content>
#pragma config USBDPTRIM =      ${CONFIG_USBDPTRIM}
</#if>
<#if CONFIG_HSUARTEN?has_content>
#pragma config HSUARTEN =    ${CONFIG_HSUARTEN}
</#if>
<#if CONFIG_WDTPSS?has_content>
#pragma config WDTPSS =    ${CONFIG_WDTPSS}
</#if>


/*** DEVCFG2 ***/
<#if CONFIG_DMTINTV?has_content>
#pragma config DMTINTV =    ${CONFIG_DMTINTV}
</#if>
<#if CONFIG_POSCMOD?has_content>
#pragma config POSCMOD =    ${CONFIG_POSCMOD}
</#if>
<#if CONFIG_WDTRMCS?has_content>
#pragma config WDTRMCS =    ${CONFIG_WDTRMCS}
</#if>
<#if CONFIG_SOSCSEL?has_content>
#pragma config SOSCSEL =    ${CONFIG_SOSCSEL}
</#if>
<#if CONFIG_WAKE2SPD?has_content>
#pragma config WAKE2SPD =    ${CONFIG_WAKE2SPD}
</#if>
<#if CONFIG_CKSWEN?has_content>
#pragma config CKSWEN =    ${CONFIG_CKSWEN}
</#if>
<#if CONFIG_FSCMEN?has_content>
#pragma config FSCMEN =    ${CONFIG_FSCMEN}
</#if>
<#if CONFIG_WDTPS?has_content>
#pragma config WDTPS =    ${CONFIG_WDTPS}
</#if>
<#if CONFIG_WDTSPGM?has_content>
#pragma config WDTSPGM =    ${CONFIG_WDTSPGM}
</#if>
<#if CONFIG_WINDIS?has_content>
#pragma config WINDIS =    ${CONFIG_WINDIS}
</#if>
<#if CONFIG_WDTEN?has_content>
#pragma config WDTEN =    ${CONFIG_WDTEN}
</#if>
<#if CONFIG_WDTWINSZ?has_content>
#pragma config WDTWINSZ =    ${CONFIG_WDTWINSZ}
</#if>
<#if CONFIG_DMTCNT?has_content>
#pragma config DMTCNT =    ${CONFIG_DMTCNT}
</#if>
<#if CONFIG_DMTEN?has_content>
#pragma config DMTEN =    ${CONFIG_DMTEN}
</#if>


/*** DEVCFG4 ***/
<#if CONFIG_SOSCCFG?has_content>
#pragma config SOSCCFG =    ${CONFIG_SOSCCFG}
</#if>
<#if CONFIG_VBZPBOREN?has_content>
#pragma config VBZPBOREN =    ${CONFIG_VBZPBOREN}
</#if>
<#if CONFIG_DSZPBOREN?has_content>
#pragma config DSZPBOREN =    ${CONFIG_DSZPBOREN}
</#if>
<#if CONFIG_DSWDTPS?has_content>
#pragma config DSWDTPS =    ${CONFIG_DSWDTPS}
</#if>
<#if CONFIG_DSWDTOSC?has_content>
#pragma config DSWDTOSC =    ${CONFIG_DSWDTOSC}
</#if>
<#if CONFIG_DSWDTEN?has_content>
#pragma config DSWDTEN =    ${CONFIG_DSWDTEN}
</#if>
<#if CONFIG_DSEN?has_content>
#pragma config DSEN =    ${CONFIG_DSEN}
</#if>
<#if CONFIG_SOSCEN?has_content>
#pragma config SOSCEN =    ${CONFIG_SOSCEN}
</#if>


/*** FCPN0 ***/
<#if CONFIG_CP?has_content>
#pragma config CP =    ${CONFIG_CP}
</#if>

</#if>