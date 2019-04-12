"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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

from os.path import join
Log.writeInfoMessage( "Loading Interrupt Manager for " + Variables.get( "__PROCESSOR" ) )

################################################################################
#### Public Globals -- variables used in this module and accessible from other files
################################################################################
global getInterruptName

global interruptNamespace
global interruptSymbolEnable
global interruptSymbolHandler
global interruptSymbolHandlerLock

global interruptLastNameEnable 
global interruptLastNameHandler 
global interruptLastNameLock 

interruptNamespace =        "core"
interruptLastNameEnable =   "_INTERRUPT_ENABLE"
interruptLastNameHandler =  "_INTERRUPT_HANDLER"
interruptLastNameLock =     "_INTERRUPT_HANDLER_LOCK"

################################################################################
global showSharedVectorsInMenu
global numSharedVectors
global sharedVectors
global subVectorToSharedVector

showSharedVectorsInMenu = False
numSharedVectors = 0
sharedVectors = {}
subVectorToSharedVector = {}

################################################################################
#### Static Globals -- variables intended to be used inside this file only
################################################################################
# not currently public
global interruptsChildren
global interruptLastNameMapType
global interruptLastNameVector
global interruptLastNameSrcType
global interruptLastNamePriority

global aicMenuTitle
global aicRedirectionVisibility
global aicMapTypeVisibility
global aicPriorityOutputMode
global aicPriorityChoices
global aicSrcTypes
global aicMinPriorityName
global aicMaxPriorityName


interruptLastNameMapType =  "_INTERRUPT_MAP_TYPE"
interruptLastNameVector =   "_INTERRUPT_VECTOR"
interruptLastNameSrcType =  "_INTERRUPT_SRC_TYPE"
interruptLastNamePriority = "_INTERRUPT_PRIORITY"

interruptsChildren = ATDF.getNode( "/avr-tools-device-file/devices/device/interrupts" ).getChildren()

aicMenuTitle =              ""
aicRedirectionVisibility =  False
aicMapTypeVisibility =      False
aicPriorityOutputMode =     ""
aicPriorityChoices =        []
aicSrcTypes =               []
aicMinPriorityName =        ""
aicMaxPriorityName =        ""

aicCodeGenerationDependencies = []

neverSecureList =           []
alwaysSecureList =          []
programmedSecureList =      []
externalList =              []

################################################################################
#### Global Methods
################################################################################
def getInterruptName( interruptNode ):
    if "header:alternate-name" in interruptNode.getAttributeList():
        retval = interruptNode.getAttribute( "header:alternate-name" )
    else:
        retval = interruptNode.getAttribute( "name" )
    return( str( retval ) )

################################################################################
#### Local Methods
################################################################################
def getInterruptDescription( interruptNode ):
    if "header:alternate-caption" in interruptNode.getAttributeList():
        retval = interruptNode.getAttribute( "header:alternate-caption" )
    else:
        retval = interruptNode.getAttribute( "caption" )
    return( str( retval ) )


global getNameValueCaptionTuple
def getNameValueCaptionTuple( aGroupName, aTupleArray ):
    choiceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AIC\"]/value-group@[name=\"" + aGroupName + "\"]")
    if choiceNode:
        choiceValues = choiceNode.getChildren()
        del aTupleArray[:]
        for ii in range( 0, len( choiceValues ) ):
            aTupleArray.append( ( choiceValues[ ii ].getAttribute("name"), 
                                 choiceValues[ ii ].getAttribute("value"),
                                 choiceValues[ ii ].getAttribute("caption")
                                ) )


def getTupleNameContaining( aTupleArray, aString ):
    tupleName = ""
    if len( aTupleArray ):
        tupleName = aTupleArray[ 0 ][ 0 ]
        aString = aString.upper()
        for tuple in aTupleArray:
            if( aString in tuple[ 0 ].upper() ):
                tupleName = tuple[ 0 ]
                break
    return tupleName


def aicMapTypeRedirectionCallback( aicMapType, eventDictionary ):
    if( True == eventDictionary[ "value" ] ):
        # Mapping Secure to NonSecure
        if(     ("AlwaysSecure" == aicMapType.getDefaultValue())
            or  ("Secure" == aicMapType.getDefaultValue())
        ):
            aicMapType.setValue( "RedirectedToNonSecure", 1 )   # make change evident for user
    else:
        if(     ("AlwaysSecure" == aicMapType.getDefaultValue())
            or  ("Secure" == aicMapType.getDefaultValue())
        ):
            aicMapType.clearValue()                             # restore the default value


