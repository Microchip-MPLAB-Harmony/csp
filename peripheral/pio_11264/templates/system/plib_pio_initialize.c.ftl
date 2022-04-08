<#-- Initialize variables -->
<#compress>
<#assign TOTAL_NUM_OF_INT_USED = 0>
<#assign portNumCbList = [0]>

<#list 0..PORT_CHANNEL_TOTAL-1 as i>
  <#assign channel = "PORT_CHANNEL_" + i + "_NAME">
  <@"<#assign PORT_${.vars[channel]}_NUM_INT_PINS = 0>"?interpret />
</#list>

<#list 1..PIO_PIN_TOTAL as i>
    <#assign pinchannel = "PIN_" + i + "_PIO_CHANNEL">
    <#assign intConfig = "PIN_" + i + "_PIO_INTERRUPT">
    <#if .vars[intConfig]?has_content>
        <#if (.vars[intConfig] != "Disabled")>
          <@"<#assign PORT_${.vars[pinchannel]}_NUM_INT_PINS = PORT_${.vars[pinchannel]}_NUM_INT_PINS + 1>"?interpret />
        </#if>
    </#if>
</#list>

<#-- count total number of active interrupts and save it in variable -->
<#list 0..PORT_CHANNEL_TOTAL-1 as i>
    <#assign channel = "PORT_CHANNEL_" + i + "_NAME">
    <@"<#assign TOTAL_NUM_OF_INT_USED = TOTAL_NUM_OF_INT_USED + PORT_${.vars[channel]}_NUM_INT_PINS>"?interpret />
    <@"<#assign port${.vars[channel]}IndexStart = 0>"?interpret />
</#list>

</#compress>
<#-- PIO initialization sequence  -->
<#assign NEED_PIO_INIT = false>
<#assign PIO_PLIB_INIT>
<#assign PORT = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] >
<#assign PERFUNC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', "GPIO"] >
<#list PORT as port>
    <#list PERFUNC as func>
    <#assign PORT_MSKR = "PORT_" + port + "_MSKR_Value" + func >
    <#assign PORT_CFGR = "FUNC_" + func + "_CFGR_Value">
    <#if .vars[PORT_MSKR] != '0x0' && .vars[PORT_MSKR] != '0x0L'>
    <#lt> /* Port ${port} Peripheral function ${func} configuration */
    <#lt>	PIO${port}_REGS->PIO_MSKR = ${.vars[PORT_MSKR]}U;
    <#lt>	PIO${port}_REGS->PIO_CFGR = ${.vars[PORT_CFGR]}U;
    <#assign NEED_PIO_INIT = true>

    </#if>
    </#list>
    <#list 0..31 as pin>
    <#assign PORT_MSKR = "PORT_" + port + "_MSKR_Value" + pin >
    <#assign PORT_CFGR = "PORT_" + port + "_CFGR_Value" + pin >
    <#if .vars[PORT_CFGR] != '0x0'>
    <#lt> /* Port ${port} Pin ${pin} configuration */
    <#lt>	PIO${port}_REGS->PIO_MSKR = ${.vars[PORT_MSKR]}U;
    <#lt>	PIO${port}_REGS->PIO_CFGR = (PIO${port}_REGS->PIO_CFGR & (PIO_CFGR_FUNC_Msk)) | ${.vars[PORT_CFGR]}U;
    <#assign NEED_PIO_INIT = true>

    </#if>
    </#list>
    <#assign PORT_MSKR_GPIO = "PORT_" + port + "_MSKR_ValueGPIO">
    <#if .vars[PORT_MSKR_GPIO] != '0x0'>
    <#assign PORT_LATCH = "PORT_" + port + "_LATCH" >
    <#lt> /* Port ${port} Latch configuration */
    <#if .vars[PORT_LATCH] != '0x0'>
    <#lt>	PIO${port}_REGS->PIO_SODR = ${.vars[PORT_LATCH]}U;
    <#assign NEED_PIO_INIT = true>
    </#if>
    <#if .vars[PORT_MSKR_GPIO] != .vars[PORT_LATCH]>
    <#lt>	PIO${port}_REGS->PIO_CODR = ${.vars[PORT_MSKR_GPIO]}U${(.vars[PORT_LATCH] != '0x0')?string(" & ~" + .vars[PORT_LATCH] +"U", "")};
    <#assign NEED_PIO_INIT = true>
    </#if>
    </#if>

    <#assign PORT_ISR = "PORT_" + port + "_NUM_INT_PINS" >
    <#if .vars[PORT_ISR] != 0>
    /* Clear the ISR register */
    <#lt>	(uint32_t)PIO${port}_REGS->PIO_ISR;
    <#assign NEED_PIO_INIT = true>
  </#if>
</#list>
<#if PORT_SCLK_DIV?? && PORT_SCLK_DIV != 0>
<#lt> /* Slow Clock Divider Selection for Debouncing */
<#lt>	PIO_REGS->PIO_SCDR = ${PORT_SCLK_DIV}U;
<#assign NEED_PIO_INIT = true>

</#if>
<#if TOTAL_NUM_OF_INT_USED gt 0>
    uint32_t i;
    /* Initialize Interrupt Pin data structures */
    <#list 0..PORT_CHANNEL_TOTAL-1 as i>
        <#assign channel = "PORT_CHANNEL_" + i + "_NAME">
        <#if .vars[channel]?has_content>
            <@"<#assign portCurNumCb_${.vars[channel]} = 0>"?interpret />
        </#if>
    </#list>
    <#list 1..PIO_PIN_TOTAL as i>
        <#assign intConfig = "PIN_" + i + "_PIO_INTERRUPT">
        <#assign portChannel = "PIN_" + i + "_PIO_CHANNEL">
        <#assign portPosition = "PIN_" + i + "_PIO_PIN">
        <#if .vars[intConfig]?has_content>
            <#if (.vars[intConfig] != "Disabled")>
                <#lt>    portPinCbObj[${.vars["port${.vars[portChannel]}IndexStart"]} + ${.vars["portCurNumCb_${.vars[portChannel]}"]}].pin = PIO_PIN_P${.vars[portChannel]}${.vars[portPosition]};
                <#lt>    <@"<#assign portCurNumCb_${.vars[portChannel]} = portCurNumCb_${.vars[portChannel]} + 1>"?interpret />
            </#if>
        </#if>
    </#list>
    <#lt>    for(i=0U; i<${TOTAL_NUM_OF_INT_USED}U; i++)
    <#lt>    {
    <#lt>        portPinCbObj[i].callback = NULL;
    <#lt>    }
    <#assign NEED_PIO_INIT = true>
</#if>
</#assign>