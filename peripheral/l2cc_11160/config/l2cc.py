global update_file_generation_enabled
def update_file_generation_enabled(comp, event):
    comp.setEnabled(event["value"])


global update_component_visability
def update_component_visability(comp, event):
    comp.setVisible(event["value"])

Log.writeInfoMessage("Loading L2CC for " + Variables.get("__PROCESSOR"))

l2cc_menu = coreComponent.createMenuSymbol("L2CC_MENU", None)
l2cc_menu.setLabel("L2 Cache (L2CC)")
l2cc_menu.setDescription("Configuration for Level 2 cache controller")


l2cc_cr_l2cen = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                getRegister("L2CC_CR").getBitfield("L2CEN")
l2cc_enable = coreComponent.createBooleanSymbol("L2CC_ENABLE", l2cc_menu)
l2cc_enable.setLabel(l2cc_cr_l2cen.getDescription())
l2cc_enable.setDefaultValue(False)

l2cc_acr_hpso = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                getRegister("L2CC_ACR").getBitfield("HPSO")
l2cc_hpso = coreComponent.createBooleanSymbol("L2CC_ACR_HPSO", l2cc_menu)
l2cc_hpso.setLabel(l2cc_acr_hpso.getDescription())
l2cc_hpso.setDefaultValue(False)
l2cc_hpso.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_hpso.setVisible(False)

l2cc_acr_sbdle = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                 getRegister("L2CC_ACR").getBitfield("SBDLE")
l2cc_sbdle = coreComponent.createBooleanSymbol("L2CC_ACR_SBDLE", l2cc_menu)
l2cc_sbdle.setLabel(l2cc_acr_sbdle.getDescription())
l2cc_sbdle.setDefaultValue(False)
l2cc_sbdle.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_sbdle.setVisible(False)

l2cc_acr_excc = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                getRegister("L2CC_ACR").getBitfield("EXCC")
l2cc_excc = coreComponent.createBooleanSymbol("L2CC_ACR_EXCC", l2cc_menu)
l2cc_excc.setLabel(l2cc_acr_excc.getDescription())
l2cc_excc.setDefaultValue(False)
l2cc_excc.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_excc.setVisible(False)

l2cc_acr_saie = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                getRegister("L2CC_ACR").getBitfield("SAIE")
l2cc_saie = coreComponent.createBooleanSymbol("L2CC_ACR_SAIE", l2cc_menu)
l2cc_saie.setLabel(l2cc_acr_saie.getDescription())
l2cc_saie.setDefaultValue(False)
l2cc_saie.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_saie.setVisible(False)

l2cc_acr_emben = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                 getRegister("L2CC_ACR").getBitfield("EMBEN")
l2cc_emben = coreComponent.createBooleanSymbol("L2CC_ACR_EMBEN", l2cc_menu)
l2cc_emben.setLabel(l2cc_acr_emben.getDescription())
l2cc_emben.setDefaultValue(False)
l2cc_emben.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_emben.setVisible(False)

l2cc_acr_pen = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
               getRegister("L2CC_ACR").getBitfield("PEN")
l2cc_pen = coreComponent.createBooleanSymbol("L2CC_ACR_PEN", l2cc_menu)
l2cc_pen.setLabel(l2cc_acr_pen.getDescription())
l2cc_pen.setDefaultValue(False)
l2cc_pen.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_pen.setVisible(False)

l2cc_acr_saoen = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                 getRegister("L2CC_ACR").getBitfield("SAOEN")
l2cc_saoen = coreComponent.createBooleanSymbol("L2CC_ACR_SAOEN", l2cc_menu)
l2cc_saoen.setLabel(l2cc_acr_saoen.getDescription())
l2cc_saoen.setDefaultValue(False)
l2cc_saoen.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_saoen.setVisible(False)

l2cc_acr_fwa = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
               getRegister("L2CC_ACR").getBitfield("FWA")
l2cc_fwa = coreComponent.createKeyValueSetSymbol("L2CC_ACR_FWA", l2cc_menu)
l2cc_fwa.setLabel(l2cc_acr_fwa.getDescription())
#TODO add these to atdf and get them from there
l2cc_fwa.addKey("0", "0", "The L2 Cache controller uses AWCACHE attributes for WA")
l2cc_fwa.addKey("1", "1", "User forces no allocate, WA bit must be set to 0.")
l2cc_fwa.addKey("2", "2", "User overrides AWCACHE attributes, WA bit must be set to 1")
l2cc_fwa.setSelectedKey("0", 1)
l2cc_fwa.setOutputMode("Value")
l2cc_fwa.setDisplayMode("Description")
l2cc_fwa.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_fwa.setVisible(False)

