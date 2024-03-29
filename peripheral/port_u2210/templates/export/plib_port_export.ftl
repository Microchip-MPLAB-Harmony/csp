<#list 1..PORT_PIN_COUNT>
Pin Number,Pin ID,Custom Name,Function,Mode, Direction,Latch,Pull Up,Pull Down${PORT_GROUP_PINCFG_ODRAIN?string(",Open Drain", "")}${PORT_GROUP_PINCFG_SLEWRATE?string(",Slew Rate Control","")}${PORT_GROUP_PINCFG_DRVSTR?string(",Drive Strength","")}
    <#items as INDEX>
        <#assign PORT_GROUP = .vars["PIN_" + INDEX + "_PORT_GROUP"]>
        <#if PORT_GROUP !="">
            <#assign PIN_NUMBER = .vars["PIN_" + INDEX + "_EXPORT_NAME"]?split(":")[0]>
            <#assign PIN_ID = .vars["PIN_" + INDEX + "_EXPORT_NAME"]?split(":")[1]>
            <#assign CUSTOM_NAME = .vars["PIN_" + INDEX + "_FUNCTION_NAME"]>
            <#assign DIRECTION = .vars["PIN_" + INDEX + "_DIR"]>
            <#assign INPUT_ENABLE = .vars["PIN_" + INDEX + "_INEN"]>
            <#assign PULL = .vars["PIN_" + INDEX + "_PULLEN"]>
            <#assign LATCH = .vars["PIN_" + INDEX + "_LAT"]>
            <#assign MODE = (.vars["PIN_" + INDEX + "_MODE"] == "")?string("Digital", "Analog")>
            <#if DIRECTION = "Out" &&  INPUT_ENABLE == "True">
                <#assign DIRECTION ="In/Out">
            <#elseif DIRECTION = "" && INPUT_ENABLE == "True">
                <#assign DIRECTION ="In">
            <#elseif DIRECTION = "" && INPUT_ENABLE == "">
                <#assign DIRECTION = "High Impedance">
            </#if>
            <#if MODE == "Digital"  && (DIRECTION == "In" || DIRECTION =="High Impedance")>
                <#assign PULL_UP = (PULL == "True" && LATCH == "High")?string("Yes", "No")>
                <#assign PULL_DOWN = (PULL == "True" && LATCH == "")?string("Yes", "No")>
            <#else>
                <#assign PULL_UP = "">
                <#assign PULL_DOWN = "">
            </#if>
            <#if PORT_GROUP_PINCFG_ODRAIN>
                <#assign OPEN_DRAIN = (.vars["PIN_" + INDEX + "_ODRAIN"] == "True")?string("Yes", "No")>
            <#else>
                <#assign OPEN_DRAIN = "">
            </#if>
            <#if PORT_GROUP_PINCFG_SLEWRATE>
                <#assign SLEW_RATE = .vars["PIN_" + INDEX + "_SLEWRATE"]>
            <#else>
                <#assign SLEW_RATE = "">
            </#if>
            <#if PORT_GROUP_PINCFG_DRVSTR>
                <#assign DRIVE_STR = .vars["PIN_" + INDEX + "_DRVSTR"]>
            <#else>
                <#assign DRIVE_STR = "">
            </#if>
            <#assign FUNCTION = .vars["PIN_" + INDEX + "_FUNCTION_TYPE"]>
            <#if FUNCTION == "">
                <#assign FUNCTION = "Available">
                <#if DIRECTION == "High Impedance">
                    <#assign DIRECTION = "">
                </#if>
                <#assign PULL_UP = (PULL_UP == "Yes")?string(PULL_UP, "")>
                <#assign PULL_DOWN = (PULL_DOWN == "Yes")?string(PULL_DOWN, "")>
                <#assign MODE = "">
                <#assign LATCH = "">
            <#else>
                <#if DIRECTION == "Out" || DIRECTION == "In/Out">
                    <#assign LATCH = .vars["PIN_" + INDEX + "_LAT"]>
                    <#if LATCH == "">
                        <#assign LATCH = "Low">
                    </#if>
                <#else>
                    <#assign LATCH = "n/a">
                </#if>
            </#if>
${PIN_NUMBER},${PIN_ID},${CUSTOM_NAME},${FUNCTION},${MODE},${DIRECTION},${LATCH},${PULL_UP},${PULL_DOWN}${PORT_GROUP_PINCFG_ODRAIN?string("," + OPEN_DRAIN, "")}${PORT_GROUP_PINCFG_SLEWRATE?string("," + SLEW_RATE, "")}${PORT_GROUP_PINCFG_DRVSTR?string("," + DRIVE_STR, "")}
        </#if>
    </#items>
</#list>
