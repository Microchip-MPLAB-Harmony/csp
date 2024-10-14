import { SymbolProps } from '@mplab_harmony/harmony-plugin-client-lib';
import IntegerFrequencyLabel from './IntegerFrequencyLabel';
import StringFrequencyLabel from './StringFrequencyLabel';
import { LabelProps } from '../FrequencyLabelComponent';
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
    default:
      break;
  }
  return null;
};
export default FrequencyLabelBySymbolType;
