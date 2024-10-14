import { SymbolProps, useIntegerSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import PlainLabel from '../PlainLabel';
import { GetClockDisplayFreqValue } from '../../../Tools/Tools';
import { LabelProps } from '../FrequencyLabelComponent';

const IntegerFrequencyLabel = (props: SymbolProps & LabelProps) => {
  const clockFreq = useIntegerSymbol(props);
  return (
    <div>
      <PlainLabel
        disPlayText={GetClockDisplayFreqValue(clockFreq.value)}
        redColorStatus={
          (props.redColorForZeroFrequency === true && clockFreq.value === 0) ||
          props.minMaxOutofRangeRedColorStatus === true
        }
        booldStatus={props.boldLabelStatus}
        toolTip={props.tooltip}
        className={props.className}
      />
    </div>
  );
};
export default IntegerFrequencyLabel;
