"""*****************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

import os.path

# Capability of different peripherals that higher level layers depends on
peripherals = {
                "EFC_6450"      : ["MEMORY"],
                "NVMCTRL_U2409" : ["MEMORY"],
                "NVMCTRL_U2207" : ["MEMORY"],
                "NVMCTRL_U2802" : ["MEMORY"],
                "NVMCTRL_03929" : ["MEMORY"],
                "FLEXCOM_11268" : ["UART", "SPI", "I2C"],
                "FLEXCOM_11277" : ["UART", "SPI", "I2C"],
                "SERCOM_U2201"  : ["UART", "SPI", "I2C"],
                "SPI_6088"      : ["SPI"],
                "TWI_6212"      : ["I2C"],
                "TWI_11280"     : ["I2C"],
                "TWIHS_11210"   : ["I2C"],
                "I2C_01441"     : ["I2C"],
                "I2C_00774"     : ["I2C"],
                "UART_02478"    : ["UART"],
                "UART_6418"     : ["UART"],
                "USART_6089"    : ["UART", "SPI"],
                "USART_11278"   : ["UART"],
                "UART_39"       : ["UART"],
                "QSPI_U2008"    : ["SQI","SPI"],
                "QSPI_44132"    : ["SQI","SPI"],
                "SQI_00206"     : ["SQI"],
                "SQI_04044"     : ["SQI"],
                "TC_U2212"      : ["TMR"],
                "TC_U2249"      : ["TMR"],
                "TC_44162"      : ["TMR"],
                "PIT_6079"      : ["TMR"],
                "RTT_6081"      : ["TMR"],
                "RTC_U2250"     : ["TMR"],
                "RTC_U2202"     : ["TMR"],
                "TMR_02815"     : ["TMR"],
                "TMR_00745"     : ["TMR"],
                "CCT_12"        : ["TMR"],
                "LCDC_11062"    : ["LCDC"],
                "SPI_01329"     : ["SPI"],
                "SPI_00753"     : ["SPI"],
                "UART_00734"    : ["UART"],
                "NVM_02819"     : ["MEMORY"],
                "NVM_01390"     : ["MEMORY"],
                "NVM_02629"     : ["MEMORY"],
                "NVM_00761"     : ["MEMORY"],
                "NVM_03140"     : ["MEMORY"],
                "NVM_02695"     : ["MEMORY"],
                "HEFC_44123"    : ["MEMORY"],
                "FCW_03433"     : ["MEMORY"],
                "SDMMC_44002"   : ["SDHC"],
                "SDHC_U2011"    : ["SDHC"],
                "HSMCI_6449"    : ["SDHC"],
                "SDHC_00187"    : ["SDHC"],
                "SDMMC_03592"   : ["SDHC"],
                "DBGU_6059"     : ["UART"],
                "PMP_00751"     : ["PMP"],
                "TMR1_00687"    : ["TMR"],
                "TMR1_02141"    : ["TMR"],
                "ADCHS_02508"   : ["ADC"],
                "AFEC_11147"    : ["ADC"],
                "ADC_U2500"     : ["ADC"],
                "ADC_U2247"     : ["ADC"],
                "ADC_U2204"     : ["ADC"],
                "ADC_44134"     : ["ADC"],
                "MCPWM_01477"   : ["PWM"],
                "PWM_6343"      : ["PWM"],
                "TCC_U2213"     : ["PWM"],
                "QEI_01494"     : ["QDEC"],
                "PDEC_U2263"    : ["QDEC", "HALL"],
                "PM_U2206"      : ["PM"],
                "PM_U2240"      : ["PM"],
                "PM_U2406"      : ["PM"],
                "SUPC_U2117"    : ["SUPC"],
                "SUPC_U2407"    : ["SUPC"],
                "CAN_U2003"     : ["CAN"],
                "MCAN_11273"    : ["CAN"],
                "SEFC_04463"    : ["MEMORY"]
}

# a dictionary to translate the new id mentioned in ATDF to old id used in csp
peripheral_ID_map = {
    "AC_03784"     : "AC_U2501",
    "AC_04704"     : "AC_U2501",
    "CAN_03723"    : "CAN_U2003",
    "CCL_03718"    : "CCL_U2225",
    "CCL_04702"    : "CCL_U2225",
    "CMCC_04727"   : "CMCC_U2015",
    "DMAC_04587"   : "DMAC_U2503",
    "DSU_03716"    : "DSU_U2810",
    "DSU_04850"    : "DSU_U2810",
    "DSU_05006"    : "DSU_U2410",
    "EIC_03706"    : "EIC_U2804",
    "EIC_04714"    : "EIC_U2254",
    "EVSYS_03601"  : "EVSYS_U2504",
    "EVSYS_04712"  : "EVSYS_U2504",
    "FREQM_03707"  : "FREQM_U2257",
    "FREQM_04703"  : "FREQM_U2257",
    "PAC_04701"    : "PAC_U2120",
    "PAC_03585"    : "PAC_U2120",
    "PDEC_03604"   : "PDEC_U2263",
    "PTC_03721"    : "PTC_U2215",
    "QSPI_04708"   : "QSPI_U2008",
    "RTC_03608"    : "RTC_U2250",
    "RTC_04715"    : "RTC_U2250",
    "SERCOM_03715" : "SERCOM_U2201",
    "SERCOM_04707" : "SERCOM_U2201",
    "TC_04705"     : "TC_U2249",
    "TCC_03610"    : "TCC_U2213",
    "TCC_04706"    : "TCC_U2213",
    "TRAM_03938"   : "TRAM_U2801",
    "TRNG_03597"   : "TRNG_U2242"
}

system_components = ["PORT", "PIO", "AIC", "NVIC", "XDMAC", "DMAC", "DMA", "OSCILLATOR", "PMC", "WDT", "DMT", "PAC", "MATRIX", "L2CC", "CMCC", "ECIA", "EC_REG_BANK"]

#RSTC, SUPC is loaded as a system component for PIC32CXMT devices
if ATDF.getNode("/avr-tools-device-file/devices/device").getAttribute("family") == "PIC32CXMT":
    system_components.extend(["RSTC", "SUPC"])

if("MIPS" in coreArch):
    coreTimerComponent = Module.CreateComponent("core_timer", "CORE TIMER", "/Peripherals/CORE TIMER/", "../peripheral/coretimer/config/coretimer.py")
    coreTimerComponent.addCapability("CORE_TIMER_TMR", "TMR")
    coreTimerComponent.setDisplayType("Peripheral Library")

valueGroup_OSCCON_SLPEN = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CRU\"]/value-group@[name=\"OSCCON__SLPEN\"]")
if valueGroup_OSCCON_SLPEN is None:
    valueGroup_OSCCON_SLPEN = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OSC\"]/value-group@[name=\"OSCCON__SLPEN\"]")
if valueGroup_OSCCON_SLPEN is not None:
    powerComponent = Module.CreateComponent("power", "POWER", "/Peripherals/POWER/", "../peripheral/power/config/power.py")
    powerComponent.setDisplayType("Peripheral Library")

periphNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals")
modules = periphNode.getChildren()

processor = Variables.get("__PROCESSOR")
# Certain members of certain families use the QSPI peripheral only in SPI mode - this makes the capability key/value match for those parts
if( (("SAMV7" in processor) or ("SAME7" in processor) or ("SAMS7" in processor)) and
    (("J19" in processor[-4:]) or ("J20" in processor[-4:]) or ("J21" in processor[-4:])) ):
    peripherals["QSPI_11171"]=["SPI"]
else:
    peripherals["QSPI_11171"]=["SPI","SQI"]   # most parts in the family support QSPI mode from the QSPI peripheral

#Cortex M7 devices support quadrature encoder mode
if( (("SAMV7" in processor) or ("SAME7" in processor) or ("SAMS7" in processor) or ("SAMRH71" in processor)) ):
    peripherals["TC_6082"]=["TMR","QDEC"]
else:
    peripherals["TC_6082"]=["TMR"]

# Create RAM Peripheral Library
if ("CEC173" not in processor):
    print("CSP: create component: Peripheral RAM")
    ramComponent = Module.CreateComponent("ram", "RAM", "/Peripherals/RAM/", "../peripheral/ram/config/ram.py")
    ramComponent.setDisplayType("Peripheral Library")
    ramComponent.addCapability("RAM_MEMORY", "MEMORY")


for module in range (0, len(modules)):

    periphName = str(modules[module].getAttribute("name"))
    periphID = str(modules[module].getAttribute("id"))
    if (periphName + "_" + periphID) in peripheral_ID_map:
        periphID = peripheral_ID_map[periphName + "_" + periphID].split("_")[1]

    periphScript = "/peripheral/" + periphName.lower() + "_" + periphID.lower() + \
                    "/config/" + periphName.lower() + ".py"

    # Don't load system services. They will be loaded by family specific script
    if any(x in periphName for x in system_components):
        print("CSP: System Peripheral [" + periphName + " id=" + periphID + "]")
        continue

    # Check if peripheral has implementation
    if (os.path.isfile(Variables.get("__CSP_DIR") + periphScript)):

        instances = modules[module].getChildren()
        for instance in range (0, len(instances)):

            periphInstanceName = str(instances[instance].getAttribute("name"))
            print("CSP: create component: Peripheral " + periphInstanceName + " (ID = " + periphID + ")")

            periphComponent = Module.CreateComponent(periphInstanceName.lower(), periphInstanceName.upper(), "/Peripherals/" +
                            periphName.upper() + "/", ".." + periphScript)

            periphComponent.setDisplayType("Peripheral Library")

            key = periphName + "_" + periphID

            if key in peripherals:
                for capablity in peripherals[key]:
                    capablityId = periphInstanceName + "_" + capablity
                    periphComponent.addCapability(capablityId, capablity)
            else:
                if periphName == "SMC":
                    smcRegGroup = ATDF.getNode( '/avr-tools-device-file/modules/module@[name="SMC"]/register-group@[name="SMC"]/register-group@[name="SMC_CS_NUMBER"]' )
                    smcChipSelCount = int( smcRegGroup.getAttribute( "count" ) )
                    for smcChipSel in range(0, smcChipSelCount):
                        if (("SAM9X60" in processor) and smcChipSel == 3) or (("SAM9X7" in processor) and smcChipSel == 2):
                            periphComponent.addCapability("smc_cs"  + str(smcChipSel), "NAND_CS", "SMC_CS"  + str(smcChipSel), False)
                        else:
                            periphComponent.addCapability("smc_cs"  + str(smcChipSel), "SMC_CS", "SMC_CS"  + str(smcChipSel), False)
                if periphName == "EBI":
                    ebiRegGroup = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="EBI"]').getChildren()
                    ebiChipSelCount = 0
                    for csregister in ebiRegGroup:
                        if("EBICS" in csregister.getAttribute("name")):
                            ebiChipSelCount += 1
                    if ebiChipSelCount == 0:
                        ebiRegGroup = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EBI\"]/register-group@[name=\"EBI\"]/register-group@[name=\"CS_X\"]")
                        if ebiRegGroup != None:
                            ebiChipSelCount = int(ebiRegGroup.getAttribute("count"))
                    for ebiChipSel in range(0, ebiChipSelCount):
                        periphComponent.addCapability("ebi_cs"  + str(ebiChipSel), "EBI_CS", "EBI_CS"  + str(ebiChipSel), False)
    else:
        print("CSP: Peripheral [" + periphName + " id=" + periphID + "] is not supported in MCC")
