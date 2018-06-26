import os.path

periphNames = map(str, Register.getRegisterModuleNames())
periphNames.sort()

# SMC Chip Select Register Group
smcRegModule    = Register.getRegisterModule("SMC")
smcRegGroup     = smcRegModule.getRegisterGroup("SMC_CS_NUMBER")
smcChipSelCount = smcRegGroup.getRegisterCount()

for periphName in periphNames:
    periphModule =  Register.getRegisterModule(periphName)
    periphInstanceCount = Peripheral.getModuleInstanceCount(periphName)
    periphID = periphModule.getID()
    periphScript = "/peripheral/" + periphName.lower() + "_" + periphID + \
                    "/config/" + periphName.lower() + ".py"

    # Don't load system services. They will be loaded by family specific script
    if any(x in periphName for x in ["PORT", "PIO", "NVIC", "XDMAC", "OSCILLATOR", "PMC", "WDT"]):
        print("CSP: System Peripheral [" + periphName + " id=" + periphID + "]")
        continue

    # Check if peripheral has implementation
    if (os.path.isfile(Variables.get("__CSP_DIR") + periphScript)):
        for periphInstance in range(0, periphInstanceCount):
            print("CSP: create component: Peripheral " + periphName + 
                    str(periphInstance) + " (ID = " + periphID + ")")
            periphComponent = Module.CreateComponent(periphName.lower() +
                            str(periphInstance), periphName.upper() +
                            str(periphInstance), "/Peripherals/" +
                            periphName.upper() + "/", ".." + periphScript)

            periphComponent.setDisplayType("Peripheral Library")

            if (periphName == "EFC"):
                periphComponent.addCapability(periphName + "_" + str(periphInstance), "MEMORY")
            elif (periphName == "TWIHS"):
                periphComponent.addCapability(periphName + "_" + str(periphInstance), "I2C")
            elif (periphName == "USART"):
                periphComponent.addCapability(periphName + "_" + str(periphInstance), "UART")
            elif (periphName == "SSC"):
                periphComponent.addCapability("I2S_" + str(periphInstance), "I2S")
            elif (periphName == "I2SC"):
                periphComponent.addCapability("I2S_" + str(periphInstance), "I2S")
            elif (periphName == "SMC"):
                for smcChipSel in range(0, smcChipSelCount):
                    periphComponent.addCapability("smc_cs"  + str(smcChipSel), "SMC_CS", "SMC_CS"  + str(smcChipSel), False)
            else:
                periphComponent.addCapability(periphName + "_" + str(periphInstance), periphName)

    else:
        print("CSP: Peripheral [" + periphName + " id=" + periphID + 
                "] is not supported in MCC")