def priorityMapTypeCallback( aicVectorPriority, eventDictionary ):
    global aicMaxPriorityName
    if(     ("AlwaysSecure" == eventDictionary[ "value" ]) 
        or  ("Secure" == eventDictionary[ "value" ]) 
    ):
        aicVectorPriority.setSelectedKey( aicMaxPriorityName, 0 )
        aicVectorPriority.setVisible( False )
    else:
        aicVectorPriority.setVisible( True )


def aicCodeGenerationCallback( aicCodeGeneration, eventDictionary ):
    global interruptLastNameEnable 
    # Interrupt enables and map type determine the code generation to be done later
    secureCount = 0
    nonSecureCount = 0
    for interrupt in interruptsChildren:
        interruptName = getInterruptName( interrupt )
        component = aicCodeGeneration.getComponent()
        enableSymbol = component.getSymbolByID( interruptName + interruptLastNameEnable )
        if( enableSymbol.getValue() ):
            mapTypeSymbol = component.getSymbolByID( interruptName + interruptLastNameMapType )
            if(     ("NeverSecure" == mapTypeSymbol.value) 
                or  ("NonSecure" == mapTypeSymbol.value) 
                or  ("RedirectedToNonSecure" == mapTypeSymbol.value)
            ):
                nonSecureCount = nonSecureCount + 1
            else:
                secureCount = secureCount + 1
    if secureCount and nonSecureCount:
        aicCodeGeneration.setValue( "AICandSAIC", 0xFF )
    elif nonSecureCount:
        aicCodeGeneration.setValue( "AIC", 0xFF )
    elif secureCount:
        aicCodeGeneration.setValue( "SAIC", 0xFF )
    else:
        aicCodeGeneration.setValue( "NONE", 0xFF )


global aicVectorEnableCallback
def aicVectorEnableCallback( aicVectorEnable, eventDictionary ):
    global sharedVectors

    desiredValue = eventDictionary[ "value" ]
    interrupt = eventDictionary[ "id" ].replace( interruptLastNameLock, "" ).replace( interruptLastNameEnable, "" )
    aicVectorEnable.setReadOnly( True )
    if aicVectorEnable.getDefaultValue() == desiredValue:
        aicVectorEnable.clearValue()
    else:
        aicVectorEnable.setValue( desiredValue, 1 )
    aicVectorEnable.setReadOnly( False )

    sharedInterrupt = subVectorToSharedVector.get( interrupt )
    if( sharedInterrupt ):
        # check if any sibling is enabled
        component = aicVectorEnable.getComponent()
        desiredValue = False
        for elem in sharedVectors[ sharedInterrupt ]:
            vectorEnable = component.getSymbolByID( elem + interruptLastNameEnable )
            if vectorEnable and vectorEnable.getValue():
                desiredValue = True

        aicVectorEnable = component.getSymbolByID( sharedInterrupt + interruptLastNameEnable )
        aicVectorEnable.setValue( desiredValue, 1 )


def setupEnableAndHandler( component, anInterrupt, aicVectorEnable, aicVectorHandler ):
    global sharedVectors

    enableDependencies = []
    interruptName = getInterruptName( anInterrupt )
    moduleInstance = anInterrupt.getAttribute( "module-instance" ).split()
    sharedVectorMaxShares = len( moduleInstance )
    if 1 < sharedVectorMaxShares:
        aicVectorHandler.setReadOnly( True )
        aicVectorHandler.setValue( interruptName + "_SharedHandler", 0 )
        aicVectorHandler.setReadOnly( False )
        sharedVectors[ interruptName ] = moduleInstance
        aicVectorHandler.setVisible( False )

        for elem in moduleInstance:
            subVectorToSharedVector[ elem ] = interruptName
            subVectorEnable = component.createBooleanSymbol( elem + interruptLastNameEnable, aicVectorEnable )
            subVectorEnable.setLabel( "Enable " + elem )
            subVectorEnable.setDefaultValue( False )
            subVectorEnable.setDependencies( aicVectorEnableCallback, [elem + interruptLastNameLock] )
            enableDependencies.append( elem + interruptLastNameEnable )     # Parent enable depends on children

            subVectorHandlerLock = component.createBooleanSymbol( elem + interruptLastNameLock, subVectorEnable )
            subVectorHandlerLock.setDefaultValue( False )
            subVectorHandlerLock.setVisible( False )
            
            subVectorHandler = component.createStringSymbol( elem + interruptLastNameHandler, subVectorEnable )
            subVectorHandler.setLabel( elem + " Handler" )
            subVectorHandler.setDefaultValue( elem + "_Handler" )

    enableDependencies.append( interruptName + interruptLastNameLock )
    aicVectorEnable.setDependencies( aicVectorEnableCallback, enableDependencies )


