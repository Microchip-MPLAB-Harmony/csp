import { SymbolProps, useIntegerSymbol } from '@mplab_harmony/harmony-plugin-client-lib';

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
      <label
        className={props.class}
        title={props.labelTooltip}
        style={{
          color:
            clockFreq.value < props.minValue || clockFreq.value > props.maxValue ? 'red' : 'black',
          fontWeight: props.boldLabelStatus === true ? 'bold' : 'initial'
        }}>
        {clockFreq.value} Hz
      </label>
    </div>
  );
};
export default FrequencyLabelRangeComponent;
