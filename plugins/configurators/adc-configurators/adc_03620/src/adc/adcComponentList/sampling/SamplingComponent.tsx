import React, { useContext } from "react";
import {
  createClassResolver,
  InputNumber,
  PluginConfigContext,
  useCommentSymbol,
  useIntegerSymbol,
  useStringSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import positions from "../../../styles/positions.module.css";

type SamplingSymbolProps = {
  moduleId: number;
};

const cx = createClassResolver(positions);
const SamplingComponent = ({ moduleId }: SamplingSymbolProps) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const clckFreq = useCommentSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_ADC_CLOCK_FREQ`,
  });
  const commentData = clckFreq.label.split(",");
  const actualRate = useStringSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_ADC_CONVERSION_RATE`,
  });
  const clkDiv = useIntegerSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_CORCTRL_ADCDIV`,
  });
  const sampleCount = useIntegerSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_CORCTRL_SAMC`,
  });

  const numChannels = useIntegerSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_NUM_CHANNELS`,
  });


  return (
    <div>
      <InputNumber
        integerSymbolHook={clkDiv}
        className={cx("clkDiv")}
        hidden={false}
      ></InputNumber>
      <InputNumber
        integerSymbolHook={sampleCount}
        className={cx("sampleCount")}
        hidden={false}
      ></InputNumber>
      <label className={cx("clockSource")}>{commentData[0]}</label>
      <label className={cx("tad")}>{commentData[1]}</label>
      <label className={cx("actualRate")}>{actualRate.value}</label>
      <label className={cx("snLabel")}>{numChannels.value}</label>
    </div>
  );
};

export default SamplingComponent;
