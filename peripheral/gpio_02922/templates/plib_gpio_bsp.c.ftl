<#--  =====================
      MACRO mhc_process_leds
      ===================== -->
<#compress>
<#macro mhc_process_leds>
	<#assign LED_Name_List = []>
	<#assign LED_PortPin_List = []>
	<#assign LED_PortChannel_List = []>
	<#assign LED_ActiveLevel_List = []>

	<#list 1..GPIO_PIN_TOTAL as i>
		<#assign functype = "BSP_PIN_" + i + "_FUNCTION_TYPE">
		<#assign funcname = "BSP_PIN_" + i + "_FUNCTION_NAME">
		<#assign pinport = "BSP_PIN_" + i + "_PORT_PIN">
		<#assign pinchannel = "BSP_PIN_" + i + "_PORT_CHANNEL">

		<#if .vars[functype]?has_content>
			<#if (.vars[functype] == "LED_AH") || (.vars[functype] == "LED_AL")>
				<#if .vars[funcname]?has_content>
					<#if .vars[pinport]?has_content>
						<#if .vars[pinchannel]?has_content>

							<#assign LED_Name_List = LED_Name_List + [.vars[funcname]]>
							<#assign LED_PortPin_List = LED_PortPin_List + [.vars[pinport]]>
							<#assign LED_PortChannel_List = LED_PortChannel_List + [.vars[pinchannel]]>
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
	<#assign SWITCH_PortChannel_List = []>
	<#assign SWITCH_ActiveLevel_List = []>

	<#list 1..GPIO_PIN_TOTAL as i>
		<#assign functype = "BSP_PIN_" + i + "_FUNCTION_TYPE">
		<#assign funcname = "BSP_PIN_" + i + "_FUNCTION_NAME">
		<#assign pinport = "BSP_PIN_" + i + "_PORT_PIN">
		<#assign pinchannel = "BSP_PIN_" + i + "_PORT_CHANNEL">

		<#if .vars[functype]?has_content>
			<#if (.vars[functype] == "SWITCH_AH") || (.vars[functype] == "SWITCH_AL")>
				<#if .vars[funcname]?has_content>
					<#if .vars[pinport]?has_content>
						<#if .vars[pinchannel]?has_content>

							<#assign SWITCH_Name_List = SWITCH_Name_List + [.vars[funcname]]>
							<#assign SWITCH_PortPin_List = SWITCH_PortPin_List + [.vars[pinport]]>
							<#assign SWITCH_PortChannel_List = SWITCH_PortChannel_List + [.vars[pinchannel]]>
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
      MACRO mhc_process_vbus
      ===================== -->
<#macro mhc_process_vbus>
	<#assign VBUS_Name_List = []>
	<#assign VBUS_PortPin_List = []>
	<#assign VBUS_PortChannel_List = []>
	<#assign VBUS_ActiveLevel_List = []>

	<#list 1..GPIO_PIN_TOTAL as i>
		<#assign functype = "BSP_PIN_" + i + "_FUNCTION_TYPE">
		<#assign funcname = "BSP_PIN_" + i + "_FUNCTION_NAME">
		<#assign pinport = "BSP_PIN_" + i + "_PORT_PIN">
		<#assign pinchannel = "BSP_PIN_" + i + "_PORT_CHANNEL">

		<#if .vars[functype]?has_content>
			<#if (.vars[functype] == "VBUS_AH") || (.vars[functype] == "VBUS_AL") || (.vars[functype] == "VBUS")>
				<#if .vars[funcname]?has_content>
					<#if .vars[pinport]?has_content>
						<#if .vars[pinchannel]?has_content>

							<#assign VBUS_Name_List = VBUS_Name_List + [.vars[funcname]]>
							<#assign VBUS_PortPin_List = VBUS_PortPin_List + [.vars[pinport]]>
							<#assign VBUS_PortChannel_List = VBUS_PortChannel_List + [.vars[pinchannel]]>
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
	</#list>
</#macro>


<#--  =====================
      MACRO execution
      ===================== -->
<@mhc_process_leds/>
<@mhc_process_switches/>
<@mhc_process_vbus/>
</#compress>

<#if (VBUS_Name_List?size > 0)>
    /* Disable VBUS power */
	<#list VBUS_Name_List as vbus>
		${vbus}_PowerDisable();
	</#list>
</#if>

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
