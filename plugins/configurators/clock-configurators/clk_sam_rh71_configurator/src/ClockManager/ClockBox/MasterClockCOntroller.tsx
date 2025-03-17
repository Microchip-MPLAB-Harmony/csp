import ResetSymbolsIcon from "clock-common/lib/Components/ResetSymbolsIcon";
import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import LoadDynamicComponents from "clock-common/lib/Components/Dynamic/LoadDynamicComponents";
import { useContext, useState } from "react";
import {
  KeyValueSetRadio,
  PluginConfigContext,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import {
  getAllSymbolsFromJSON,
  getDynamicLabelsFromJSON,
  getDynamicSymbolsFromJSON,
} from "clock-common/lib/Tools/ClockJSONTools";
import LoadDynamicFreqencyLabels from "clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels";
import PlainLabel from "clock-common/lib/Components/LabelComponent/PlainLabel";
import FrequencyLabelComponent from "clock-common/lib/Components/LabelComponent/FrequencyLabelComponent";

const settingsArray = ['CLK_MCK_CSS','CLK_MCK_PRES','CLK_MCK_MDIV'
];

const MasterClockBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);
  const [allJsonSymbols] = useState<string[]>(
    getAllSymbolsFromJSON(props.clockController)
  );

  const [dynamicSymbolInfo] = useState(() =>
    getDynamicSymbolsFromJSON(props.clockController)
  );
  const [dynamicSymbolLabelInfo] = useState(() =>
    getDynamicLabelsFromJSON(props.clockController)
  );

  const clk_mck_css = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_MCK_CSS",
  });
  const clk_mck_pres = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_MCK_PRES",
  });
  const clk_mck_mdiv = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_MCK_MDIV",
  });
  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        dynamicSymbolsInfo={dynamicSymbolInfo}
        cx={props.cx}
      />
      <LoadDynamicFreqencyLabels
        componentId={componentId}
        dynamicLabelSymbolsInfo={dynamicSymbolLabelInfo}
        redColorForZeroFrequency={true}
        cx={props.cx}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={clk_mck_css}
        classPrefix="clk_mck_css"
        classResolver={props.cx}
      />
      <PlainLabel
        disPlayText={((clk_mck_pres.selectedOptionPair?.key)?.replace(/^\D+/g, ''))+''}
        className={props.cx("processorPresLabel")}
      />

      <PlainLabel
        disPlayText={clk_mck_mdiv.value +1 +""}
        className={props.cx("clk_mck_mdiv_lbl")}
      />
      <FrequencyLabelComponent
        className={props.cx("masterClkSlowLabeL")}
        componentId={componentId}
        symbolId="CLK_MD_SLCK_FREQ"
        boldLabelStatus={clk_mck_css.value===0}
      />
      <FrequencyLabelComponent
        className={props.cx("masterClkMainLabel")}
        componentId={componentId}
        symbolId="CLK_MAINCK_FREQ"
        boldLabelStatus={clk_mck_css?.value===1}
      />
      
      <FrequencyLabelComponent
        className={props.cx("masterClkPllaLabel")}
        componentId={componentId}
        symbolId="CLK_PLLACK_FREQ"
        boldLabelStatus={clk_mck_css?.value===2}
      />
      {/* <SettingsDialog
        tooltip="Advanced Settings"
        componentId={componentId}
        className={props.cx("dfllSetting")}
        symbolArray={settingsArray}
        dialogWidth="50rem"
        dialogHeight="47rem"
      />*/}
      <ResetSymbolsIcon
        tooltip="Reset Clock symbols to default value"
        className={props.cx("mcReset")}
        componentId={componentId}
        resetSymbolsArray={settingsArray}
      /> 
    </div>
  );
};

export default MasterClockBox;
