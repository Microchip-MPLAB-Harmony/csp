import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import LoadDynamicComponents from "clock-common/lib/Components/Dynamic/LoadDynamicComponents";
import { useContext, useState } from "react";
import {
  InputNumber,
  KeyValueSetRadio,
  PluginConfigContext,
  useBooleanSymbol,
  useIntegerSymbol,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import {
    getAllSymbolsFromJSON,
    getDynamicLabelsFromJSON,
    getDynamicSymbolsFromJSON
  } from 'clock-common/lib/Tools/ClockJSONTools';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';



const MDSLClockBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);

  const [dynamicSymbolInfo] = useState(() => getDynamicSymbolsFromJSON(props.clockController));
  const [dynamicSymbolLabelInfo] = useState(() => getDynamicLabelsFromJSON(props.clockController));
  
  const slck_xtralsel_en = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_SLCK_TDXTALSEL",
  });
  const slck_ext_frq = useIntegerSymbol({
    componentId,
    symbolId: "CLK_SLCK_EXT_FREQ",
  });

  const slck_oscbypass_en = useBooleanSymbol({
    componentId,
    symbolId: "CLK_SLCK_OSCBYPASS",
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
        keyValueSetSymbolHook={slck_xtralsel_en}
        classPrefix="slck_xtralsel_en"
        classResolver={props.cx}
      />
      <InputNumber
        integerSymbolHook={slck_ext_frq}
        className={props.cx("slck_ext_frq")}
        disabled={!slck_oscbypass_en.value}
      />
    </div>
  );
};

export default MDSLClockBox;