l2cc_acr_crpol = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                 getRegister("L2CC_ACR").getBitfield("CRPOL")
l2cc_crpol = coreComponent.createBooleanSymbol("L2CC_ACR_CRPOL", l2cc_menu)
l2cc_crpol.setLabel(l2cc_acr_crpol.getDescription())
l2cc_crpol.setDefaultValue(True)
l2cc_crpol.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_crpol.setVisible(False)

l2cc_acr_nslen = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                 getRegister("L2CC_ACR").getBitfield("NSLEN")
l2cc_nslen = coreComponent.createBooleanSymbol("L2CC_ACR_NSLEN", l2cc_menu)
l2cc_nslen.setLabel(l2cc_acr_nslen.getDescription())
l2cc_nslen.setDefaultValue(False)
l2cc_nslen.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_nslen.setVisible(False)

l2cc_acr_nsiac = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                 getRegister("L2CC_ACR").getBitfield("NSIAC")
l2cc_nsiac = coreComponent.createBooleanSymbol("L2CC_ACR_NSIAC", l2cc_menu)
l2cc_nsiac.setLabel(l2cc_acr_nsiac.getDescription())
l2cc_nsiac.setDefaultValue(False)
l2cc_nsiac.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_nsiac.setVisible(False)

l2cc_acr_dpen = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                getRegister("L2CC_ACR").getBitfield("DPEN")
l2cc_dpen = coreComponent.createBooleanSymbol("L2CC_ACR_DPEN", l2cc_menu)
l2cc_dpen.setLabel(l2cc_acr_dpen.getDescription())
l2cc_dpen.setDefaultValue(False)
l2cc_dpen.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_dpen.setVisible(False)

l2cc_acr_ipen = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                getRegister("L2CC_ACR").getBitfield("IPEN")
l2cc_ipen = coreComponent.createBooleanSymbol("L2CC_ACR_IPEN", l2cc_menu)
l2cc_ipen.setLabel(l2cc_acr_ipen.getDescription())
l2cc_ipen.setDefaultValue(False)
l2cc_ipen.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_ipen.setVisible(False)

l2cc_trcr = coreComponent.createBooleanSymbol("L2CC_TRCR", l2cc_menu)
l2cc_trcr.setLabel("Configure Ram Tag Latency")
l2cc_trcr.setDefaultValue(False)
l2cc_trcr.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_trcr.setVisible(False)

l2cc_trcr_tsetlat = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                getRegister("L2CC_TRCR").getBitfield("TSETLAT")
l2cc_tsetlat = coreComponent.createIntegerSymbol("L2CC_TRCR_TSETLAT", l2cc_trcr)
l2cc_tsetlat.setLabel(l2cc_trcr_tsetlat.getDescription())
l2cc_tsetlat.setDependencies(update_component_visability, ["L2CC_TRCR"])
l2cc_tsetlat.setVisible(False)
l2cc_tsetlat.setMin(0)
l2cc_tsetlat.setMax(7)

l2cc_trcr_trdlat = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                getRegister("L2CC_TRCR").getBitfield("TRDLAT")
l2cc_trdlat = coreComponent.createIntegerSymbol("L2CC_TRCR_TRDLAT", l2cc_trcr)
l2cc_trdlat.setLabel(l2cc_trcr_trdlat.getDescription())
l2cc_trdlat.setDependencies(update_component_visability, ["L2CC_TRCR"])
l2cc_trdlat.setVisible(False)
l2cc_trdlat.setMin(0)
l2cc_trdlat.setMax(7)

l2cc_trcr_twrlat = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                getRegister("L2CC_TRCR").getBitfield("TWRLAT")
l2cc_trdlat = coreComponent.createIntegerSymbol("L2CC_TRCR_TWRLAT", l2cc_trcr)
l2cc_trdlat.setLabel(l2cc_trcr_twrlat.getDescription())
l2cc_trdlat.setDependencies(update_component_visability, ["L2CC_TRCR"])
l2cc_trdlat.setVisible(False)
l2cc_trdlat.setMin(0)
l2cc_trdlat.setMax(7)

l2cc_drcr = coreComponent.createBooleanSymbol("L2CC_DRCR", l2cc_menu)
l2cc_drcr.setLabel("Configure Data Ram Latency")
l2cc_drcr.setDefaultValue(False)
l2cc_drcr.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_drcr.setVisible(False)

