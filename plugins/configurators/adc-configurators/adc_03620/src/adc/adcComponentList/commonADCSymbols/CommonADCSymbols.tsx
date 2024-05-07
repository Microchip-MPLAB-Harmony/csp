import React, { useContext } from "react";
import {
  createClassResolver,
  PluginConfigContext,
  useBooleanSymbol,
  CheckBox,
  useKeyValueSetSymbol,
  useIntegerSymbol,
  DropDown,
  InputNumber,
  useCommentSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import positions from "../../../styles/positions.module.css";
type Props = {
  moduleId: number;
};

const cx = createClassResolver(positions);
const CommonADCSymbols = ({ moduleId }: Props) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const VREFRDY = useBooleanSymbol({
    componentId,
    symbolId: `ADC_GLOBAL_CTLINTENSET_VREFRDY`,
  });
  const VREFUPD = useBooleanSymbol({
    componentId,
    symbolId: `ADC_GLOBAL_CTLINTENSET_VREFUPD`,
  });
  const VREFSelection = useKeyValueSetSymbol({
    componentId,
    symbolId: `ADC_GLOBAL_CTRLD_VREFSEL`,
  });
  const clockDivider = useIntegerSymbol({
    componentId,
    symbolId: `ADC_GLOBAL_CTRLD_CTLCKDIV`,
  });

  const clockFrequecncy = useIntegerSymbol({
    componentId,
    symbolId: `ADC_GLOBAL_INPUT_CLK_FREQ`,
  });
  const clockPeriod = useCommentSymbol({
    componentId,
    symbolId: `ADC_GLOBAL_CONTROL_CLOCK_PERIOD_TQ`,
  });
  const clockPeriodLabel = clockPeriod.label.split(",");

  return (
    <div>
      <CheckBox
        booleanSymbolHook={VREFRDY}
        className={cx("VREFRDY")}
        hidden={false}
        disabled={false}
      ></CheckBox>
      <CheckBox
        booleanSymbolHook={VREFUPD}
        className={cx("VREFUPD")}
        hidden={false}
        disabled={false}
      ></CheckBox>
      <DropDown
        keyValueSetSymbolHook={VREFSelection}
        className={cx("VREFSelection")}
        hidden={false}
        disabled={false}
      ></DropDown>
      <InputNumber
        integerSymbolHook={clockDivider}
        className={cx("clockDivider")}
      ></InputNumber>
      <label className={cx("clockFrequecncy")}>
        {clockFrequecncy.value} Hz
      </label>
      <label className={cx("controlClock")}>{clockPeriodLabel[0]} </label>
      <label className={cx("periodTQ")}>{clockPeriodLabel[1]} </label>
    </div>
  );
};

export default CommonADCSymbols;
