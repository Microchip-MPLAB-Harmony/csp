<#list 1..PIO_PIN_TOTAL>
"Pin Number","Pin ID","Custom Name","Function","Direction","Latch","Open Drain","PIO Interrupt","Pull Up","Pull Down","Glitch/Debounce Filter"${PIO_SLEWR_PRESENT?string(",Slew Rate Control","")},${PIO_DRIVER_PRESENT?string("Drive Strength", "")}
    <#items as INDEX>
        <#assign PIN_CHANNEL = .vars["PIN_" + INDEX + "_PIO_CHANNEL"]>
        <#if PIN_CHANNEL !="">
            <#assign PIN_NUMBER = .vars["PIN_" + INDEX + "_EXPORT_NAME"]?split(":")[0]>
            <#assign PIN_ID = .vars["PIN_" + INDEX + "_EXPORT_NAME"]?split(":")[1]>
            <#assign CUSTOM_NAME = .vars["PIN_" + INDEX + "_FUNCTION_NAME"]>
            <#assign FUNCTION = .vars["PIN_" + INDEX + "_FUNCTION_TYPE"]>
            <#if FUNCTION == "">
                <#assign FUNCTION = "Available">
                <#assign DIRECTION = "In">
                <#assign LATCH = "">
                <#assign OPEN_DRAIN = "">
                <#assign INTERRUPT = "">
                <#assign PULL_UP = "">
                <#assign PULL_DOWN = "">
                <#assign FILTER = "">
                <#assign SLEW_RATE = "">
                <#assign DRIVE_STRENGTH = "">
            <#else>
                <#if FUNCTION == "GPIO">
                    <#assign DIRECTION = .vars["PIN_" + INDEX + "_DIR"]>
                    <#if DIRECTION == "">
                        <#assign DIRECTION = "In">
                    </#if>
                <#else>
                    <#assign DIRECTION = "n/a">
                </#if>
                <#if DIRECTION == "Out">
                    <#assign LATCH = .vars["PIN_" + INDEX + "_LAT"]>
                    <#if LATCH == "">
                        <#assign LATCH = "Low">
                    </#if>
                <#else>
                    <#assign LATCH = "n/a">
                </#if>
                <#assign OPEN_DRAIN = (.vars["PIN_" + INDEX + "_OD"] != "")?string("Yes", "No")>
                <#assign INTERRUPT = .vars["PIN_" + INDEX + "_PIO_INTERRUPT"]>
                <#if INTERRUPT = "">
                    <#assign INTERRUPT = "Disabled">
                </#if>
                <#assign PULL_UP = (.vars["PIN_" + INDEX + "_PU"] != "")?string("Yes", "No")>
                <#assign PULL_DOWN = (.vars["PIN_" + INDEX + "_PD"] != "")?string("Yes", "No")>
                <#assign FILTER = .vars["PIN_" + INDEX + "_IFEN"]>
                <#if FILTER>
                    <#assign FILTER = "Disabled">
                <#else>
                    <#assign FILTER = .vars["PIN_" + INDEX + "_IFSCEN"]>
                    <#if FILTER == "SLCK">
                        <#assign FILTER = "Debounce Filter">
                    <#else>
                        <#assign FILTER = "Glitch Filter">
                    </#if>
                </#if>
                <#if PIO_SLEWR_PRESENT>
                    <#assign SLEW_RATE = (.vars["PIN_" + INDEX + "_SLEW_RATE"] != "")?string("Yes", "No")>
                <#else>
                    <#assign SLEW_RATE = "">
                </#if>
                <#if PIO_DRIVER_PRESENT>
                    <#assign DRIVE_STRENGTH = .vars["PIN_" + INDEX + "_DRV"]>
                    <#if DRIVE_STRENGTH = "">
                        <#assign DRIVE_STRENGTH = "Low">
                    </#if>
                <#else>
                    <#assign DRIVE_STRENGTH = "">
                </#if>
            </#if>
${PIN_NUMBER},${PIN_ID},${CUSTOM_NAME},${FUNCTION},${DIRECTION},${LATCH},${OPEN_DRAIN},${INTERRUPT},${PULL_UP},${PULL_DOWN},${FILTER}${PIO_SLEWR_PRESENT?string("," + SLEW_RATE, "")}${PIO_DRIVER_PRESENT?string("," + DRIVE_STRENGTH, "")}
        </#if>
    </#items>
</#list>
