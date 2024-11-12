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

def loadModule():

    coreArch = ATDF.getNode( "/avr-tools-device-file/devices/device" ).getAttribute( "architecture" )
    
    print("Load Module: Device Family Pack (DFP)")
    dfpComponent = Module.CreateComponent("dfp", "Device Family Pack (DFP)", "/Packs/", "config/dfp.py")

    # Avoid loading CMSIS for non-relevant processors
    if ("CORTEX" in coreArch):
        print("Load Module: CMSIS Pack")
        cmsisComponent = Module.CreateComponent("cmsis", "CMSIS Pack", "/Packs/", "config/cmsis.py")

    print("Load Module: CSP System")
    coreComponent = Module.CreateSharedComponent("core", "System", "/", "config/core.py")

    # initiate stdio
    stdioComponent = Module.CreateComponent("stdio", "STDIO", "/Tools/", "../arch/stdio/config/stdio.py")
    stdioComponent.addDependency("UART","UART",False,True)
    stdioComponent.addCapability("STDIO", "STDIO", True)

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        # initiate stdio
        stdioComponent = Module.CreateComponent("stdio_s", "Secure STDIO", "/Tools/", "../arch/stdio/config/stdio_secure.py")
        stdioComponent.addDependency("UART","UART",False,True)

    # load device specific peripherals
    d = dict(locals(), **globals())
    execfile(Module.getPath() + "../../csp/peripheral/config/peripheral.py", d, d)
