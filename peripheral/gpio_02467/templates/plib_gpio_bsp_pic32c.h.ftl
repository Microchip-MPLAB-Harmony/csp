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

<#if (LED_Name_List?size > 0)>
	<#list LED_Name_List as ledName>
		<#list LED_PortChannel_List as ledChannel>
			<#list LED_PortPin_List as ledPinPos>
				<#list LED_ActiveLevel_List as ledActiveLevel>

					<#if ledName?counter == ledChannel?counter>
						<#if ledName?counter == ledPinPos?counter>
							<#if ledName?counter == ledActiveLevel?counter>
								/*** LED Macros for ${ledName} ***/
								#define ${ledName}_Toggle()     (GPIO${ledChannel}_REGS->GPIO_LATINV = (1UL<<${ledPinPos}))
								#define ${ledName}_Get()        ((GPIO${ledChannel}_REGS->GPIO_PORT >> ${ledPinPos}) & 0x1U)
								<#if ledActiveLevel == "High">
									#define ${ledName}_On()         (GPIO${ledChannel}_REGS->GPIO_LATSET = (1UL<<${ledPinPos}))
									#define ${ledName}_Off()        (GPIO${ledChannel}_REGS->GPIO_LATCLR = (1UL<<${ledPinPos}))
								<#else>
									#define ${ledName}_On()         (GPIO${ledChannel}_REGS->GPIO_LATCLR = (1UL<<${ledPinPos}))
									#define ${ledName}_Off()        (GPIO${ledChannel}_REGS->GPIO_LATSET = (1UL<<${ledPinPos}))
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
		<#list SWITCH_PortChannel_List as switchChannel>
			<#list SWITCH_PortPin_List as switchPinPos>
				<#list SWITCH_ActiveLevel_List as switchActiveLevel>

					<#if switchName?counter == switchChannel?counter>
						<#if switchName?counter == switchPinPos?counter>
							<#if switchName?counter == switchActiveLevel?counter>
								/*** SWITCH Macros for ${switchName} ***/
								#define ${switchName}_Get()     ((GPIO${switchChannel}_REGS->GPIO_PORT >> ${switchPinPos}) & 0x1U)
								<#if switchActiveLevel == "High">
									#define ${switchName}_STATE_PRESSED  1U
									#define ${switchName}_STATE_RELEASED 0U
								<#else>
									#define ${switchName}_STATE_PRESSED   0U
									#define ${switchName}_STATE_RELEASED  1U
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
		<#list VBUS_PortChannel_List as vbusChannel>
			<#list VBUS_PortPin_List as vbusPinPos>
				<#list VBUS_ActiveLevel_List as vbusActiveLevel>

					<#if vbusName?counter == vbusChannel?counter>
						<#if vbusName?counter == vbusPinPos?counter>
							<#if vbusChannel?counter == vbusActiveLevel?counter>
								/*** VBUS Macros for ${vbusName} ***/
								<#if vbusActiveLevel == "High">
									#define ${vbusName}_PowerEnable()         (GPIO${vbusChannel}_REGS->GPIO_LATSET = (1UL<<${vbusPinPos}))
									#define ${vbusName}_PowerDisable()        (GPIO${vbusChannel}_REGS->GPIO_LATCLR = (1UL<<${vbusPinPos}))
								<#else>
									#define ${vbusName}_PowerEnable()         (GPIO${vbusChannel}_REGS->GPIO_LATCLR = (1UL<<${vbusPinPos}))
									#define ${vbusName}_PowerDisable()        (GPIO${vbusChannel}_REGS->GPIO_LATSET = (1UL<<${vbusPinPos}))
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