l2cc_drcr_dsetlat = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                getRegister("L2CC_DRCR").getBitfield("DSETLAT")
l2cc_dsetlat = coreComponent.createIntegerSymbol("L2CC_DRCR_DSETLAT", l2cc_drcr)
l2cc_dsetlat.setLabel(l2cc_drcr_dsetlat.getDescription())
l2cc_dsetlat.setDependencies(update_component_visability, ["L2CC_DRCR"])
l2cc_dsetlat.setVisible(False)
l2cc_dsetlat.setMin(0)
l2cc_dsetlat.setMax(7)

l2cc_drcr_drdlat = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                getRegister("L2CC_DRCR").getBitfield("DRDLAT")
l2cc_drdlat = coreComponent.createIntegerSymbol("L2CC_DRCR_DRDLAT", l2cc_drcr)
l2cc_drdlat.setLabel(l2cc_drcr_drdlat.getDescription())
l2cc_drdlat.setDependencies(update_component_visability, ["L2CC_DRCR"])
l2cc_drdlat.setVisible(False)
l2cc_drdlat.setMin(0)
l2cc_drdlat.setMax(7)

l2cc_drcr_dwrlat = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                getRegister("L2CC_DRCR").getBitfield("DWRLAT")
l2cc_drdlat = coreComponent.createIntegerSymbol("L2CC_DRCR_DWRLAT", l2cc_drcr)
l2cc_drdlat.setLabel(l2cc_drcr_dwrlat.getDescription())
l2cc_drdlat.setDependencies(update_component_visability, ["L2CC_DRCR"])
l2cc_drdlat.setVisible(False)
l2cc_drdlat.setMin(0)
l2cc_drdlat.setMax(7)

l2cc_ecr_evcen = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                getRegister("L2CC_ECR").getBitfield("EVCEN")
l2cc_evcen = coreComponent.createBooleanSymbol("L2CC_ECR_EVCEN", l2cc_menu)
l2cc_evcen.setLabel(l2cc_ecr_evcen.getDescription())
l2cc_evcen.setDefaultValue(False)
l2cc_evcen.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_evcen.setVisible(False)

cmt = coreComponent.createCommentSymbol("L2CC_ECFGR0_CMT", l2cc_evcen)
cmt.setLabel("Event Counter 0 configuration")
cmt.setDependencies(update_component_visability, ["L2CC_ECR_EVCEN"])
cmt.setVisible(False)

l2cc_ecfgr0_eigen = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                getRegister("L2CC_ECFGR0").getBitfield("EIGEN")
l2cc_ecfgr0_eigen_values = Register.getRegisterModule("L2CC").\
                           getValueGroup(l2cc_ecfgr0_eigen.getValueGroupName())
l2cc_eigen0 = coreComponent.createKeyValueSetSymbol("L2CC_ECFGR0_EIGEN", l2cc_evcen)
l2cc_eigen0.setLabel(l2cc_ecfgr0_eigen.getDescription())
l2cc_eigen0.setDependencies(update_component_visability, ["L2CC_ECR_EVCEN"])
l2cc_eigen0.setVisible(False)
for name in l2cc_ecfgr0_eigen_values.getValueNames():
    value = l2cc_ecfgr0_eigen_values.getValue(name)
    l2cc_eigen0.addKey(value.getName(), value.getValue(), value.getDescription())
l2cc_eigen0.setOutputMode("Value")
l2cc_eigen0.setDisplayMode("Description")
l2cc_eigen0.setSelectedKey("INT_DIS", 1)

l2cc_ecfgr0_esrc = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                getRegister("L2CC_ECFGR0").getBitfield("ESRC")
l2cc_ecfgr0_esrc_values = Register.getRegisterModule("L2CC").\
                           getValueGroup(l2cc_ecfgr0_esrc.getValueGroupName())
l2cc_esrc = coreComponent.createKeyValueSetSymbol("L2CC_ECFGR0_ESRC", l2cc_evcen)
l2cc_esrc.setLabel(l2cc_ecfgr0_esrc.getDescription())
l2cc_esrc.setDependencies(update_component_visability, ["L2CC_ECR_EVCEN"])
l2cc_esrc.setVisible(False)
for name in l2cc_ecfgr0_esrc_values.getValueNames():
    value = l2cc_ecfgr0_esrc_values.getValue(name)
    l2cc_esrc.addKey(value.getName(), value.getValue(), value.getDescription())
l2cc_esrc.setOutputMode("Value")
l2cc_esrc.setDisplayMode("Description")
l2cc_esrc.setSelectedKey("CNT_DIS", 1)

