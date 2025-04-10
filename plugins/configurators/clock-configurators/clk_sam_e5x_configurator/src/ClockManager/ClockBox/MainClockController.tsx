import {
  PluginConfigContext,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import LoadDynamicComponents from "clock-common/lib/Components/Dynamic/LoadDynamicComponents";
import LoadDynamicFreqencyLabels from "clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels";
import PlainLabel from "clock-common/lib/Components/LabelComponent/PlainLabel";
import ResetSymbolsIcon from "clock-common/lib/Components/ResetSymbolsIcon";
import {
  getDynamicLabelsFromJSON,
  getDynamicSymbolsFromJSON,
} from "clock-common/lib/Tools/ClockJSONTools";
import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import { removeDuplicates } from "clock-common/lib/Tools/Tools";
import { useContext, useState } from "react";

const MainClockController = (props: {
  mainClockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);
  const mainClockDiv = useKeyValueSetSymbol({
    componentId,
    symbolId: "CONF_CPU_CLOCK_DIVIDER",
  });
  let symbols: any = props.mainClockController
    .map((e) => e.symbol_id)
    .filter((e) => e !== undefined);
  symbols = removeDuplicates(symbols);

  const [dynamicSymbolsInfo] = useState(() =>
    getDynamicSymbolsFromJSON(props.mainClockController)
  );
  const [dynamicLabelSymbolInfo] = useState(() =>
    getDynamicLabelsFromJSON(props.mainClockController)
  );
  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        dynamicSymbolsInfo={dynamicSymbolsInfo}
        cx={props.cx}
      />
      <LoadDynamicFreqencyLabels
        componentId={componentId}
        dynamicLabelSymbolsInfo={dynamicLabelSymbolInfo}
        cx={props.cx}
      />
      <PlainLabel
        disPlayText={mainClockDiv.selectedOption.replace("DIV", "")}
        className={props.cx("cpuDivLabel")}
      />
      <ResetSymbolsIcon
        tooltip="Reset Main Clock symbols to default value"
        className={props.cx("mainClockReset")}
        componentId={componentId}
        resetSymbolsArray={symbols}
      />
    </div>
  );
};
export default MainClockController;
