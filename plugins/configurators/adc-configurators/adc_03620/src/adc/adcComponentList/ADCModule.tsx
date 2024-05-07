import React, { useContext, useState } from "react";
import { ListBox } from "primereact/listbox";
import {
  createClassResolver,
  PluginConfigContext,
  CheckBoxDefault,
  useBooleanSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import positions from "../../styles/positions.module.css";
import useADCModuleConfig from "./useADCModuleConfig";
import SamplingComponent from "./sampling/SamplingComponent";
import ADCBooleanComponent from "./adcBooleanComponent/ADCBooleanComponent";
import ADCComboBoxComponent from "./adcComboBoxComponent/ADCComboBoxComponent";
import CommonADCSymbols from "./commonADCSymbols/CommonADCSymbols";
import ChannelConfiguration from "../channelConfig/ChannelConfiguration";
const cx = createClassResolver(positions);
const ADCComponentList = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const { adcModules } = useADCModuleConfig();
  const [selectedADC, setSelectedADC] = useState({
    name: "ADC CORE 0",
    moduleId: 0,
  });

  const AdcListTemplate = (options: any) => {
    const channelEnable = useBooleanSymbol({
      componentId,
      symbolId: `ADC_CORE_${options.moduleId}_ENABLE`,
    });
    return (
      <>
        <label
          style={{
            fontWeight: "bold",
            color: channelEnable.value ? "#82B366" : "",
          }}
        >
          ADC CORE {options.moduleId}{" "}
          {channelEnable.value ? "Enabled" : "Disabled"}
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
      <label className={cx("enableLabel")}> Enable</label>
      <CheckBoxDefault
        componentId={componentId}
        symbolId={`ADC_CORE_${selectedADC.moduleId}_ENABLE`}
        className={cx("channelEnable")}
      ></CheckBoxDefault>
      <ADCBooleanComponent moduleId={selectedADC.moduleId} />
      <ADCComboBoxComponent moduleId={selectedADC.moduleId} />
      <SamplingComponent moduleId={selectedADC.moduleId} />
      <CommonADCSymbols moduleId={selectedADC.moduleId} />
      <ChannelConfiguration moduleId={selectedADC.moduleId} />
    </>
  );
};

export default React.memo(ADCComponentList);
