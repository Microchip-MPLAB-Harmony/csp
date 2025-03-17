import { SymbolProps } from '@mplab_harmony/harmony-plugin-client-lib';
import IntegerFrequencyLabel from './IntegerFrequencyLabel';
import StringFrequencyLabel from './StringFrequencyLabel';
import { LabelProps } from '../FrequencyLabelComponent';
import LongFrequencyLabel from './LongFrequencyLabel';
interface LabelNewProps extends LabelProps {
  symbolType: string;
}
const FrequencyLabelBySymbolType = (props: SymbolProps & LabelNewProps) => {
  switch (props.symbolType) {
    case 'IntegerSymbol':
      return (
        <>
          <IntegerFrequencyLabel {...props} />
        </>
      );
    case 'StringSymbol':
      return (
        <>
          <StringFrequencyLabel {...props} />
        </>
      );
    case 'LongSymbol':
      return (
        <>
          <LongFrequencyLabel {...props} />
        </>
      );
    default:
      break;
  }
  return null;
};
export default FrequencyLabelBySymbolType;
