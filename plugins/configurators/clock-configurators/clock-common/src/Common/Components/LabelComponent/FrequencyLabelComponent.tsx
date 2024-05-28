import { SymbolProps, useIntegerSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
interface LabelProps {
  class: string;
  boldLabelStatus?: boolean;
  redColorForZeroFrequency?: boolean;
}
const FrequencyLabelComponent = (props: SymbolProps & LabelProps) => {
  const clockFreq = useIntegerSymbol(props);
  return (
    <div>
      <label
        className={props.class}
        style={{
          color: props.redColorForZeroFrequency && clockFreq.value === 0 ? 'red' : 'black',
          fontWeight: props.boldLabelStatus === true ? 'bold' : 'initial'
        }}>
        {clockFreq.value} Hz
      </label>
    </div>
  );
};
export default FrequencyLabelComponent;
