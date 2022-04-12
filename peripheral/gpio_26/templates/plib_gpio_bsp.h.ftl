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

<#if (LED_Name_List?size > 0)>
    <#list LED_Name_List as ledName>
        <#list LED_PortNum_List as ledPort>
            <#list LED_PinNum_List as ledPinPos>
                <#list LED_ActiveLevel_List as ledActiveLevel>

                    <#if ledName?counter == ledPort?counter>
                        <#if ledName?counter == ledPinPos?counter>
                            <#if ledName?counter == ledActiveLevel?counter>
                                /*** LED Macros for ${ledName} ***/
                                    #define ${ledName}_Toggle()         (GPIO_REGS->GPIO_CTRL${ledPort}[${ledPinPos}] ^= GPIO_CTRL0_ALT_GPIO_DATA_Msk)
                                <#if ledActiveLevel == "High">
                                    #define ${ledName}_On()         (GPIO_REGS->GPIO_CTRL${ledPort}[${ledPinPos}] |= GPIO_CTRL0_ALT_GPIO_DATA_Msk)
                                    #define ${ledName}_Off()        (GPIO_REGS->GPIO_CTRL${ledPort}[${ledPinPos}] &= ~GPIO_CTRL0_ALT_GPIO_DATA_Msk)
                                <#else>
                                    #define ${ledName}_On()         (GPIO_REGS->GPIO_CTRL${ledPort}[${ledPinPos}] &= ~GPIO_CTRL0_ALT_GPIO_DATA_Msk)
                                    #define ${ledName}_Off()        (GPIO_REGS->GPIO_CTRL${ledPort}[${ledPinPos}] |= GPIO_CTRL0_ALT_GPIO_DATA_Msk)
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
        <#list SWITCH_PortChannel_List as switchPort>
            <#list SWITCH_PortPin_List as switchPinPos>
                <#list SWITCH_ActiveLevel_List as switchActiveLevel>

                    <#if switchName?counter == switchPort?counter>
                        <#if switchName?counter == switchPinPos?counter>
                            <#if switchName?counter == switchActiveLevel?counter>
                                /*** SWITCH Macros for ${switchName} ***/
                                #define ${switchName}_Get()     ((GPIO_REGS->GPIO_CTRL${switchPort}[${switchPinPos}] & GPIO_CTRL0_GPIO_INP_Msk)? 1:0)
                                <#if switchActiveLevel == "High">
                                    #define ${switchName}_STATE_PRESSED  1
                                    #define ${switchName}_STATE_RELEASED 0
                                <#else>
                                    #define ${switchName}_STATE_PRESSED  0
                                    #define ${switchName}_STATE_RELEASED  1
                                </#if>
                            </#if>
                        </#if>
                    </#if>

                </#list>
            </#list>
        </#list>
    </#list>
</#if>
</#compress>


<#--
/*******************************************************************************
 End of File
*/
-->
