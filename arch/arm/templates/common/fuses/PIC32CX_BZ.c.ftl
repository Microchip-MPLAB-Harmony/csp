<#if LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION?has_content>
<@mhc_expand_list list=LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION/>
</#if>

/*** FUSERID ***/
<#if CONFIG_USER_ID?has_content>
#pragma config USER_ID =      0x${CONFIG_USER_ID}
</#if>

/*** DEVCFG0 ***/
<#if CONFIG_TDOEN?has_content>
#pragma config TDOEN =      ${CONFIG_TDOEN}
</#if>
<#if CONFIG_SWOEN?has_content>
#pragma config SWOEN =      ${CONFIG_SWOEN}
</#if>
<#if CONFIG_TROEN?has_content>
#pragma config TROEN =      ${CONFIG_TROEN}
</#if>
<#if CONFIG_JTAGEN?has_content>
#pragma config JTAGEN =      ${CONFIG_JTAGEN}
</#if>
<#if CONFIG_ADCPOVR?has_content>
#pragma config ADCPOVR =      ${CONFIG_ADCPOVR}
</#if>
<#if CONFIG_GPSOSCE?has_content>
#pragma config GPSOSCE =      ${CONFIG_GPSOSCE}
</#if>
<#if CONFIG_ACCMP1_ALTEN?has_content>
#pragma config ACCMP1_ALTEN =      ${CONFIG_ACCMP1_ALTEN}
</#if>
<#if CONFIG_CPENFILT?has_content>
#pragma config CPENFILT =      ${CONFIG_CPENFILT}
</#if>
<#if CONFIG_RTCIN0_ALTEN?has_content>
#pragma config RTCIN0_ALTEN =      ${CONFIG_RTCIN0_ALTEN}
</#if>
<#if CONFIG_RTCOUT_ALTEN?has_content>
#pragma config RTCOUT_ALTEN =      ${CONFIG_RTCOUT_ALTEN}
</#if>
<#if CONFIG_PMULOCK?has_content>
#pragma config PMULOCK =      ${CONFIG_PMULOCK}
</#if>
<#if CONFIG_PGLOCK?has_content>
#pragma config PGLOCK =      ${CONFIG_PGLOCK}
</#if>
<#if CONFIG_PMDLOCK?has_content>
#pragma config PMDLOCK =      ${CONFIG_PMDLOCK}
</#if>
<#if CONFIG_IOLOCK?has_content>
#pragma config IOLOCK =      ${CONFIG_IOLOCK}
</#if>
<#if CONFIG_CFGLOCK?has_content>
#pragma config CFGLOCK =      ${CONFIG_CFGLOCK}
</#if>
<#if CONFIG_VBCMODE?has_content>
#pragma config VBCMODE =      ${CONFIG_VBCMODE}
</#if>
<#if CONFIG_SMBUSEN0?has_content>
#pragma config SMBUSEN0 =      ${CONFIG_SMBUSEN0}
</#if>
<#if CONFIG_SMBUSEN1?has_content>
#pragma config SMBUSEN1 =      ${CONFIG_SMBUSEN1}
</#if>
<#if CONFIG_SMBUSEN2?has_content>
#pragma config SMBUSEN2 =      ${CONFIG_SMBUSEN2}
</#if>
<#if CONFIG_HPLUGDIS?has_content>
#pragma config HPLUGDIS =      ${CONFIG_HPLUGDIS}
</#if>
<#if CONFIG_SLRTEN0?has_content>
#pragma config SLRTEN0 =      ${CONFIG_SLRTEN0}
</#if>
<#if CONFIG_SLRTEN1?has_content>
#pragma config SLRTEN1 =      ${CONFIG_SLRTEN1}
</#if>
<#if CONFIG_SLRTEN2?has_content>
#pragma config SLRTEN2 =      ${CONFIG_SLRTEN2}
</#if>
<#if CONFIG_PCM?has_content>
#pragma config PCM =      ${CONFIG_PCM}
</#if>
<#if CONFIG_INT0E?has_content>
#pragma config INT0E =      ${CONFIG_INT0E}
</#if>
<#if CONFIG_INT0P?has_content>
#pragma config INT0P =      ${CONFIG_INT0P}
</#if>
<#if CONFIG_ADCFCEN?has_content>
#pragma config ADCFCEN =      ${CONFIG_ADCFCEN}
</#if>
<#if CONFIG_FECCCON?has_content>
#pragma config FECCCON =         ${CONFIG_FECCCON}
</#if>
<#if CONFIG_FRECCDIS?has_content>
#pragma config FRECCDIS =      ${CONFIG_FRECCDIS}
</#if>
<#if CONFIG_EPGMCLK?has_content>
#pragma config EPGMCLK =      ${CONFIG_EPGMCLK}
</#if>


