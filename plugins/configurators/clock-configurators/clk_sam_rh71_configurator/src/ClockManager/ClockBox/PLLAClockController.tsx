import ResetSymbolsIcon from "clock-common/lib/Components/ResetSymbolsIcon";
import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import SettingsDialog from "clock-common/lib/Components/SettingsDialog";
import LoadDynamicComponents from "clock-common/lib/Components/Dynamic/LoadDynamicComponents";
import PlainLabel from "clock-common/lib/Components/LabelComponent/PlainLabel";
import { useContext, useState } from "react";
import {
  PluginConfigContext,
  useIntegerSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import {
    getAllSymbolsFromJSON,
    getDynamicLabelsFromJSON,
    getDynamicSymbolsFromJSON
  } from 'clock-common/lib/Tools/ClockJSONTools';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';

const settingsArray = [
  "CLK_PLLACK_FREQ_VCO",
  "CLK_PLLACK_SRA",
  "CLK_PLLACK_SCA",
  "CLK_PLLACK_OUTCUR",
];

const PLLAClockController = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);

  const [dynamicSymbolInfo] = useState(() => getDynamicSymbolsFromJSON(props.clockController));
  const [dynamicSymbolLabelInfo] = useState(() => getDynamicLabelsFromJSON(props.clockController));
  
  const pllaMulLbl = useIntegerSymbol({
    componentId,
    symbolId: "CLK_PLLACK_MULA",
  });
  const pllaDivLbl = useIntegerSymbol({
    componentId,
    symbolId: "CLK_PLLACK_DIVA",
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
      <PlainLabel
        disPlayText={`(${pllaMulLbl.value} + 1)`}
        className={props.cx("pllaMulLbl")}
        booldStatus
      />
      <PlainLabel
        disPlayText={pllaDivLbl.value+''}
        className={props.cx("pllaDivLbl")}
        booldStatus
      />
      <SettingsDialog
        tooltip="Advanced Settings"
        componentId={componentId}
        className={props.cx("pllaSet")}
        symbolArray={settingsArray}
        dialogWidth="50rem"
        dialogHeight="47rem"
      />
      <ResetSymbolsIcon
        tooltip="Reset Clock symbols to default value"
        className={props.cx("pllaReset")}
        componentId={componentId}
        resetSymbolsArray={settingsArray}
      />
    </div>
  );
};

export default PLLAClockController;
