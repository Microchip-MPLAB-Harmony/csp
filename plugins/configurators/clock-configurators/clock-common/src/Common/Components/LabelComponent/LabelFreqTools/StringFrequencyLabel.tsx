import { SymbolProps, useStringSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import PlainLabel from '../PlainLabel';
import { GetClockDisplayFreqValue } from '../../../Tools/Tools';
import { LabelProps } from '../FrequencyLabelComponent';

const StringFrequencyLabel = (props: SymbolProps & LabelProps) => {
  const clockFreq = useStringSymbol(props);
  const formattedClockFreq = Number(clockFreq.value).toLocaleString();
  return (
    <div>
      <PlainLabel
        disPlayText={GetClockDisplayFreqValue(Number(clockFreq.value))}
        redColorStatus={
          (props.redColorForZeroFrequency === true && Number(clockFreq.value) === 0) ||
          props.minMaxOutofRangeRedColorStatus === true
        }
        booldStatus={props.boldLabelStatus}
        toolTip={
          props.tooltip
            ? `${formattedClockFreq} Hz ( ${props.tooltip} )`
            : `${formattedClockFreq} Hz`
        }
        className={props.className}
      />
    </div>
  );
};
export default StringFrequencyLabel;
