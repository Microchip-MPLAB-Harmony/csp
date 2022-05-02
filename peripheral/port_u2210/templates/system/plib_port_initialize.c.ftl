<#assign NEED_PORT_INIT = false>
<#assign PLIB_PORT_INIT>
<#list 0..PORT_GROUP_COUNT as n>
    <#assign PORT_GROUP = "PORT_GROUP_"+ n>
    <#assign PORT_GROUP_NAME = "PORT_GROUP_NAME_" + n>
    <#assign PORT_GROUP_EVCTRL = "PORT_GROUP_" + n + "_EVCTRL">
        <#if .vars[PORT_GROUP]!false>
            <#lt>   /************************** GROUP ${.vars[PORT_GROUP_NAME]} Initialization *************************/
            <#assign PORT_DIR = "PORT_GROUP_" + n + "_DIR">
            <#assign PORT_OUT = "PORT_GROUP_" + n + "_OUT">
            <#assign PORT_CTRL = "PORT_GROUP_" + n + "_CTRL">
            <#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
              <#assign PORT_NONSEC = "PORT_GROUP_" + n + "_NONSEC">
            </#if>
                <#if "${.vars[PORT_DIR]}" != "0x0">
                    <#lt>   ${PORT_REG_NAME}_REGS->GROUP[${.vars[PORT_GROUP_NAME]}].PORT_DIR = ${.vars[PORT_DIR]};
                    <#assign NEED_PORT_INIT = true>
                </#if>
                <#if "${.vars[PORT_OUT]}" != "0x0">
                    <#lt>   ${PORT_REG_NAME}_REGS->GROUP[${.vars[PORT_GROUP_NAME]}].PORT_OUT = ${.vars[PORT_OUT]};
                    <#assign NEED_PORT_INIT = true>
                </#if>
                <#if "${.vars[PORT_CTRL]}" != "0x0">
                    <#lt>   ${PORT_REG_NAME}_REGS->GROUP[${.vars[PORT_GROUP_NAME]}].PORT_CTRL = ${.vars[PORT_CTRL]};
                    <#assign NEED_PORT_INIT = true>
                </#if>
                <#list 0..31 as i>
                    <#assign PORT_PINCONFIG = "PORT_GROUP_" + n + "_PINCFG" + i>
                    <#assign PORT_PIN_USED = "PORT_GROUP_" + n + "_PIN_" + i  + "_USED">
                    <#assign PORT_GROUP_PINCFG_INDEX = i>
                    <#if "${.vars[PORT_PIN_USED]?c}" == "true">
                        <#lt>   ${PORT_REG_NAME}_REGS->GROUP[${.vars[PORT_GROUP_NAME]}].PORT_PINCFG[${PORT_GROUP_PINCFG_INDEX}] = ${.vars[PORT_PINCONFIG]};
                        <#assign NEED_PORT_INIT = true>
                    </#if>
                </#list>

                <#list 0..15 as i>
                    <#assign PORT_PINMUX = "PORT_GROUP_" + n + "_PMUX"+ i>
                    <#assign PORT_INDEX = i>
                    <#assign PORT_PMUX_PMUXE_USED = "PORT_GROUP_" + n + "_PIN_" + (i * 2) + "_USED">
                    <#assign PORT_PMUX_PMUXO_USED = "PORT_GROUP_" + n + "_PIN_" + ((i * 2) + 1) + "_USED">
                    <#if (.vars[PORT_PMUX_PMUXE_USED] == true || .vars[PORT_PMUX_PMUXO_USED] == true)>
                        <#lt>   ${PORT_REG_NAME}_REGS->GROUP[${.vars[PORT_GROUP_NAME]}].PORT_PMUX[${PORT_INDEX}] = ${.vars[PORT_PINMUX]};
                        <#assign NEED_PORT_INIT = true>
                    </#if>
                </#list>
                <#if .vars[PORT_GROUP_EVCTRL]??>
                <#if "${.vars[PORT_GROUP_EVCTRL]}" != "0x0">
                    <#lt>   ${PORT_REG_NAME}_REGS->GROUP[${.vars[PORT_GROUP_NAME]}].PORT_EVCTRL = ${.vars[PORT_GROUP_EVCTRL]};
                    <#assign NEED_PORT_INIT = true>
                </#if>
                </#if>

                <#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
                  <#if "${.vars[PORT_NONSEC]}" != "0x0">
                    <#lt>   ${PORT_REG_NAME}_REGS->GROUP[${.vars[PORT_GROUP_NAME]}].PORT_NONSEC = 0x${.vars[PORT_NONSEC]};
                    <#assign NEED_PORT_INIT = true>
                  </#if>
                </#if>
        </#if>
</#list>
</#assign>