cmt = coreComponent.createCommentSymbol("L2CC_ECFGR1_CMT", l2cc_evcen)
cmt.setLabel("Event Counter 1 configuration")
cmt.setDependencies(update_component_visability, ["L2CC_ECR_EVCEN"])
cmt.setVisible(False)

l2cc_ecfgr1_eigen = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                getRegister("L2CC_ECFGR1").getBitfield("EIGEN")
l2cc_ecfgr1_eigen_values = Register.getRegisterModule("L2CC").\
                           getValueGroup(l2cc_ecfgr1_eigen.getValueGroupName())
l2cc_eigen1 = coreComponent.createKeyValueSetSymbol("L2CC_ECFGR1_EIGEN", l2cc_evcen)
l2cc_eigen1.setLabel(l2cc_ecfgr1_eigen.getDescription())
l2cc_eigen1.setDependencies(update_component_visability, ["L2CC_ECR_EVCEN"])
l2cc_eigen1.setVisible(False)
for name in l2cc_ecfgr1_eigen_values.getValueNames():
    value = l2cc_ecfgr1_eigen_values.getValue(name)
    l2cc_eigen1.addKey(value.getName(), value.getValue(), value.getDescription())
l2cc_eigen1.setOutputMode("Value")
l2cc_eigen1.setDisplayMode("Description")
l2cc_eigen1.setSelectedKey("INT_DIS", 1)

l2cc_ecfgr1_esrc = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                getRegister("L2CC_ECFGR1").getBitfield("ESRC")
l2cc_ecfgr1_esrc_values = Register.getRegisterModule("L2CC").\
                           getValueGroup(l2cc_ecfgr1_esrc.getValueGroupName())
l2cc_esrc = coreComponent.createKeyValueSetSymbol("L2CC_ECFGR1_ESRC", l2cc_evcen)
l2cc_esrc.setLabel(l2cc_ecfgr1_esrc.getDescription())
l2cc_esrc.setDependencies(update_component_visability, ["L2CC_ECR_EVCEN"])
l2cc_esrc.setVisible(False)
for name in l2cc_ecfgr1_esrc_values.getValueNames():
    value = l2cc_ecfgr1_esrc_values.getValue(name)
    l2cc_esrc.addKey(value.getName(), value.getValue(), value.getDescription())
l2cc_esrc.setOutputMode("Value")
l2cc_esrc.setDisplayMode("Description")
l2cc_esrc.setSelectedKey("CNT_DIS", 1)

l2cc_dcr_dcl = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                 getRegister("L2CC_DCR").getBitfield("DCL")
l2cc_dcl = coreComponent.createBooleanSymbol("L2CC_DCR_DCL", l2cc_menu)
l2cc_dcl.setLabel(l2cc_dcr_dcl.getDescription())
l2cc_dcl.setDefaultValue(False)
l2cc_dcl.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_dcl.setVisible(False)

l2cc_dcr_dwb = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                 getRegister("L2CC_DCR").getBitfield("DWB")
l2cc_dwb = coreComponent.createBooleanSymbol("L2CC_DCR_DWB", l2cc_menu)
l2cc_dwb.setLabel(l2cc_dcr_dwb.getDescription())
l2cc_dwb.setDefaultValue(False)
l2cc_dwb.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_dwb.setVisible(False)

l2cc_pcr_offset = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                 getRegister("L2CC_PCR").getBitfield("OFFSET")
l2cc_offset = coreComponent.createComboSymbol("L2CC_PCR_OFFSET", l2cc_menu,\
        ["0", "1", "2", "3", "4", "5", "6", "7", "15", "23", "31"])
l2cc_offset.setLabel(l2cc_pcr_offset.getDescription())
l2cc_offset.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_offset.setVisible(False)

l2cc_pcr_nsiden = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                 getRegister("L2CC_PCR").getBitfield("NSIDEN")
l2cc_nsiden = coreComponent.createBooleanSymbol("L2CC_PCR_NSIDEN", l2cc_menu)
l2cc_nsiden.setLabel(l2cc_pcr_nsiden.getDescription())
l2cc_nsiden.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_nsiden.setVisible(False)

l2cc_pcr_idlen = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                 getRegister("L2CC_PCR").getBitfield("IDLEN")
l2cc_idlen = coreComponent.createBooleanSymbol("L2CC_PCR_IDLEN", l2cc_menu)
l2cc_idlen.setLabel(l2cc_pcr_idlen.getDescription())
l2cc_idlen.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_idlen.setVisible(False)