def setupSharedVectorFtlSymbols( component, anInterrupt, aicVectorEnable ):
    global showSharedVectorsInMenu
    global numSharedVectors

    interruptName = getInterruptName( anInterrupt )
    moduleInstance = anInterrupt.getAttribute( "module-instance" ).split()
    numShares = len( moduleInstance )
    if 1 < numShares:
        numSharedVectors = numSharedVectors + 1
        # SHARED_VECTOR_N = "name", e.g. SHARED_VECTOR_1 = "SYSC"
        # Create a generic shared handler symbol with a value indicating the HANDLER 
        sharedVector = component.createStringSymbol( "SHARED_VECTOR_" + str( numSharedVectors - 1 ), aicVectorEnable )
        Database.clearSymbolValue( "core", interruptName + "SHARED_VECTOR_" + str( numSharedVectors - 1 ) )
        sharedVector.setDefaultValue( interruptName )
        sharedVector.setVisible( False )
        
        sharedVectorNumShares = component.createIntegerSymbol( interruptName + "_NUM_SHARES", sharedVector )
        sharedVectorNumShares.setMin( numShares )
        sharedVectorNumShares.setMax( numShares )
        Database.clearSymbolValue( "core", interruptName + "_NUM_SHARES" )
        sharedVectorNumShares.setValue( numShares, 0 )
        sharedVectorNumShares.setVisible( showSharedVectorsInMenu )
        # Create symbols for the shared handler names 
        # {SHARED_VECTOR_#}_HANDLER_#, e.g.
        #    SYSC_HANDLER_0 = "PMC"    ==> PMC_InterruptHandler
        #    SYSC_HANDLER_1 = "RSTC"   ==> RSTC_InterruptHandler
        #    SYSC_HANDLER_2 = "RTC"    ==> RTC_InterruptHandler
        ii = 0
        for elem in moduleInstance:
            shareName = component.createStringSymbol( interruptName + "_SHARE_" + str( ii ), aicVectorEnable )
            shareName.setDefaultValue( elem )
            shareName.setVisible( showSharedVectorsInMenu )
            ii = ii + 1


