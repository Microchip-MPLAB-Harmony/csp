# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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

global family
node = ATDF.getNode("/avr-tools-device-file/devices")
family = node.getChildren()[0].getAttribute("family")

trustZoneMenu = coreComponent.createMenuSymbol("TRUSTZONE_MENU", devCfgMenu)
trustZoneMenu.setLabel('Arm\xae TrustZone\xae for Armv8-M') #Arm® TrustZone® for Armv8-M

memoryMenu = coreComponent.createMenuSymbol("MEMORY_MENU", devCfgMenu)
memoryMenu.setLabel("Memory Configuration")

secSystemDefinitionsHeadersList =      coreComponent.createListSymbol( "LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES",       None )
secsystemIntHandlerdeclsList =         coreComponent.createListSymbol("LIST_SYSTEM_INTERRUPT_SECURE_HANDLER_DECLS",       None)
secsystemIntVectorsMultipleHandlesList =   coreComponent.createListSymbol( "LIST_SYSTEM_INTERRUPT_SECURE_MULTIPLE_HANDLERS",  None )
secsystemIntVectorsWeakHandlesList =       coreComponent.createListSymbol( "LIST_SYSTEM_INTERRUPT_SECURE_WEAK_HANDLERS",      None )
secsystemIntVectorsHandlesList =           coreComponent.createListSymbol( "LIST_SYSTEM_INTERRUPT_SECURE_HANDLERS",           None )
secSystemInitStaticFuncList =          coreComponent.createListSymbol( "LIST_SYSTEM_SECURE_INIT_C_INITIALIZER_STATIC_FUNCTIONS",  None )

secsystemInitFuseList =        coreComponent.createListSymbol( "LIST_SYSTEM_SECURE_INIT_C_CONFIG_BITS_INITIALIZATION",    None )
secsystemInitStart1List =      coreComponent.createListSymbol( "LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_START1",         None )
secsystemInitStartList =       coreComponent.createListSymbol( "LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_START",          None )
secsystemInitCoreList =        coreComponent.createListSymbol( "LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_CORE",           None )
secsystemInitPeripheral1List = coreComponent.createListSymbol( "LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS1",   None )
secsystemInitCore1List =       coreComponent.createListSymbol( "LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_CORE1",          None )
secsystemInitPeripheralList =  coreComponent.createListSymbol( "LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS",    None )
secsystemInterruptEnableList = coreComponent.createListSymbol( "LIST_SYSTEM_SECURE_INIT_INTERRUPTS",    None )

BspSecureHeaderIncludeList   = coreComponent.createListSymbol( "LIST_BSP_MACRO_SECURE_INCLUDES",    None )
BspSecureInitList            = coreComponent.createListSymbol( "LIST_BSP_SECURE_INITIALIZATION",    None )

if family == "PIC32CK":
    execfile(Variables.get("__CORE_DIR") + "/config/trustZone/trustZone_pic32ck.py")
else:
    execfile(Variables.get("__CORE_DIR") + "/config/trustZone/trustZone_saml11_pic32cm.py")

coreComponent.addPlugin("/config/trustZone/plugin/trustzone_manager.jar")