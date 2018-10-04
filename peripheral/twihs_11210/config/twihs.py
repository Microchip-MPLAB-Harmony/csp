"""*****************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

global twihsInstanceName

def instantiateComponent(twihsComponent):

    global twihsInstanceName

    twihsInstanceName = twihsComponent.createStringSymbol("TWIHS_INSTANCE_NAME", None)
    twihsInstanceName.setVisible(False)
    twihsInstanceName.setDefaultValue(twihsComponent.getID().upper())
    
    print("Running " + twihsInstanceName.getValue())

    #main menu
    twihsMenu = twihsComponent.createMenuSymbol("TWIHS_MENU_MAIN", None)
    
    twihsMenu.setLabel("Hardware Settings ")

    #operation mode
    opModeValues = ["MASTER"]
    
    twihsOpMode = twihsComponent.createComboSymbol("TWIHS_OPMODE", twihsMenu, opModeValues)
    
    twihsOpMode.setLabel("TWIHS Operation Mode")
    twihsOpMode.setDefaultValue("MASTER")
    
    #Clock speed
    twihsSymClockSpeed = twihsComponent.createIntegerSymbol("I2C_CLOCK_SPEED", twihsMenu)

    twihsSymClockSpeed.setLabel("Clock Speed")
    twihsSymClockSpeed.setDefaultValue(400000)
    twihsSymClockSpeed.setMax(400000)

    cldiv, chdiv, ckdiv = getTWIHSClockDividerValue(twihsSymClockSpeed.getValue())
    
    #Clock Divider
    twihsSymDivider = twihsComponent.createStringSymbol("TWIHS_DIVIDER", twihsMenu)
    
    twihsSymDivider.setVisible(False)
    twihsSymDivider.setDependencies(setClockDividerValue, ["I2C_CLOCK_SPEED", "core." + twihsInstanceName.getValue() + "_CLOCK_FREQUENCY"])
    
    #CLDIV
    twihsSym_CWGR_CLDIV = twihsComponent.createIntegerSymbol("TWIHS_CWGR_CLDIV", twihsMenu)
    
    twihsSym_CWGR_CLDIV.setVisible(False)
    twihsSym_CWGR_CLDIV.setValue(cldiv, 1)
    
    #CHDIV
    twihsSym_CWGR_CHDIV = twihsComponent.createIntegerSymbol("TWIHS_CWGR_CHDIV", twihsMenu)
    
    twihsSym_CWGR_CHDIV.setVisible(False)
    twihsSym_CWGR_CHDIV.setValue(chdiv, 1)
    
    #CKDIV
    twihsSym_CWGR_CKDIV = twihsComponent.createIntegerSymbol("TWIHS_CWGR_CKDIV", twihsMenu)
    
    twihsSym_CWGR_CKDIV.setVisible(False)
    twihsSym_CWGR_CKDIV.setValue(ckdiv, 1)
    
    # Initialize peripheral clock
    Database.clearSymbolValue("core", twihsInstanceName.getValue()+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", twihsInstanceName.getValue()+"_CLOCK_ENABLE", True, 1)
    
    # Initialize peripheral Interrupt
    Database.clearSymbolValue("core", twihsInstanceName.getValue() + "INTERRUPT_ENABLE")
    Database.setSymbolValue("core", twihsInstanceName.getValue() + "_INTERRUPT_ENABLE", True, 1)
    
    # Set Interrupt Handler Name
    Database.clearSymbolValue("core", twihsInstanceName.getValue() + "_INTERRUPT_HANDLER")
    Database.setSymbolValue("core", twihsInstanceName.getValue() + "_INTERRUPT_HANDLER", twihsInstanceName.getValue() + "_InterruptHandler", 1)

    # Set Interrupt Handler Lock
    Database.clearSymbolValue("core", twihsInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK")
    Database.setSymbolValue("core", twihsInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK", True, 1)

    # Master Clock Frequency
    twihsSymMasterClkFreq = twihsComponent.createStringSymbol("TWIHS_CLK_SRC_FREQ", twihsMenu)
    twihsSymMasterClkFreq.setVisible(False)
    twihsSymMasterClkFreq.setDefaultValue(str(Database.getSymbolValue("core", twihsInstanceName.getValue() + "_CLOCK_FREQUENCY")))
    twihsSymMasterClkFreq.setDependencies(setClockSourceFreq, ["core."+ twihsInstanceName.getValue() + "_CLOCK_FREQUENCY"])
    
    # Warning for change in Clock Enable Symbol
    twihsSymClkEnComment = twihsComponent.createCommentSymbol("TWIHS_CLK_EN_COMMENT", twihsMenu)
    twihsSymClkEnComment.setVisible(False)
    twihsSymClkEnComment.setLabel("Warning!!! TWIHS Peripheral Clock is Disabled in Clock Manager")
    twihsSymClkEnComment.setDependencies(setEnCommentVisibility, ["core."+twihsInstanceName.getValue()+"_CLOCK_ENABLE"])
    
    # Warning for change in Interrupt Enable Symbol
    twihsSymIntEnComment = twihsComponent.createCommentSymbol("TWIHS_INT_EN_COMMENT", twihsMenu)
    twihsSymIntEnComment.setVisible(False)
    twihsSymIntEnComment.setLabel("Warning!!! TWIHS Interrupt is Disabled in Interrupt Manager")
    twihsSymIntEnComment.setDependencies(setEnCommentVisibility, ["core."+twihsInstanceName.getValue()+"_INTERRUPT_ENABLE_UPDATE"])

    #TWIHS API Prefix
    twihsSymAPIPrefix = twihsComponent.createStringSymbol("I2C_PLIB_API_PREFIX", twihsMenu)
    twihsSymAPIPrefix.setDefaultValue(twihsInstanceName.getValue())
    twihsSymAPIPrefix.setVisible(False)

    REG_MODULE_TWIHS = Register.getRegisterModule("TWIHS")
    
    configName = Variables.get("__CONFIGURATION_NAME")
    
    #Master Header
    twihsMasterHeaderFile = twihsComponent.createFileSymbol("TWIHS_FILE_MASTER_HEADER", None)
    
    twihsMasterHeaderFile.setSourcePath("../peripheral/twihs_" + REG_MODULE_TWIHS.getID() + "/plib_twihs_master.h")
    twihsMasterHeaderFile.setOutputName("plib_twihs_master.h")
    twihsMasterHeaderFile.setDestPath("/peripheral/twihs/")
    twihsMasterHeaderFile.setProjectPath("config/" + configName + "/peripheral/twihs/")
    twihsMasterHeaderFile.setType("HEADER")

    #Source File
    twihsMainSourceFile = twihsComponent.createFileSymbol("TWIHS_FILE_SRC_MAIN", None)
    
    twihsMainSourceFile.setSourcePath("../peripheral/twihs_" + REG_MODULE_TWIHS.getID() + "/templates/plib_twihs.c.ftl")
    twihsMainSourceFile.setOutputName("plib_"+twihsInstanceName.getValue().lower()+".c")
    twihsMainSourceFile.setDestPath("/peripheral/twihs/")
    twihsMainSourceFile.setProjectPath("config/" + configName + "/peripheral/twihs/")
    twihsMainSourceFile.setType("SOURCE")
    twihsMainSourceFile.setMarkup(True)
    
    #Instance Header File
    twihsInstHeaderFile = twihsComponent.createFileSymbol("TWIHS_FILE_MAIN_HEADER", None)
    
    twihsInstHeaderFile.setSourcePath("../peripheral/twihs_" + REG_MODULE_TWIHS.getID() + "/templates/plib_twihs.h.ftl")
    twihsInstHeaderFile.setOutputName("plib_"+twihsInstanceName.getValue().lower()+".h")
    twihsInstHeaderFile.setDestPath("/peripheral/twihs/")
    twihsInstHeaderFile.setProjectPath("config/" + configName + "/peripheral/twihs/")
    twihsInstHeaderFile.setType("HEADER")
    twihsInstHeaderFile.setMarkup(True)
    
    #TWIHS Initialize 
    twihsSystemInitFile = twihsComponent.createFileSymbol("TWIHS_FILE_SYS_INIT", None)
    twihsSystemInitFile.setType("STRING")
    twihsSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    twihsSystemInitFile.setSourcePath("../peripheral/twihs_" + REG_MODULE_TWIHS.getID() + "/templates/system/system_initialize.c.ftl")
    twihsSystemInitFile.setMarkup(True)

    #TWIHS definitions header
    twihsSystemDefFile = twihsComponent.createFileSymbol("TWIHS_FILE_SYS_DEF", None)
    
    twihsSystemDefFile.setType("STRING")
    twihsSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    twihsSystemDefFile.setSourcePath("../peripheral/twihs_" + REG_MODULE_TWIHS.getID() + "/templates/system/system_definitions.h.ftl")
    twihsSystemDefFile.setMarkup(True)
    
def getMasterClockFreq():
    return int(Database.getSymbolValue("core", twihsInstanceName.getValue() + "_CLOCK_FREQUENCY"))
        
def getTWIHSClkSpeed():
    global num
    return Database.getSymbolValue(twihsInstanceName.getValue().lower(), "I2C_CLOCK_SPEED")

def getTWIHSLowLevelTimeLimit( ):
    return 384000

def getTWIHSClockDividerMaxValue( ):
    return 255

def getTWIHSClockDividerMinValue( ):
    return 7

def getTWIHSClockDividerValue( twihsClkSpeed ):

    cldiv = 0 
    chdiv = 0
    ckdiv = 0

    masterClockFreq = getMasterClockFreq( )

    if twihsClkSpeed > getTWIHSLowLevelTimeLimit():
        cldiv = masterClockFreq // ( getTWIHSLowLevelTimeLimit() * 2) - 3
        chdiv = masterClockFreq // ((twihsClkSpeed + (twihsClkSpeed - getTWIHSLowLevelTimeLimit())) * 2 ) - 3

        while cldiv > getTWIHSClockDividerMaxValue() and ckdiv < getTWIHSClockDividerMinValue():
            ckdiv += 1
            cldiv //= 2

        while chdiv > getTWIHSClockDividerMaxValue() and ckdiv < getTWIHSClockDividerMinValue():
            ckdiv += 1
            chdiv //= 2
    else:
        cldiv = masterClockFreq / ( twihsClkSpeed * 2 ) - 3

        while cldiv > getTWIHSClockDividerMaxValue() and ckdiv < getTWIHSClockDividerMinValue():
            ckdiv += 1
            cldiv //= 2

        chdiv = cldiv

    return cldiv, chdiv, ckdiv

def setClockDividerValue( twihsSymDivider, event):

    global twihsInstanceName
    cldiv, chdiv, ckdiv = getTWIHSClockDividerValue( getTWIHSClkSpeed( ) )

    # set CLDIV Value
    Database.setSymbolValue(twihsInstanceName.getValue().lower(), "TWIHS_CWGR_CLDIV", cldiv, 1)

    # set CHDIV Value
    Database.setSymbolValue(twihsInstanceName.getValue().lower(), "TWIHS_CWGR_CHDIV", chdiv, 1)

    # set CKDIV Value
    Database.setSymbolValue(twihsInstanceName.getValue().lower(), "TWIHS_CWGR_CKDIV", ckdiv, 1)

def setEnCommentVisibility( twihsSymComment, event ):
    twihsSymComment.setVisible(event["value"])

def setClockSourceFreq( twihsSymClockFreq, event ):
    masterClockFreq = str(Database.getSymbolValue("core", twihsInstanceName.getValue() + "_CLOCK_FREQUENCY"))
    twihsSymClockFreq.setValue(masterClockFreq, 1)

'''********************************End of the file*************************'''
    