def formAicPyGlobalData( theProcessor, theCoreComponent ):
    global getNameValueCaptionTuple
    global aicMenuTitle
    global aicRedirectionVisibility
    global aicMapTypeVisibility
    global aicPriorityOutputMode
    global aicPriorityChoices
    global aicSrcTypes

    aicPriorityOutputMode = "Value"
    aicPrioritySymbolStem = "PRIORITY"
    getNameValueCaptionTuple( "AIC_SMR__" + aicPrioritySymbolStem, aicPriorityChoices )
    if not len( aicPriorityChoices ):
        aicPrioritySymbolStem = "PRIOR"
        getNameValueCaptionTuple( "AIC_SMR__" + aicPrioritySymbolStem, aicPriorityChoices )
        if not len( aicPriorityChoices ):
            # still not found in the atdf; so set some defaults
            aicPriorityChoices.append( ( "MINIMUM",    "0x0", "Minimum priority" ) )
            aicPriorityChoices.append( ( "VERY_LOW",   "0x1", "Very low priority" ) )
            aicPriorityChoices.append( ( "LOW",        "0x2", "Low priority" ) )
            aicPriorityChoices.append( ( "MEDIUM_LOW", "0x3", "Medium priority" ) )
            aicPriorityChoices.append( ( "MEDIUM_HIGH","0x4", "Medium high priority" ) )
            aicPriorityChoices.append( ( "HIGH",       "0x5", "High priority" ) )
            aicPriorityChoices.append( ( "VERY_HIGH",  "0x6", "Very high priority" ) )
            aicPriorityChoices.append( ( "MAXIMUM",    "0x7", "Maximum priority" ) )

    aicSmrPrioritySymbol = theCoreComponent.createStringSymbol( "AIC_SMR_PRIORITY_SYMBOL", None )
    aicSmrPrioritySymbol.setDefaultValue( "AIC_SMR_" + aicPrioritySymbolStem )
    aicSmrPrioritySymbol.setVisible( False )
    #
    aicSrcTypeSymbolStem =  "SRCTYPE"
    getNameValueCaptionTuple( "AIC_SMR__" + aicSrcTypeSymbolStem, aicSrcTypes )
    aicSmrSrcTypeSymbol = theCoreComponent.createStringSymbol( "AIC_SMR_SRCTYPE_SYMBOL", None )
    aicSmrSrcTypeSymbol.setDefaultValue( "AIC_SMR_" + aicSrcTypeSymbolStem )
    aicSmrSrcTypeSymbol.setVisible( False )
    #
    if "SAMA5" in theProcessor:
        aicMenuTitle =              "Interrupts (AIC/SAIC)"
        aicRedirectionVisibility =  True
        aicMapTypeVisibility =      True
        neverSecureList =           [ '49', '62' ]
        alwaysSecureList =          [  '0', '14', '15', '16', '18', '51', '61', '68', '69', '70' ]
        programmedSecureList =      []                                                                      # Todo create map interface to populate this list
        externalList =              [  '0', '49' ] # '2', '56', '57', '64', '65', '66', '67', '71', '72' have been subsumed data sheet peripheral table is misleading
    elif "SAM9X60" in theProcessor:
        aicMenuTitle =              "Interrupts"
        aicRedirectionVisibility =  False
        aicMapTypeVisibility =      False
        neverSecureList =           [ str( ii ) for ii in list( range( 0, 50 ) ) ]     # '0', '1',...'49'
        alwaysSecureList =          []
        programmedSecureList =      []
        externalList =              [  '0', '31' ]


################################################################################
#### Component
################################################################################
theProcessor = Variables.get("__PROCESSOR")
formAicPyGlobalData( theProcessor, coreComponent )

aicMinPriorityName = getTupleNameContaining( aicPriorityChoices, "min" )
aicMaxPriorityName = getTupleNameContaining( aicPriorityChoices, "max" )

aicMenu = coreComponent.createMenuSymbol( "AIC_MENU", cortexMenu )
aicMenu.setLabel( aicMenuTitle )
aicMenu.setDescription( "Configuration for AIC Initialization" )

### Symbol for interrupt redirection decision
aicRedirection = coreComponent.createBooleanSymbol( "SECURE_TO_NONSECURE_REDIRECTION", aicMenu )
aicRedirection.setLabel( "Secure to NonSecure Redirection" )
aicRedirection.setDefaultValue( True )
aicRedirection.setVisible( aicRedirectionVisibility )

aicVectorMax = coreComponent.createIntegerSymbol( "AIC_VECTOR_MAX", aicMenu )
aicVectorMax.setDefaultValue( Interrupt.getMaxInterruptID() )
aicVectorMax.setVisible( False )

aicVectorMax = coreComponent.createIntegerSymbol( "AIC_VECTOR_MIN", aicMenu )
aicVectorMax.setDefaultValue( Interrupt.getMinInterruptID() )
aicVectorMax.setVisible( False )

