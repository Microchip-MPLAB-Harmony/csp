import os.path

peripherals = {
                "EFC_6450"      : ["MEMORY"],
                "FLEXCOM_11268" : ["UART", "SPI", "I2C"],
                "I2SC_11241"    : ["I2S"],
                "NVMCTRL_U2409" : ["MEMORY"],
                "NVMCTRL_U2207" : ["MEMORY"],
                "NVMCTRL_U2802" : ["MEMORY"],
                "SERCOM_U2201"  : ["UART", "SPI", "I2C"],
                "SSC_6078"      : ["I2S"],
                "TWI_6212"      : ["I2C"],
                "TWI_11280"     : ["I2C"],
                "TWIHS_11210"   : ["I2C"],
                "USART_6089"    : ["UART"],
                "USART_11278"   : ["UART"],
    }

periphNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals")
modules = periphNode.getChildren()

for module in range (0, len(modules)):

    periphName = str(modules[module].getAttribute("name"))
    periphID = str(modules[module].getAttribute("id"))
    periphScript = "/peripheral/" + periphName.lower() + "_" + periphID + \
                    "/config/" + periphName.lower() + ".py"

    # Don't load system services. They will be loaded by family specific script
    if any(x in periphName for x in ["PORT", "PIO", "NVIC", "XDMAC", "DMAC", "OSCILLATOR", "PMC", "WDT"]):
        print("CSP: System Peripheral [" + periphName + " id=" + periphID + "]")
        continue

    # Check if peripheral has implementation
    if (os.path.isfile(Variables.get("__CSP_DIR") + periphScript)):

        instances = modules[module].getChildren()

        for instance in range (0, len(instances)):

            periphInstanceName = str(instances[instance].getAttribute("name"))

            if len(instances) == 1:
                periphInstanceName = periphInstanceName + "0"

            print("CSP: create component: Peripheral " + periphInstanceName + " (ID = " + periphID + ")")

            periphComponent = Module.CreateComponent(periphInstanceName.lower(), periphInstanceName.upper(), "/Peripherals/" +
                            periphName.upper() + "/", ".." + periphScript)

            periphComponent.setDisplayType("Peripheral Library")

            periphInstanceIndex = ''.join([i for i in periphInstanceName if i.isdigit()])

            key = periphName + "_" + periphID

            if key in peripherals:
                defaultCapablity = peripherals[key][0]

                if len(peripherals[key]) == 1:
                    periphComponent.addCapability(periphName + "_" + str(periphInstanceIndex), defaultCapablity)
                else:
                    for capablity in peripherals[key]:
                        capablityId = periphName + "_" + str(periphInstanceIndex) + "_" + capablity
                        periphComponent.addCapability(capablityId, capablity)
                        print "capablity is :- & defaultCapablity is :- & id is :-", capablity, defaultCapablity, capablityId
                        if capablity != defaultCapablity:
                            periphComponent.setCapabilityEnabled(capablityId, False)
            else:
                if periphName == "SMC":
                    smcRegModule    = Register.getRegisterModule("SMC")
                    smcRegGroup     = smcRegModule.getRegisterGroup("SMC_CS_NUMBER")
                    smcChipSelCount = smcRegGroup.getRegisterCount()
                    for smcChipSel in range(0, smcChipSelCount):
                        periphComponent.addCapability("smc_cs"  + str(smcChipSel), "SMC_CS", "SMC_CS"  + str(smcChipSel), False)
                else:
                    periphComponent.addCapability(periphName + "_" + str(periphInstanceIndex), periphName)
    else:
        print("CSP: Peripheral [" + periphName + " id=" + periphID + "] is not supported in MCC")
