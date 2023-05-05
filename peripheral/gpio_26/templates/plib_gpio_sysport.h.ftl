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
<#list 0..GPIO_NUM_GROUPS-1 as i>
    SYS_PORT_${i} = ${i},
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
<#list 0..GPIO_PIN_MAX_GPIO_PINS as k>
  <#assign GPIO_PIN_INDEX = "GPIO_PIN_INDEX_" + k>
  <#assign GPIO_PIN_PAD = "GPIO_PIN_PAD_" + k>
      <#if .vars[GPIO_PIN_PAD]?has_content>
          <#if (.vars[GPIO_PIN_PAD] != "None")>
              <#lt>    /* ${.vars[GPIO_PIN_PAD]} pin */
              <#lt>    SYS_PORT_PIN_${.vars[GPIO_PIN_PAD]} = ${.vars[GPIO_PIN_INDEX]}U,
          </#if>
      </#if>
</#list>

    /* This element should not be used in any of the PORTS APIs.
       It will be used by other modules or application to denote that none of the PORT Pin is used */
    SYS_PORT_PIN_NONE = -1

} SYS_PORT_PIN;