/*** DEVCFG1 ***/
<#if CONFIG_DEBUG?has_content>
#pragma config DEBUG =      ${CONFIG_DEBUG}
</#if>
<#if CONFIG_ICESEL?has_content>
#pragma config ICESEL =      ${CONFIG_ICESEL}
</#if>
<#if CONFIG_TRCEN?has_content>
#pragma config TRCEN =      ${CONFIG_TRCEN}
</#if>
<#if CONFIG_ZBTWKSYS?has_content>
#pragma config ZBTWKSYS =      ${CONFIG_ZBTWKSYS}
</#if>
<#if CONFIG_CMP0_OE?has_content>
#pragma config CMP0_OE =      ${CONFIG_CMP0_OE}
</#if>
<#if CONFIG_CMP1_OE?has_content>
#pragma config CMP1_OE =      ${CONFIG_CMP1_OE}
</#if>
<#if CONFIG_CLASSBDIS?has_content>
#pragma config CLASSBDIS =      ${CONFIG_CLASSBDIS}
</#if>
<#if CONFIG_SLRCTRL0?has_content>
#pragma config SLRCTRL0 =      ${CONFIG_SLRCTRL0}
</#if>
<#if CONFIG_SLRCTRL1?has_content>
#pragma config SLRCTRL1 =      ${CONFIG_SLRCTRL1}
</#if>
<#if CONFIG_SLRCTRL2?has_content>
#pragma config SLRCTRL2 =      ${CONFIG_SLRCTRL2}
</#if>
<#if CONFIG_SMCLR?has_content>
#pragma config SMCLR =      ${CONFIG_SMCLR}
</#if>
<#if CONFIG_QSCHE_EN?has_content>
#pragma config QSCHE_EN =      ${CONFIG_QSCHE_EN}
</#if>
<#if CONFIG_QSPI_HSEN?has_content>
#pragma config QSPI_HSEN =      ${CONFIG_QSPI_HSEN}
</#if>
<#if CONFIG_SCOM0_HSEN?has_content>
#pragma config SCOM0_HSEN =      ${CONFIG_SCOM0_HSEN}
</#if>
<#if CONFIG_SCOM1_HSEN?has_content>
#pragma config SCOM1_HSEN =      ${CONFIG_SCOM1_HSEN}
</#if>
<#if CONFIG_SCOM2_HSEN?has_content>
#pragma config SCOM2_HSEN =      ${CONFIG_SCOM2_HSEN}
</#if>
<#if CONFIG_CCL_OE?has_content>
#pragma config CCL_OE =      ${CONFIG_CCL_OE}
</#if>
<#if CONFIG_I2CDSEL0?has_content>
#pragma config I2CDSEL0 =      ${CONFIG_I2CDSEL0}
</#if>
<#if CONFIG_I2CDSEL1?has_content>
#pragma config I2CDSEL1 =      ${CONFIG_I2CDSEL1}
</#if>
<#if CONFIG_I2CDSEL2?has_content>
#pragma config I2CDSEL2 =      ${CONFIG_I2CDSEL2}
</#if>
<#if CONFIG_WDTPSS?has_content>
#pragma config WDTPSS =      ${CONFIG_WDTPSS}
</#if>
<#if CONFIG_QSPIDDRM?has_content>
#pragma config QSPIDDRM =      ${CONFIG_QSPIDDRM}
</#if>
<#if CONFIG_CLKZBREF?has_content>
#pragma config CLKZBREF =      ${CONFIG_CLKZBREF}
</#if>
<#if CONFIG_FMPDAEN?has_content>
#pragma config FMPDAEN =      ${CONFIG_FMPDAEN}
</#if>

