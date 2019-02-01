
<#compress> <#-- To remove unwanted new lines -->

<#list 0..GPIO_CHANNEL_TOTAL-1 as i>
    <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
    <#if .vars[channel]?has_content>
        <@"<#assign PORT${.vars[channel]}_Pin_List = []>"?interpret />
    </#if>
</#list>

<#list 1..GPIO_PIN_TOTAL as i>
    <#assign pinPort = "BSP_PIN_" + i + "_PORT_PIN">
    <#assign pinChannel = "BSP_PIN_" + i + "_PORT_CHANNEL">

    <#if .vars[pinPort]?has_content>
        <#if .vars[pinChannel]?has_content && .vars[pinChannel] != "None">
                <@"<#assign PORT${.vars[pinChannel]}_Pin_List = PORT${.vars[pinChannel]}_Pin_List + [.vars[pinPort]]>"?interpret />
        </#if>
    </#if>
</#list>


</#compress>
// *****************************************************************************
// *****************************************************************************
// Section: Data types and constants
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
/* Sys Port

  Summary:
    Identifies the available Port Channels.

  Description:
    This enumeration identifies the available Port Channels.

  Remarks:
    The caller should not rely on the specific numbers assigned to any of
    these values as they may change from one processor to the next.

    Not all ports are available on all devices.  Refer to the specific
    device data sheet to determine which ports are supported.
*/


typedef enum
{
<#list 0..GPIO_CHANNEL_TOTAL-1 as i>
    <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
    <#if .vars[channel]?has_content>
        <#if (.vars["PORT${.vars[channel]}_Pin_List"])?has_content>
                <#lt>    SYS_PORT_${.vars[channel]} = ${i},
        </#if>
    </#if>
</#list>

} SYS_PORT;


// *****************************************************************************
/* Sys Port Pins

  Summary:
    Identifies the available port pins.

  Description:
    This enumeration identifies the available port pins.

  Remarks:
    The caller should not rely on the specific numbers assigned to any of
    these values as they may change from one processor to the next.

    Not all pins are available on all devices.  Refer to the specific
    device data sheet to determine which pins are supported.
*/

typedef enum
{

<#list 0..GPIO_CHANNEL_TOTAL-1 as i>
    <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
    <#if .vars[channel]?has_content>
        <#if .vars["PORT${.vars[channel]}_Pin_List"]?has_content>
            <@"<#assign PORT${.vars[channel]}_Pin_List =  PORT${.vars[channel]}_Pin_List?sort>"?interpret />
            <#list .vars["PORT${.vars[channel]}_Pin_List"] as pin>
                <#lt>    SYS_PORT_PIN_R${.vars[channel]}${pin} = ${pin+(16*i)},
            </#list>
        </#if>
    </#if>
</#list>

    /* This element should not be used in any of the PORTS APIs.
       It will be used by other modules or application to denote that none of the PORT Pin is used */
    SYS_PORT_PIN_NONE = -1
} SYS_PORT_PIN;
