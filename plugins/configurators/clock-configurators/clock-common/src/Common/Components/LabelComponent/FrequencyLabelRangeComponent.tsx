import { SymbolProps, useIntegerSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import PlainLabel from './PlainLabel';
import FrequencyLabelComponent from './FrequencyLabelComponent';
import { GetClockDisplayFreqValue } from '../../Tools/Tools';

interface LabelProps {
  class: string;
  minValue: number;
  maxValue: number;
  labelTooltip: string;
  boldLabelStatus?: boolean;
}

const FrequencyLabelRangeComponent = (props: SymbolProps & LabelProps) => {
  const clockFreq = useIntegerSymbol(props);
  return (
    <div>
      <PlainLabel
        disPlayText={GetClockDisplayFreqValue(clockFreq.value)}
        redColorStatus={clockFreq.value < props.minValue || clockFreq.value > props.maxValue}
        booldStatus={props.boldLabelStatus}
        className={props.class}
      />
    </div>
  );
};
export default FrequencyLabelRangeComponent;