/*** DEVCFG2 ***/
<#if CONFIG_ACMP_CYCLE?has_content>
#pragma config ACMP_CYCLE =      ${CONFIG_ACMP_CYCLE}
</#if>
<#if CONFIG_DMTINTV?has_content>
#pragma config DMTINTV =      ${CONFIG_DMTINTV}
</#if>
<#if CONFIG_PMUTEST_VDD_EN?has_content>
#pragma config PMUTEST_VDD_EN =      ${CONFIG_PMUTEST_VDD_EN}
</#if>
<#if CONFIG_POSCMOD?has_content>
#pragma config POSCMOD =      ${CONFIG_POSCMOD}
</#if>
<#if CONFIG_WDTRMCS?has_content>
#pragma config WDTRMCS =      ${CONFIG_WDTRMCS}
</#if>
<#if CONFIG_SOSCSEL?has_content>
#pragma config SOSCSEL =      ${CONFIG_SOSCSEL}
</#if>
<#if CONFIG_WAKE2SPD?has_content>
#pragma config WAKE2SPD =      ${CONFIG_WAKE2SPD}
</#if>
<#if CONFIG_CKSWEN?has_content>
#pragma config CKSWEN =      ${CONFIG_CKSWEN}
</#if>
<#if CONFIG_FSCMEN?has_content>
#pragma config FSCMEN =      ${CONFIG_FSCMEN}
</#if>
<#if CONFIG_WDTPSR?has_content>
#pragma config WDTPSR =      ${CONFIG_WDTPSR}
</#if>
<#if CONFIG_WDTSPGM?has_content>
#pragma config WDTSPGM =      ${CONFIG_WDTSPGM}
</#if>
<#if CONFIG_WINDIS?has_content>
#pragma config WINDIS =      ${CONFIG_WINDIS}
</#if>
<#if CONFIG_WDTEN?has_content>
#pragma config WDTEN =      ${CONFIG_WDTEN}
</#if>
<#if CONFIG_WDTWINSZ?has_content>
#pragma config WDTWINSZ =    ${CONFIG_WDTWINSZ}
</#if>
<#if CONFIG_DMTCNT?has_content>
#pragma config DMTCNT =      ${CONFIG_DMTCNT}
</#if>
<#if CONFIG_DMTEN?has_content>
#pragma config DMTEN =      ${CONFIG_DMTEN}
</#if>


/*** DEVCFG4 ***/
<#if CONFIG_SOSCCFG?has_content>
#pragma config SOSCCFG =    0x${CONFIG_SOSCCFG}
</#if>
<#if CONFIG_RTCEVENT_SEL?has_content>
#pragma config RTCEVENT_SEL =      ${CONFIG_RTCEVENT_SEL}
</#if>
<#if CONFIG_RTCEVENT_EN?has_content>
#pragma config RTCEVENT_EN =      ${CONFIG_RTCEVENT_EN}
</#if>
<#if CONFIG_VBKP_1KCSEL?has_content>
#pragma config VBKP_1KCSEL =      ${CONFIG_VBKP_1KCSEL}
</#if>
<#if CONFIG_VBKP_32KCSEL?has_content>
#pragma config VBKP_32KCSEL =      ${CONFIG_VBKP_32KCSEL}
</#if>
<#if CONFIG_VBKP_DIVSEL?has_content>
#pragma config VBKP_DIVSEL =      ${CONFIG_VBKP_DIVSEL}
</#if>
<#if CONFIG_LPCLK_MOD?has_content>
#pragma config LPCLK_MOD =      ${CONFIG_LPCLK_MOD}
</#if>
<#if CONFIG_RTCEVTYPE?has_content>
#pragma config RTCEVTYPE =      ${CONFIG_RTCEVTYPE}
</#if>
<#if CONFIG_CPEN_DLY?has_content>
#pragma config CPEN_DLY =      ${CONFIG_CPEN_DLY}
</#if>
<#if CONFIG_DSZPBOREN?has_content>
#pragma config DSZPBOREN =      ${CONFIG_DSZPBOREN}
</#if>
<#if CONFIG_DSWDTPS?has_content>
#pragma config DSWDTPS =      ${CONFIG_DSWDTPS}
</#if>
<#if CONFIG_DSWDTOSC?has_content>
#pragma config DSWDTOSC =    ${CONFIG_DSWDTOSC}
</#if>
<#if CONFIG_DSWDTEN?has_content>
#pragma config DSWDTEN =      ${CONFIG_DSWDTEN}
</#if>
<#if CONFIG_DSEN?has_content>
#pragma config DSEN =    ${CONFIG_DSEN}
</#if>
<#if CONFIG_UVREGROVR?has_content>
#pragma config UVREGROVR =      ${CONFIG_UVREGROVR}
</#if>
<#if CONFIG_LPOSCEN?has_content>
#pragma config LPOSCEN =      ${CONFIG_LPOSCEN}
</#if>
<#if CONFIG_RTCNTM_CSEL?has_content>
#pragma config RTCNTM_CSEL =      ${CONFIG_RTCNTM_CSEL}
</#if>

/*** FBCFG0 ***/
<#if CONFIG_BINFOVALID?has_content>
#pragma config BINFOVALID =      ${CONFIG_BINFOVALID}
</#if>
<#if CONFIG_PCSCMODE?has_content>
#pragma config PCSCMODE =      ${CONFIG_PCSCMODE}
</#if>

/*** FCPN0 ***/
<#if CONFIG_CP?has_content>
#pragma config CP =      ${CONFIG_CP}
</#if>