l2cc_pcr_pden = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                 getRegister("L2CC_PCR").getBitfield("PDEN")
l2cc_pden = coreComponent.createBooleanSymbol("L2CC_PCR_PDEN", l2cc_menu)
l2cc_pden.setLabel(l2cc_pcr_pden.getDescription())
l2cc_pden.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_pden.setVisible(False)

l2cc_pcr_dlfwrdis = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                 getRegister("L2CC_PCR").getBitfield("DLFWRDIS")
l2cc_dlfwrdis = coreComponent.createBooleanSymbol("L2CC_PCR_DLFWRDIS", l2cc_menu)
l2cc_dlfwrdis.setLabel(l2cc_pcr_dlfwrdis.getDescription())
l2cc_dlfwrdis.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_dlfwrdis.setVisible(False)

l2cc_pcr_dlen = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                 getRegister("L2CC_PCR").getBitfield("DLEN")
l2cc_dlen = coreComponent.createBooleanSymbol("L2CC_PCR_DLEN", l2cc_menu)
l2cc_dlen.setLabel(l2cc_pcr_dlen.getDescription())
l2cc_dlen.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_dlen.setVisible(False)

l2cc_powcr_stbyen = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                 getRegister("L2CC_POWCR").getBitfield("STBYEN")
l2cc_stbyen = coreComponent.createBooleanSymbol("L2CC_POWCR_STBYEN", l2cc_menu)
l2cc_stbyen.setLabel(l2cc_powcr_stbyen.getDescription())
l2cc_stbyen.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_stbyen.setVisible(False)

l2cc_powcr_dckgaten = Register.getRegisterModule("L2CC").getRegisterGroup("L2CC").\
                 getRegister("L2CC_POWCR").getBitfield("DCKGATEN")
l2cc_dckgaten = coreComponent.createBooleanSymbol("L2CC_POWCR_DCKGATEN", l2cc_menu)
l2cc_dckgaten.setLabel(l2cc_powcr_dckgaten.getDescription())
l2cc_dckgaten.setDependencies(update_component_visability, ["L2CC_ENABLE"])
l2cc_dckgaten.setVisible(False)

#TODO: Add interrupt support
#just register the handlers, let the application enable the interrupts

configName = Variables.get("__CONFIGURATION_NAME")

l2ccHeaderFile = coreComponent.createFileSymbol("l2ccHeaderFile", None)
l2ccHeaderFile.setSourcePath("../peripheral/l2cc_11160/templates/plib_l2cc.h.ftl")
l2ccHeaderFile.setOutputName("plib_l2cc.h")
l2ccHeaderFile.setDestPath("peripheral/l2cc/")
l2ccHeaderFile.setProjectPath("config/" + configName + "/peripheral/l2cc/")
l2ccHeaderFile.setType("HEADER")
l2ccHeaderFile.setMarkup(True)
l2ccHeaderFile.setEnabled(False)
l2ccHeaderFile.setDependencies(update_file_generation_enabled,["L2CC_ENABLE"])

l2ccSourceFile = coreComponent.createFileSymbol("l2ccSourceFile", None)
l2ccSourceFile.setSourcePath("../peripheral/l2cc_11160/templates/plib_l2cc.c.ftl")
l2ccSourceFile.setOutputName("plib_l2cc.c")
l2ccSourceFile.setDestPath("peripheral/l2cc/")
l2ccSourceFile.setProjectPath("config/" + configName + "/peripheral/l2cc/")
l2ccSourceFile.setType("SOURCE")
l2ccSourceFile.setMarkup(True)
l2ccSourceFile.setEnabled(False)
l2ccSourceFile.setDependencies(update_file_generation_enabled,["L2CC_ENABLE"])

l2ccSystemInitFile = coreComponent.createFileSymbol("l2ccSystemInitFile", None)
l2ccSystemInitFile.setType("STRING")
l2ccSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
l2ccSystemInitFile.setSourcePath("../peripheral/l2cc_11160/templates/system/system_initialize.c.ftl")
l2ccSystemInitFile.setMarkup(True)
l2ccSystemInitFile.setEnabled(False)
l2ccSystemInitFile.setDependencies(update_file_generation_enabled,["L2CC_ENABLE"])

l2ccSystemDefFile = coreComponent.createFileSymbol("l2ccSystemDefFile", None)
l2ccSystemDefFile.setType("STRING")
l2ccSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
l2ccSystemDefFile.setSourcePath("../peripheral/l2cc_11160/templates/system/system_definitions.h.ftl")
l2ccSystemDefFile.setMarkup(True)
l2ccSystemDefFile.setEnabled(False)
l2ccSystemDefFile.setDependencies(update_file_generation_enabled,["L2CC_ENABLE"])
