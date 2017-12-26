def instantiateComponent(twiComponent):
	num = twiComponent.getID()[-1:]
	print("Running TWI" + str(num))

	#main menu
	twiMenu = twiComponent.createMenuSymbol(None, None)
	twiMenu.setLabel("Hardware Settings ")

	#instance index
	twiIndex = twiComponent.createIntegerSymbol("INDEX", twiMenu)
	twiIndex.setVisible(False)
	twiIndex.setDefaultValue(int(num))

	#operation mode
	opModeValues = ["MASTER"]
	
	twiOpMode = twiComponent.createComboSymbol("TWI_OPMODE", twiMenu, opModeValues)
	twiOpMode.setLabel("TWI Operation Mode")
	twiOpMode.setDefaultValue("MASTER")
	
	#Number of Transaction request blocks
	twiNumTRBs = twiComponent.createIntegerSymbol("TWI_NUM_TRBS", twiMenu)
	twiNumTRBs.setLabel("Number of TRB's")
	twiNumTRBs.setDefaultValue(1)
	twiNumTRBs.setValue("TWI_NUM_TRBS", True, 1)
	twiNumTRBs.setMax(255)

	#Clock speed
	twiClockSpeed = twiComponent.createIntegerSymbol("TWI_CLK_SPEED", twiMenu)
	twiClockSpeed.setLabel("Clock Speed")
	twiClockSpeed.setDefaultValue(400000)
	twiClockSpeed.setMax(400000)

	cldiv, chdiv, ckdiv = getTWIClockDividerValue(twiClockSpeed.getValue())
	
	#CLDIV
	twiSym_CWGR_CLDIV = twiComponent.createIntegerSymbol("TWI_CWGR_CLDIV", twiMenu)
	twiSym_CWGR_CLDIV.setVisible(False)
	twiSym_CWGR_CLDIV.setValue("TWI_CWGR_CLDIV", cldiv, 1)
	twiSym_CWGR_CLDIV.setDependencies(setLowClockDividerValue, ["TWI_CLK_SPEED"])
	
	#CHDIV
	twiSym_CWGR_CHDIV = twiComponent.createIntegerSymbol("TWI_CWGR_CHDIV", twiMenu)
	twiSym_CWGR_CHDIV.setVisible(False)
	twiSym_CWGR_CHDIV.setValue("TWI_CWGR_CHDIV", chdiv, 1)
	twiSym_CWGR_CHDIV.setDependencies(setHighClockDividerValue, ["TWI_CLK_SPEED"])
	
	#CKDIV
	twiSym_CWGR_CKDIV = twiComponent.createIntegerSymbol("TWI_CWGR_CKDIV", twiMenu)
	twiSym_CWGR_CKDIV.setVisible(False)
	twiSym_CWGR_CKDIV.setValue("TWI_CWGR_CKDIV", ckdiv, 1)
	twiSym_CWGR_CKDIV.setDependencies(setClockDividerValue, ["TWI_CLK_SPEED"])

	REG_MODULE_TWI = Register.getRegisterModule("TWI")
	
	#Master Header
	if twiOpMode.getValue() == "MASTER":
		print("Operational Mode = ", twiOpMode.getValue())
		twiMasterHeaderFile = twiComponent.createFileSymbol(None, None)
		twiMasterHeaderFile.setSourcePath("../peripheral/twi_" + REG_MODULE_TWI.getID() + "/plib_twi_master.h")
		twiMasterHeaderFile.setOutputName("plib_twi_master.h")
		twiMasterHeaderFile.setDestPath("/peripheral/twi/")
		twiMasterHeaderFile.setProjectPath("/peripheral/twi/")
		twiMasterHeaderFile.setType("HEADER")
		twiMasterHeaderFile.setOverwrite(False)

	#Source File
	twiMainSourceFile = twiComponent.createFileSymbol(None, None)
	twiMainSourceFile.setSourcePath("../peripheral/twi_" + REG_MODULE_TWI.getID() + "/templates/plib_twi.c.ftl")
	twiMainSourceFile.setOutputName("plib_twi" + str(num) + ".c")
	twiMainSourceFile.setDestPath("/peripheral/twi/")
	twiMainSourceFile.setProjectPath("/peripheral/twi/")
	twiMainSourceFile.setType("SOURCE")
	twiMainSourceFile.setMarkup(True)
	
	#Instance Header File
	twiInstHeaderFile = twiComponent.createFileSymbol(None, None)
	twiInstHeaderFile.setSourcePath("../peripheral/twi_" + REG_MODULE_TWI.getID() + "/templates/plib_twi.h.ftl")
	twiInstHeaderFile.setOutputName("plib_twi" + str(num) + ".h")
	twiInstHeaderFile.setDestPath("/peripheral/twi/")
	twiInstHeaderFile.setProjectPath("/peripheral/twi/")
	twiInstHeaderFile.setType("HEADER")
	twiInstHeaderFile.setMarkup(True)

def getMasterClockFreq():
        return 150000000

def getTWILowLevelTimeLimit():
        return 384000

def getTWIClockDividerMaxValue():
        return 255

def getTWIClockDividerMinValue():
        return 7
        
def getTWIClockDividerValue( clkSpeed ):

        cldiv = chdiv = ckdiv = 0

        if clkSpeed > getTWILowLevelTimeLimit():
                cldiv = getMasterClockFreq() // ( getTWILowLevelTimeLimit() * 2) - 3
                chdiv = getMasterClockFreq() // ((clkSpeed + (clkSpeed - getTWILowLevelTimeLimit())) * 2 ) - 3

                while cldiv > getTWIClockDividerMaxValue() and ckdiv < getTWIClockDividerMinValue():
                        ckdiv += 1
                        cldiv //= 2

                while chdiv > getTWIClockDividerMaxValue() and ckdiv < getTWIClockDividerMinValue():
                        ckdiv += 1
                        chdiv //= 2
        else:
                cldiv = getMasterClockFreq() / ( clkSpeed * 2 ) - 3

                while cldiv > getTWIClockDividerMaxValue() and ckdiv < getTWIClockDividerMinValue():
                        ckdiv += 1
                        cldiv //= 2

                chdiv = cldiv

        return cldiv, chdiv, ckdiv
                        
def setLowClockDividerValue( twiSym_CWGR_CLDIV, twiClockSpeed):

        cldiv = getTWIClockDividerValue(twiClockSpeed.getValue())[0]
        twiSym_CWGR_CLDIV.setValue("TWI_CWGR_CLDIV", cldiv, 1)
        
def setHighClockDividerValue( twiSym_CWGR_CHDIV, twiClockSpeed):

        chdiv = getTWIClockDividerValue(twiClockSpeed.getValue())[1]
        twiSym_CWGR_CHDIV.setValue("TWI_CWGR_CLDIV", chdiv, 1)

def setClockDividerValue( twiSym_CWGR_CKDIV, twiClockSpeed):

        ckdiv = getTWIClockDividerValue(twiClockSpeed.getValue())[2]
        twiSym_CWGR_CKDIV.setValue("TWI_CWGR_CLDIV", ckdiv, 1)
                
	
'''********************************End of the file*************************'''
	
