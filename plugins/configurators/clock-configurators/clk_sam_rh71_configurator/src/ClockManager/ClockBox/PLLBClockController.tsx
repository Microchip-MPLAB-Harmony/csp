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
  "CLK_PLLBCK_FREQ_VCO",
  "CLK_PLLBCK_SRB",
  "CLK_PLLBCK_SCB",
  "CLK_PLLBCK_OUTCUR"
];

const PLLBClockController = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);

  const [dynamicSymbolInfo] = useState(() => getDynamicSymbolsFromJSON(props.clockController));
  const [dynamicSymbolLabelInfo] = useState(() => getDynamicLabelsFromJSON(props.clockController));
  
  const pllbMulLbl = useIntegerSymbol({
    componentId,
    symbolId: "CLK_PLLBCK_MULB",
  });
  const pllbDivLbl = useIntegerSymbol({
    componentId,
    symbolId: "CLK_PLLBCK_DIVB",
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
        cx={props.cx}
      />
      <PlainLabel
        disPlayText={`(${pllbMulLbl.value} + 1)`}
        className={props.cx("pllbMulLbl")}
        booldStatus
      />
      <PlainLabel
        disPlayText={pllbDivLbl.value+''}
        className={props.cx("pllbDivLbl")}
        booldStatus
      />
      <SettingsDialog
        tooltip="Advanced Settings"
        componentId={componentId}
        className={props.cx("pllbSet")}
        symbolArray={settingsArray}
        dialogWidth="50rem"
        dialogHeight="47rem"
      />
      <ResetSymbolsIcon
        tooltip="Reset Clock symbols to default value"
        className={props.cx("pllbReset")}
        componentId={componentId}
        resetSymbolsArray={settingsArray}
      />
    </div>
  );
};

export default PLLBClockController;