for interrupt in interruptsChildren:
    interruptName = getInterruptName( interrupt )
    aicNumber = str( interrupt.getAttribute( "index" ) )

    if aicNumber in neverSecureList:            # secure to nonSecure redirection will have no effect
        mapTypeDefault = "NeverSecure"
    elif aicNumber in alwaysSecureList:         # secure to nonSecure redirection will disable and hide these
        mapTypeDefault = "AlwaysSecure"
    elif aicNumber in programmedSecureList:     # secure to nonSecure redirection will change mapType to 'RedirectedToNonSecure' and set highest priority
        mapTypeDefault = "Secure"
    else: # programmed nonSecure                # secure to nonSecure redirection will have no effect
        mapTypeDefault = "NonSecure"
    # only for use by the aic ftl code
    aicInterruptFirstName = coreComponent.createStringSymbol( "AIC_FIRST_NAME_KEY" + aicNumber, None )
    aicInterruptFirstName.setDefaultValue( interruptName )
    aicInterruptFirstName.setVisible( False )
    ###
    aicVectorEnable = coreComponent.createBooleanSymbol( interruptName + interruptLastNameEnable, aicMenu )
    aicVectorEnable.setLabel( "Enable " + aicNumber + " -- " + getInterruptDescription( interrupt ) )
    aicVectorEnable.setDefaultValue( False )
    ###
    if (aicNumber in externalList):
        vectorPreCursor = "External Vector: "
    else:
        vectorPreCursor = "Internal Vector: "
    aicVectorSourceGUILabel = coreComponent.createCommentSymbol( interruptName + "_INTERRUPT_VECTOR_LABEL", aicVectorEnable )
    aicVectorSourceGUILabel.setLabel( vectorPreCursor + interruptName + "_IRQn" )
    # This is the same as aicVectorSourceGUILabel but creates a .var assignment accessible in plib_aic.c.ftl
    aicVectorSource = coreComponent.createStringSymbol( interruptName + interruptLastNameVector, aicVectorEnable )
    aicVectorSource.setDefaultValue( interruptName + "_IRQn" )
    aicVectorSource.setVisible( False )
    ###
    aicVectorLock = coreComponent.createBooleanSymbol( interruptName + interruptLastNameLock, aicVectorEnable )
    aicVectorLock.setDefaultValue( False )
    aicVectorLock.setVisible( False )

    aicVectorHandler = coreComponent.createStringSymbol( interruptName + interruptLastNameHandler, aicVectorEnable )
    aicVectorHandler.setLabel( "Handler" )
    aicVectorHandler.setDefaultValue( interruptName + "_Handler" )
    ###
    setupEnableAndHandler( coreComponent, interrupt, aicVectorEnable, aicVectorHandler )
    setupSharedVectorFtlSymbols( coreComponent, interrupt, aicVectorEnable )
    #
    aicMapType = coreComponent.createStringSymbol( interruptName + interruptLastNameMapType, aicVectorEnable )
    aicMapType.setLabel( "Map Type" )
    aicMapType.setDefaultValue( mapTypeDefault )
    aicMapType.setVisible( aicMapTypeVisibility )
    aicMapType.clearValue()
    aicMapType.setReadOnly( True )
    aicMapType.setDependencies( aicMapTypeRedirectionCallback, [ "SECURE_TO_NONSECURE_REDIRECTION" ] )
    
    aicVectorSourceType = coreComponent.createKeyValueSetSymbol( interruptName + interruptLastNameSrcType, aicVectorEnable )
    aicVectorSourceType.setLabel( "Source Type" )
    for tupleElem in aicSrcTypes:
        if (aicNumber not in externalList) and ("internal" not in tupleElem[ 2 ]):
            continue
        aicVectorSourceType.addKey( tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )

    aicVectorSourceType.setOutputMode( "Key" )
    aicVectorSourceType.setDisplayMode( "Description" )
    aicVectorSourceType.setDefaultValue( 0 )
    aicVectorSourceType.setSelectedKey( str( aicSrcTypes[ 0 ][ 0 ] ), 0 )

    aicVectorPriority = coreComponent.createKeyValueSetSymbol( interruptName + interruptLastNamePriority, aicVectorEnable )
    aicVectorPriority.setLabel( "Priority" )
    for tupleElem in aicPriorityChoices:
        aicVectorPriority.addKey( tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )
    aicVectorPriority.setOutputMode( aicPriorityOutputMode )
    aicVectorPriority.setDisplayMode( "Description" )
    aicVectorPriority.setDefaultValue( 0 )
    if( ("AlwaysSecure" == aicMapType.value) or ("Secure" == aicMapType.value) ):
        aicVectorPriority.setSelectedKey( aicMaxPriorityName, 0 )
        aicVectorPriority.setVisible( False )   # fiq interrupts do not have a priority, but if the get forced nonSecure we want a reasonable value
    else: 
        aicVectorPriority.setSelectedKey( aicMinPriorityName, 0 )
    aicVectorPriority.setDependencies( priorityMapTypeCallback, [ interruptName + interruptLastNameMapType ] )

    aicCodeGenerationDependencies.append( interruptName + interruptLastNameEnable )   # add to dependency list for code generation symbol
    aicCodeGenerationDependencies.append( interruptName + interruptLastNameMapType )  # add to dependency list for code generation symbol

