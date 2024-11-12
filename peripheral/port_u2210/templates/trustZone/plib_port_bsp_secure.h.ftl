<#--  =====================
    MACRO mhc_process_leds
    ===================== -->
<#compress>
<#macro mhc_process_leds>
    <#assign LED_Name_List = []>
    <#assign LED_PortPin_List = []>
    <#assign LED_PortGroup_List = []>
    <#assign LED_ActiveLevel_List = []>

    <#list 1..PORT_PIN_COUNT as i>
        <#assign functype = "PIN_" + i + "_FUNCTION_TYPE">
        <#assign funcname = "PIN_" + i + "_FUNCTION_NAME">
        <#assign pinport  = "PIN_" + i + "_PORT_PIN">
        <#assign pingroup = "PIN_" + i + "_PORT_GROUP">
        <#assign pinisSecure = "PIN_" + i + "_IS_NON_SECURE">

        <#if .vars[pinisSecure] == "SECURE">
        <#if .vars[functype]?has_content>
            <#if (.vars[functype] == "LED_AH") || (.vars[functype] == "LED_AL")>
                <#if .vars[funcname]?has_content>
                    <#if .vars[pinport]?has_content>
                        <#if .vars[pingroup]?has_content>

                            <#assign LED_Name_List = LED_Name_List + [.vars[funcname]]>
                            <#assign LED_PortPin_List = LED_PortPin_List + [.vars[pinport]]>
                            <#assign LED_PortGroup_List = LED_PortGroup_List + [.vars[pingroup]]>
                            <#if (.vars[functype] == "LED_AH")>
                                <#assign LED_ActiveLevel_List = LED_ActiveLevel_List + ["High"]>
                            <#else>
                                <#assign LED_ActiveLevel_List = LED_ActiveLevel_List + ["Low"]>
                            </#if>

                        </#if>
                    </#if>
                </#if>
            </#if>
        </#if>
        </#if>
    </#list>
</#macro>

<#--  =====================
    MACRO mhc_process_switches
    ===================== -->
<#macro mhc_process_switches>
    <#assign SWITCH_Name_List = []>
    <#assign SWITCH_PortPin_List = []>
    <#assign SWITCH_PortGroup_List = []>
    <#assign SWITCH_ActiveLevel_List = []>

    <#list 1..PORT_PIN_COUNT as i>
        <#assign functype = "PIN_" + i + "_FUNCTION_TYPE">
        <#assign funcname = "PIN_" + i + "_FUNCTION_NAME">
        <#assign pinport = "PIN_" + i + "_PORT_PIN">
        <#assign pingroup = "PIN_" + i + "_PORT_GROUP">
        <#assign pinisSecure = "PIN_" + i + "_IS_NON_SECURE">

        <#if .vars[pinisSecure] == "SECURE">
        <#if .vars[functype]?has_content>
            <#if (.vars[functype] == "SWITCH_AH") || (.vars[functype] == "SWITCH_AL")>
                <#if .vars[funcname]?has_content>
                    <#if .vars[pinport]?has_content>
                        <#if .vars[pingroup]?has_content>

                            <#assign SWITCH_Name_List = SWITCH_Name_List + [.vars[funcname]]>
                            <#assign SWITCH_PortPin_List = SWITCH_PortPin_List + [.vars[pinport]]>
                            <#assign SWITCH_PortGroup_List = SWITCH_PortGroup_List + [.vars[pingroup]]>
                            <#if (.vars[functype] == "SWITCH_AH")>
                                <#assign SWITCH_ActiveLevel_List = SWITCH_ActiveLevel_List + ["High"]>
                            <#else>
                                <#assign SWITCH_ActiveLevel_List = SWITCH_ActiveLevel_List + ["Low"]>
                            </#if>

                        </#if>
                    </#if>
                </#if>
            </#if>
        </#if>
        </#if>
    </#list>
</#macro>

<#--  =====================
    MACRO mhc_process_vbus
    ===================== -->
<#macro mhc_process_vbus>
    <#assign VBUS_Name_List = []>
    <#assign VBUS_PortPin_List = []>
    <#assign VBUS_PortGroup_List = []>
    <#assign VBUS_ActiveLevel_List = []>

    <#list 1..PORT_PIN_COUNT as i>
        <#assign functype = "PIN_" + i + "_FUNCTION_TYPE">
        <#assign funcname = "PIN_" + i + "_FUNCTION_NAME">
        <#assign pinport  = "PIN_" + i + "_PORT_PIN">
        <#assign pingroup = "PIN_" + i + "_PORT_GROUP">
        <#assign pinisSecure = "PIN_" + i + "_IS_NON_SECURE">

        <#if .vars[pinisSecure] == "SECURE">
        <#if .vars[functype]?has_content>
            <#if (.vars[functype] == "VBUS_AH") || (.vars[functype] == "VBUS_AL") || (.vars[functype] == "VBUS")>
                <#if .vars[funcname]?has_content>
                    <#if .vars[pinport]?has_content>
                        <#if .vars[pingroup]?has_content>

                            <#assign VBUS_Name_List = VBUS_Name_List + [.vars[funcname]]>
                            <#assign VBUS_PortPin_List = VBUS_PortPin_List + [.vars[pinport]]>
                            <#assign VBUS_PortGroup_List = VBUS_PortGroup_List + [.vars[pingroup]]>
                            <#if (.vars[functype] == "VBUS_AH")>
                                <#assign VBUS_ActiveLevel_List = VBUS_ActiveLevel_List + ["High"]>
                            <#else>
                                <#assign VBUS_ActiveLevel_List = VBUS_ActiveLevel_List + ["Low"]>
                            </#if>

                        </#if>
                    </#if>
                </#if>
            </#if>
        </#if>
        </#if>
    </#list>
