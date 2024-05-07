import React, { useContext, useEffect, useState } from "react";
import { ListBox } from "primereact/listbox";
import {
  createClassResolver,
  PluginConfigContext,
  CheckBoxDefault,
  useBooleanSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import positions from "../../styles/positions.module.css";
import DedicatedPinConfig from "./pinConfig/DedicatedPinConfig";
import useADCModuleConfig, { SymbolId } from "./useADCModuleConfig";
import CommonCheckBox from "./channelEnable/CommonCheckBox";
import ResolutionComponent from "./resolution/ResolutionComponent";
import SamplingComponent from "./sampling/SamplingComponent";
import TriggerSource from "./triggerSource/TriggerSource";
import ChannelConfiguration from "../channelConfig/ChannelConfiguration";
import { updateSVG } from "../SVGhandler";
const cx = createClassResolver(positions);
const ADCComponentList = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const {
    adcModules,
    getDedicatedSymbolIds,
    getSharedSymbolIds,
    sharedModuleId,
  } = useADCModuleConfig();

  const [selectedADC, setSelectedADC] = useState({
    name: "ADCHS 7 ENABLE",
    moduleId: sharedModuleId,
  });

  const [commonSymbols, setCommonSymbols] = useState<SymbolId>(
    getSharedSymbolIds(sharedModuleId)
  );
  
  useEffect(() => {
    if (selectedADC.moduleId !== sharedModuleId) {
      setCommonSymbols(getDedicatedSymbolIds(selectedADC.moduleId));
      updateSVG(false);
    } else {
      setCommonSymbols(getSharedSymbolIds(sharedModuleId));
      updateSVG(true);
    }
  }, [selectedADC]);

  const AdcListTemplate = (options: any) => {
    const channelEnable = useBooleanSymbol({
      componentId,
      symbolId: `ADCHS_${options.moduleId}_ENABLE`,
    });
    return (
      <>
        <label style={{fontWeight:'bold' ,color:channelEnable.value?'#82B366':''}}>
          ADC {options.moduleId} {channelEnable.value ? "Enabled" : "Disabled"}
        </label>
      </>
    );
  };

  return (
    <>
      <div className={cx("componentList")}>
        <ListBox
          value={selectedADC}
          onChange={(e) => {
            if (e.value) setSelectedADC(e?.value);
          }}
          options={adcModules}
          optionLabel="name"
          itemTemplate={AdcListTemplate}
        />
      </div>
      <CheckBoxDefault
        componentId={componentId}
        symbolId={commonSymbols.channelEnable}
        className={cx("channelEnable")}
      ></CheckBoxDefault>
      {selectedADC.moduleId !== sharedModuleId && (
        <CommonCheckBox
          inputScanSymbol={commonSymbols.inputScan}
          interruptSymbolo={commonSymbols.interrupt}
          signModeSymbol={commonSymbols.signMode}
          channelEnableSymbol={commonSymbols.channelEnable}
        />
      )}
      <ResolutionComponent resolutionSymbol={commonSymbols.resolution} />
      <SamplingComponent
        clockDividerSymbol={commonSymbols.clockDivider}
        conversionRateSymbol={commonSymbols.conversionRate}
        sampleCountSymbol={commonSymbols.sampleCount}
        tadSymbol={commonSymbols.tad}
        moduleId={selectedADC.moduleId}
      />
      <TriggerSource moduleId={selectedADC.moduleId}></TriggerSource>
      {selectedADC.moduleId !== sharedModuleId && (
        <DedicatedPinConfig moduleId={selectedADC.moduleId} />
      )}
      {selectedADC.moduleId === sharedModuleId && <ChannelConfiguration />}
    </>
  );
};

export default React.memo(ADCComponentList);
