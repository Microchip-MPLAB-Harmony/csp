<#--  =====================
      MACRO mhc_process_leds
      ===================== -->
<#compress>
<#macro mhc_process_leds>
    <#assign LED_Name_List = []>
    <#assign LED_PortNum_List = []>
    <#assign LED_PinNum_List = []>
    <#assign LED_ActiveLevel_List = []>

    <#list 1..GPIO_PIN_MAX_INDEX as i>
        <#assign functype = "PIN_" + i + "_FUNCTION_TYPE">
        <#assign funcname = "PIN_" + i + "_FUNCTION_NAME">
        <#assign ctrlRegNum = "PIN_" + i + "_GPIO_CTRL_REG_NUM">
        <#assign ctrlRegIndex = "PIN_" + i + "_GPIO_CTRL_REG_INDEX">

        <#if .vars[functype]?has_content>
            <#if (.vars[functype] == "LED_AH") || (.vars[functype] == "LED_AL")>
                <#if .vars[funcname]?has_content>
                    <#if .vars[ctrlRegNum]?has_content>
                        <#if .vars[ctrlRegIndex]?has_content>

                            <#assign LED_Name_List = LED_Name_List + [.vars[funcname]]>
                            <#assign LED_PortNum_List = LED_PortNum_List + [.vars[ctrlRegNum]]>
                            <#assign LED_PinNum_List = LED_PinNum_List + [.vars[ctrlRegIndex]]>
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
    <#assign SWITCH_PortNum_List = []>
    <#assign SWITCH_PinNum_List = []>
    <#assign SWITCH_ActiveLevel_List = []>

    <#list 1..GPIO_PIN_MAX_INDEX as i>
        <#assign functype = "PIN_" + i + "_FUNCTION_TYPE">
        <#assign funcname = "PIN_" + i + "_FUNCTION_NAME">
        <#assign ctrlRegNum = "PIN_" + i + "_GPIO_CTRL_REG_NUM">
        <#assign ctrlRegIndex = "PIN_" + i + "_GPIO_CTRL_REG_INDEX">

        <#if .vars[functype]?has_content>
            <#if (.vars[functype] == "SWITCH_AH") || (.vars[functype] == "SWITCH_AL")>
                <#if .vars[funcname]?has_content>
                    <#if .vars[ctrlRegNum]?has_content>
                        <#if .vars[ctrlRegIndex]?has_content>

                            <#assign SWITCH_Name_List = SWITCH_Name_List + [.vars[funcname]]>
                            <#assign SWITCH_PortNum_List = SWITCH_PortPin_List + [.vars[ctrlRegNum]]>
                            <#assign SWITCH_PinNum_List = SWITCH_PortChannel_List + [.vars[ctrlRegIndex]]>
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