###
aicNumSharedVectors = coreComponent.createIntegerSymbol( "NUM_SHARED_VECTORS", aicMenu )
aicNumSharedVectors.setMin( numSharedVectors )
aicNumSharedVectors.setMax( numSharedVectors )
Database.clearSymbolValue( "core", "NUM_SHARED_VECTORS" )
aicNumSharedVectors.setValue( numSharedVectors, 1 )
aicNumSharedVectors.setVisible( showSharedVectorsInMenu )
### Symbol for code generation decisions
aicCodeGeneration = coreComponent.createComboSymbol( "AIC_CODE_GENERATION", aicMenu, [ "NONE", "AIC", "SAIC", "AICandSAIC" ] )
aicCodeGeneration.setDefaultValue( "NONE" )
aicCodeGeneration.setDependencies( aicCodeGenerationCallback, aicCodeGenerationDependencies )
aicCodeGeneration.setVisible( False )
###
aicRedirection.setValue( True, 0 )  # stimulate a aicMapTypeRedirectionCallback() by setting the aicRedirection value
aicRedirection.setReadOnly( True )

############################################################################
#### Code Generation
############################################################################
configName = Variables.get( "__CONFIGURATION_NAME" )

aicSystemDefFile = coreComponent.createFileSymbol( "SYSTEM_AIC_DEFINITIONS", None )
aicSystemDefFile.setType( "STRING" )
aicSystemDefFile.setSourcePath( "../peripheral/aic_11051/templates/system/definitions.h.ftl" )
aicSystemDefFile.setOutputName( "core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES" )
aicSystemDefFile.setMarkup( True )

aicSystemInitFile = coreComponent.createFileSymbol( "SYS_AIC_INITIALIZE", None )
aicSystemInitFile.setType( "STRING" )
aicSystemInitFile.setSourcePath( "../peripheral/aic_11051/templates/system/initialization.c.ftl" )
aicSystemInitFile.setOutputName( "core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS" )
aicSystemInitFile.setMarkup( True )

aicSystemIntWeakHandleFile = coreComponent.createFileSymbol( "AIC_WEAK_HANDLERS", None )
aicSystemIntWeakHandleFile.setType( "STRING" )
aicSystemIntWeakHandleFile.setSourcePath( "../peripheral/aic_11051/templates/system/interrupt_weak_handlers.h.ftl" )
aicSystemIntWeakHandleFile.setOutputName( "core.LIST_SYSTEM_INTERRUPT_WEAK_HANDLERS" )
aicSystemIntWeakHandleFile.setMarkup( True )

aicSharedHandlerFile = coreComponent.createFileSymbol( "AIC_SHARED_HANDLERS", None )
aicSharedHandlerFile.setType( "STRING" )
aicSharedHandlerFile.setSourcePath( "../peripheral/aic_11051/templates/system/interrupt_shared_handlers.h.ftl" )
aicSharedHandlerFile.setOutputName( "core.LIST_SYSTEM_INTERRUPT_SHARED_HANDLERS" )
aicSharedHandlerFile.setMarkup( True )

aicSourceFile = coreComponent.createFileSymbol( "AIC_SOURCE", None )
aicSourceFile.setType( "SOURCE" )
aicSourceFile.setProjectPath( "config/" + configName + "/peripheral/aic/" )
aicSourceFile.setSourcePath( "../peripheral/aic_11051/templates/plib_aic.c.ftl" )
aicSourceFile.setDestPath( "/peripheral/aic/" )
aicSourceFile.setOutputName( "plib_aic.c" )
aicSourceFile.setMarkup( True )
aicSourceFile.setOverwrite( True )
aicSourceFile.setEnabled( True )

aicHeaderFile = coreComponent.createFileSymbol( "AIC_HEADER", None )
aicHeaderFile.setType( "HEADER" )
aicHeaderFile.setProjectPath( "config/" + configName + "/peripheral/aic/" )
aicHeaderFile.setSourcePath( "../peripheral/aic_11051/templates/plib_aic.h.ftl" )
aicHeaderFile.setDestPath( "/peripheral/aic/" )
aicHeaderFile.setOutputName( "plib_aic.h" )
aicHeaderFile.setMarkup( True )
aicHeaderFile.setOverwrite( True )
aicHeaderFile.setEnabled( True )
