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
<#list 0..PORT_GROUP_COUNT - 1 as i>
    <#assign PORT_GROUP_INDEX = i>
    <#assign PORT_GROUP_NAME = "PORT_GROUP_NAME_" + i>
    SYS_PORT_${.vars[PORT_GROUP_NAME]} = ${PORT_REG_NAME}_BASE_ADDRESS + ${.vars[PORT_GROUP_NAME]} * (0x80),
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
<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
  <#list 0..PORT_PIN_COUNT as k>
      <#assign pinIndex = k + 1>
      <#assign pinisSecure = "PIN_" + pinIndex + "_IS_NON_SECURE">
      <#assign PORT_PIN  = "PIN_" + pinIndex + "_PORT_PIN">
      <#assign PORT_GROUP = "PIN_" + pinIndex + "_PORT_GROUP">
      <#if (.vars[pinisSecure]?has_content) && (.vars[pinisSecure]) == "NON-SECURE">
          <#if .vars[PORT_PIN]?has_content>
              <#if .vars[PORT_GROUP]?has_content>
                  <#lt>    /* P${.vars[PORT_GROUP]}${.vars[PORT_PIN]?string["00"]} pin */
                  <#lt>    SYS_PORT_PIN_P${.vars[PORT_GROUP]}${.vars[PORT_PIN]?string["00"]} = ${.vars[PORT_PIN]},

              </#if>
          </#if>
      </#if>
  </#list>
<#else>
  <#list 0..PORT_PIN_MAX_INDEX as k>
      <#assign PORT_PIN_INDEX = "PORT_PIN_INDEX_" + k>
      <#assign PORT_PIN_PAD = "PORT_PIN_PAD_" + k>
          <#if .vars[PORT_PIN_PAD]?has_content>
              <#if (.vars[PORT_PIN_PAD] != "None")>
                  <#lt>    SYS_PORT_PIN_${.vars[PORT_PIN_PAD]} = ${.vars[PORT_PIN_INDEX]},

              </#if>
          </#if>
  </#list>
</#if>
    /* This element should not be used in any of the PORTS APIs.
       It will be used by other modules or application to denote that none of the PORT Pin is used */
    SYS_PORT_PIN_NONE = -1
} SYS_PORT_PIN;