import React, { useContext } from "react";
import {
  createClassResolver,
  InputFloat,
  InputLong,
  PluginConfigContext,
  useFloatSymbol,
  useLongSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import positions from "../../../styles/positions.module.css";
import useSymbolControl from "../../channelConfig/useSymbolControl";
import useADCModuleConfig from "../useADCModuleConfig";

type SamplingSymbolProps = {
  clockDividerSymbol: string;
  sampleCountSymbol: string;
  conversionRateSymbol: string;
  tadSymbol: string;
  moduleId: number;
};

const cx = createClassResolver(positions);
const SamplingComponent = ({
  conversionRateSymbol,
  tadSymbol,
  moduleId,
  clockDividerSymbol,
  sampleCountSymbol,
}: SamplingSymbolProps) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const { sharedModuleId } = useADCModuleConfig();
  const { NUM_CHANNELS_COUNT, NUM_SIGNALS_COUNT } = useSymbolControl();
  const sharedADCdat = `[${NUM_CHANNELS_COUNT} - ${NUM_SIGNALS_COUNT - 1}]`;
  const conversionRate = useFloatSymbol({
    componentId,
    symbolId: conversionRateSymbol,
  });
  const tad = useFloatSymbol({
    componentId,
    symbolId: tadSymbol,
  });
  const clkDiv = useLongSymbol({
    componentId,
    symbolId: clockDividerSymbol,
  });
  const sampleCount = useLongSymbol({
    componentId,
    symbolId: sampleCountSymbol,
  });
  return (
    <div>
      <label className={cx("conversionRate")}>
        {Math.floor(conversionRate.value)}
      </label>
      <label className={cx("tad")}>TAD = {tad.value.toFixed(3)} ns</label>
      <label className={cx("adcData")}>
        ADCDAT{moduleId === sharedModuleId ? sharedADCdat : moduleId}
      </label>
      <InputLong
        longSymbolHook={clkDiv}
        className={cx("clkDiv")}
        hidden={false}
      ></InputLong>
      <InputLong
        longSymbolHook={sampleCount}
        className={cx("sampleCount")}
        hidden={false}
      ></InputLong>
    </div>
  );
};

export default SamplingComponent;