</#macro>

<#--  =====================
    MACRO execution
    ===================== -->
<@mhc_process_leds/>
<@mhc_process_switches/>
<@mhc_process_vbus/>
</#compress>

<#assign myHash = { "A": 0, "B": 1, "C": "2", "D": 3, "E": 4}>
<#if (LED_Name_List?size > 0)>
    <#list LED_Name_List as ledName>
        <#list LED_PortGroup_List as ledGroup>
            <#list LED_PortPin_List as ledPinPos>
                <#list LED_ActiveLevel_List as ledActiveLevel>
                    <#if ledName?counter == ledGroup?counter>
                        <#if ledName?counter == ledPinPos?counter>
                            <#if ledName?counter == ledActiveLevel?counter>
                                <#lt>/*** LED Macros for ${ledName} ***/
                                <#lt>#define ${ledName}_Toggle()     (${PORT_REG_NAME}_REGS->GROUP[${myHash[ledGroup]}].PORT_OUTTGL = 1 << ${ledPinPos})
                                <#if ledActiveLevel == "High">
                                    <#lt>#define ${ledName}_On()         (${PORT_REG_NAME}_REGS->GROUP[${myHash[ledGroup]}].PORT_OUTSET = 1 << ${ledPinPos})
                                    <#lt>#define ${ledName}_Off()        (${PORT_REG_NAME}_REGS->GROUP[${myHash[ledGroup]}].PORT_OUTCLR = 1 << ${ledPinPos})
                                <#else>
                                    <#lt>#define ${ledName}_On()         (${PORT_REG_NAME}_REGS->GROUP[${myHash[ledGroup]}].PORT_OUTCLR = 1 << ${ledPinPos})
                                    <#lt>#define ${ledName}_Off()        (${PORT_REG_NAME}_REGS->GROUP[${myHash[ledGroup]}].PORT_OUTSET = 1 << ${ledPinPos})
                                </#if>
                            </#if>
                        </#if>
                    </#if>
                </#list>
            </#list>
        </#list>
    </#list>
</#if>

<#if (SWITCH_Name_List?size > 0)>
    <#list SWITCH_Name_List as switchName>
        <#list SWITCH_PortGroup_List as switchGroup>
            <#list SWITCH_PortPin_List as switchPinPos>
                <#list SWITCH_ActiveLevel_List as switchActiveLevel>
                    <#if switchName?counter == switchGroup?counter>
                        <#if switchName?counter == switchPinPos?counter>
                            <#if switchName?counter == switchActiveLevel?counter>
                                <#lt>/*** SWITCH Macros for ${switchName} ***/
                                <#lt>#define ${switchName}_Get()     ((${PORT_REG_NAME}_REGS->GROUP[${myHash[switchGroup]}].PORT_IN >> ${switchPinPos}) & 0x01)
                                <#if switchActiveLevel == "High">
                                    <#lt>#define ${switchName}_STATE_PRESSED  1
                                    <#lt>#define ${switchName}_STATE_RELEASED 0
                                <#else>
                                    <#lt>#define ${switchName}_STATE_PRESSED   0
                                    <#lt>#define ${switchName}_STATE_RELEASED  1
                                </#if>
                            </#if>
                        </#if>
                    </#if>
                </#list>
            </#list>
        </#list>
    </#list>
</#if>

<#if (VBUS_Name_List?size > 0)>
    <#list VBUS_Name_List as vbusName>
        <#list VBUS_PortGroup_List as vbusGroup>
            <#list VBUS_PortPin_List as vbusPinPos>
                <#list VBUS_ActiveLevel_List as vbusActiveLevel>
                    <#if vbusName?counter == vbusGroup?counter>
                        <#if vbusName?counter == vbusPinPos?counter>
                            <#if vbusName?counter == vbusActiveLevel?counter>
                                <#lt>/*** VBUS Macros for ${vbusName} ***/
                                <#if vbusActiveLevel == "High">
                                    <#lt>#define ${vbusName}_PowerEnable()         (${PORT_REG_NAME}_REGS->GROUP[${myHash[vbusGroup]}].PORT_OUTSET = 1 << ${vbusPinPos})
                                    <#lt>#define ${vbusName}_PowerDisable()        (${PORT_REG_NAME}_REGS->GROUP[${myHash[vbusGroup]}].PORT_OUTCLR = 1 << ${vbusPinPos})
                                <#else>
                                    <#lt>#define ${vbusName}_PowerEnable()         (${PORT_REG_NAME}_REGS->GROUP[${myHash[vbusGroup]}].PORT_OUTCLR = 1 << ${vbusPinPos})
                                    <#lt>#define ${vbusName}_PowerDisable()        (${PORT_REG_NAME}_REGS->GROUP[${myHash[vbusGroup]}].PORT_OUTSET = 1 << ${vbusPinPos})
                                </#if>
                            </#if>
                        </#if>
                    </#if>
                </#list>
            </#list>
        </#list>
    </#list>
</#if>

<#--
/*******************************************************************************
 End of File
*/
-->
