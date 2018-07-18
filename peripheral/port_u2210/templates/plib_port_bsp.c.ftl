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
        <#assign pinport  = "PIN_" + i + "_PORT_PIN">
        <#assign pingroup = "PIN_" + i + "_PORT_GROUP">

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
    </#list>
</#macro>


<#--  =====================
      MACRO execution
      ===================== -->
<@mhc_process_leds/>
<@mhc_process_switches/>
</#compress>

<#if (LED_Name_List?size > 0)>
    /* Switch off LEDs */
    <#list LED_Name_List as led>
        ${led}_Off();
    </#list>
</#if>
<#--
/*******************************************************************************
 End of File
*/
-->
