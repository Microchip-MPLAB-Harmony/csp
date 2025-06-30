import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import { useContext, useEffect, useState } from "react";
import {
  booleanSymbolApi,
  CheckBox,
  DropDown,
  InputNumber,
  KeyValueSetRadio,
  PluginConfigContext,
  useBooleanSymbol,
  useIntegerSymbol,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import {
  getDynamicLabelsFromJSON,
} from "clock-common/lib/Tools/ClockJSONTools";
import LoadDynamicFreqencyLabels from "clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels";

const MainClockController = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);
  const [dynamicSymbolLabelInfo] = useState(() =>
    getDynamicLabelsFromJSON(props.clockController)
  );

  const clk_main_moscsel = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_MAINCK_MOSCSEL",
  });
  const clk_main_moscrcf = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_MAINCK_MOSCRCF",
  });
  const clk_moscrcen = useBooleanSymbol({
    componentId,
    symbolId: "CLK_MAINCK_MOSCRCEN",
  });
  

  const clk_moscxt_freq = useIntegerSymbol({
    componentId,
    symbolId: "CLK_MAINCK_FREQ",
  });

    useEffect(() => {
    if (clk_main_moscsel.selectedOptionPair?.value === "0" && !clk_moscrcen.value) {
      booleanSymbolApi.setValue(componentId, "CLK_MAINCK_MOSCRCEN", true);
    }
     if (clk_main_moscsel.selectedOptionPair?.value === "1" && clk_moscrcen.value) {
      booleanSymbolApi.setValue(componentId, "CLK_MAINCK_MOSCRCEN", false);
    }
  }, [clk_main_moscsel.selectedOptionPair?.value]);

  return (
    <div>
      <LoadDynamicFreqencyLabels
        componentId={componentId}
        dynamicLabelSymbolsInfo={dynamicSymbolLabelInfo}
        redColorForZeroFrequency={true}
        cx={props.cx}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={clk_main_moscsel}
        classPrefix="clk_main_moscsel"
        classResolver={props.cx}
      />
      <DropDown
        keyValueSetSymbolHook={clk_main_moscrcf}
        className={props.cx("clk_main_moscrcf")}
        disabled={clk_main_moscsel.selectedOptionPair?.value==='1'}
      />
      <InputNumber
        integerSymbolHook={clk_moscxt_freq}
        className={props.cx("clk_moscxt_freq")}
        disabled={clk_main_moscsel.selectedOptionPair?.value==='0'}
      />

      <CheckBox
        booleanSymbolHook={clk_moscrcen}
        className={props.cx("clk_moscrcen")}
        disabled={clk_main_moscsel.selectedOptionPair?.value==='1'}
      />
    </div>
  );
};

export default MainClockController;
